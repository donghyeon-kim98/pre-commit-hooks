from pathlib import Path

import pytest

from scripts.write_hooks_md import EXCLUDE_FILES, HOOKS_DIR, find_hook_files, get_hook_docstrings, write_hooks_md


@pytest.fixture(params=EXCLUDE_FILES, scope="module")
def exclude_file(request):
    return request.param


@pytest.fixture(scope="module")
def dump_file_content():
    return '"""hello world"""\n\n\na = 1'


def test_should_find_only_hook_files(temp_git_dir, exclude_file):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir(HOOKS_DIR)
        temp_git_dir.join(HOOKS_DIR, exclude_file).write("hello_world")
        temp_git_dir.join(HOOKS_DIR, "hook.py").write("hello_world")

        assert [f for f in find_hook_files()] == [Path(HOOKS_DIR, "hook.py")]


def test_should_return_name_with_hyphen_and_docstring_of_hook_file(temp_git_dir, dump_file_content):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir(HOOKS_DIR)
        temp_git_dir.join(HOOKS_DIR, "hook_name.py").write(dump_file_content)

        assert get_hook_docstrings() == {"hook-name": "hello world"}


def test_should_write_hooks_md_with_hook_names_and_docstrings(temp_git_dir, dump_file_content):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir(HOOKS_DIR)
        temp_git_dir.join(HOOKS_DIR, "hook_name_1.py").write(dump_file_content)
        temp_git_dir.join(HOOKS_DIR, "hook_name_2.py").write(dump_file_content)

        write_hooks_md()

        # fmt: off
        expected_content = (
            "# Hooks\n"
            "\n`hook-name-1`\n\n"
            "hello world\n"
            "\n`hook-name-2`\n\n"
            "hello world\n"
        )
        # fmt: on

        assert temp_git_dir.join("HOOKS.md").open("r").read() == expected_content
