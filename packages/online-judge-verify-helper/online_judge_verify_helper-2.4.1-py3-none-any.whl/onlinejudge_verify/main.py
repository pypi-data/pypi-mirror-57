# Python Version: 3.x
import argparse
import glob
import os
import pathlib
import subprocess
from logging import DEBUG, basicConfig, getLogger
from typing import *

import onlinejudge_verify.docs
import onlinejudge_verify.verify
import pkg_resources

package = 'onlinejudge_verify.data'
verify_yml = pkg_resources.resource_string(package, 'verify.yml')

logger = getLogger(__name__)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand')

    subparser = subparsers.add_parser('all')

    subparser = subparsers.add_parser('run')
    subparser.add_argument('path', nargs='*', type=pathlib.Path)

    subparser = subparsers.add_parser('init')

    subparser = subparsers.add_parser('export')
    subparser.add_argument('path', type=pathlib.Path)

    subparser = subparsers.add_parser('docs')

    return parser


def subcommand_run(paths: List[pathlib.Path]) -> None:
    """
    :raises Exception: if test.sh fails
    """

    does_push = 'GITHUB_ACTION' in os.environ and os.environ.get('GITHUB_REF', '').startswith('refs/heads/')  # NOTE: $GITHUB_REF may be refs/pull/... or refs/tags/...
    if does_push:
        # checkout in advance to push
        branch = os.environ['GITHUB_REF'][len('refs/heads/'):]
        logger.info('$ git checkout %s', branch)
        subprocess.check_call(['git', 'checkout', branch])

    if not paths:
        paths = list(map(pathlib.Path, glob.glob('**/*.test.cpp', recursive=True)))
    onlinejudge_verify.verify.main(paths)

    # push
    if does_push:
        push_timestamp_to_branch()


def push_timestamp_to_branch() -> None:
    # read config
    logger.info('use GITHUB_TOKEN')  # NOTE: don't use GH_PAT here, because it may cause infinite loops with triggering GitHub Actions itself
    url = 'https://{}:{}@github.com/{}.git'.format(os.environ['GITHUB_ACTOR'], os.environ['GITHUB_TOKEN'], os.environ['GITHUB_REPOSITORY'])
    logger.info('GITHUB_ACTOR = %s', os.environ['GITHUB_ACTOR'])
    logger.info('GITHUB_REPOSITORY = %s', os.environ['GITHUB_REPOSITORY'])

    # commit and push
    logger.info('$ git add .verify-helper && git commit && git push')
    subprocess.check_call(['git', 'config', '--global', 'user.name', 'GitHub'])
    subprocess.check_call(['git', 'config', '--global', 'user.email', 'noreply@github.com'])
    subprocess.check_call(['git', 'add', '.verify-helper/timestamp/'])
    if subprocess.run(['git', 'diff', '--quiet', '--staged']).returncode:
        message = '[auto-verifier] verify commit {}'.format(os.environ['GITHUB_SHA'])
        subprocess.check_call(['git', 'commit', '-m', message])
        subprocess.check_call(['git', 'push', url, 'HEAD'])


def subcommand_init() -> None:
    path = pathlib.Path('.github/workflows/verify.yml')
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), 'wb') as fh:
        fh.write(verify_yml.replace(b'git+https://github.com/kmyk/online-judge-verify-helper.git@master', b'"online-judge-verify-helper==2.*"'))


def push_documents_to_gh_pages(*, src_dir: pathlib.Path, dst_branch: str = 'gh-pages') -> None:
    # read config
    if os.environ.get('GH_PAT', None):
        logger.info('use GH_PAT')
        # see https://github.com/marketplace/actions/github-pages-deploy#secrets and https://github.com/maxheld83/ghpages/issues/1
        url = 'https://{}@github.com/{}.git'.format(os.environ['GH_PAT'], os.environ['GITHUB_REPOSITORY'])
    else:
        logger.info('use GITHUB_TOKEN')
        url = 'https://{}:{}@github.com/{}.git'.format(os.environ['GITHUB_ACTOR'], os.environ['GITHUB_TOKEN'], os.environ['GITHUB_REPOSITORY'])
    logger.info('GITHUB_ACTOR = %s', os.environ['GITHUB_ACTOR'])
    logger.info('GITHUB_REPOSITORY = %s', os.environ['GITHUB_REPOSITORY'])

    # read files before checkout
    logger.info('read files from %s', str(src_dir))
    src_files = {}
    for path in map(pathlib.Path, glob.glob(str(src_dir) + '/**/*', recursive=True)):
        if path.is_file():
            logger.info('%s', str(path))
            with open(str(path), 'rb') as fh:
                src_files[path.relative_to(src_dir)] = fh.read()

    # checkout gh-pages
    logger.info('$ git checkout %s', dst_branch)
    subprocess.check_call(['git', 'stash'])
    try:
        subprocess.check_call(['git', 'checkout', dst_branch])
    except subprocess.CalledProcessError:
        subprocess.check_call(['git', 'checkout', '--orphan', dst_branch])

    # remove all non-hidden files and write new files
    logger.info('write files to . on %s', dst_branch)
    for pattern in ('**/*', '.*/**/*'):
        for path in map(pathlib.Path, glob.glob(pattern, recursive=True)):
            if path.is_file() and path.parts[0] != '.git':
                path.unlink()
    for path, data in src_files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(str(path), 'wb') as fh:
            fh.write(data)

    # commit and push
    logger.info('$ git add . && git commit && git push')
    subprocess.check_call(['git', 'config', '--global', 'user.name', 'GitHub'])
    subprocess.check_call(['git', 'config', '--global', 'user.email', 'noreply@github.com'])
    subprocess.check_call(['git', 'add', '.'])
    if subprocess.run(['git', 'diff', '--quiet', '--staged']).returncode:
        message = '[auto-verifier] docs commit {}'.format(os.environ['GITHUB_SHA'])
        subprocess.check_call(['git', 'commit', '-m', message])
        subprocess.check_call(['git', 'push', url, 'HEAD'])


def subcommand_docs() -> None:
    if 'GITHUB_ACTION' in os.environ:
        if os.environ['GITHUB_REF'] == 'refs/heads/master':
            logger.info('generate documents...')
            onlinejudge_verify.docs.main(html=False, force=True)

            logger.info('upload documents...')
            push_documents_to_gh_pages(src_dir=pathlib.Path('md-output'))

    else:
        logger.info('generate documents...')
        onlinejudge_verify.docs.main(html=False, force=True)


def main(args: Optional[List[str]] = None) -> None:
    basicConfig(level=DEBUG)
    parser = get_parser()
    parsed = parser.parse_args(args)

    if parsed.subcommand == 'all':
        subcommand_run(paths=[])
        subcommand_docs()

    elif parsed.subcommand == 'run':
        subcommand_run(paths=parsed.path)

    elif parsed.subcommand == 'init':
        subcommand_init()

    elif parsed.subcommand == 'export':
        raise NotImplementedError('#include "hoge.hpp" みたいなやつをいい感じに展開してそのまま提出できる形コードを出力してほしい')

    elif parsed.subcommand == 'docs':
        subcommand_docs()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
