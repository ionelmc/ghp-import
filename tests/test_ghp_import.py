import pytest

from ghp_import.cli import main

pytest_plugins = 'pytester',


def test_main(testdir):
    pytest.raises(SystemExit, main)


def test_help(testdir):
    result = testdir.run('ghp-import', '--help')
    result.stdout.fnmatch_lines([
        'Usage: ghp-import [OPTIONS] DIRECTORY',
        '',
        'Options:',
        '  -n          Include a .nojekyll file in the branch.',
        '  -m MESG     The commit message to use on the target branch.',
        '  -p          Push the branch to origin/{branch} after committing.',
        '  -r REMOTE   The name of the remote to push to. [origin]',
        '  -b BRANCH   Name of the branch to write to. [gh-pages]',
        '  -h, --help  show this help message and exit',
    ])


def test_import_src(testdir):
    testdir.run('git', 'init', '.')
    output = testdir.mkdir('output')
    output.join('foobar.txt').write('abc')
    result = testdir.run('ghp-import', 'output')
    assert result.stdout.lines == []
    assert result.stderr.lines == []

    output.join('abc.txt').write('abc')
    result = testdir.run('ghp-import', 'output')
    assert result.stdout.lines == []
    assert result.stderr.lines == []
