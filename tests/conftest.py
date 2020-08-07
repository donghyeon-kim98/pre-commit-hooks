import subprocess

import pytest


class GitHelper:
    @staticmethod
    def checkout(branch: str, create: bool = True):
        cmd = ["git", "checkout"]
        if create:
            cmd.append("-b")
        cmd.append(branch)
        subprocess.run(cmd)

    @staticmethod
    def stage_new_file(filename: str = "a.file"):
        with open(filename, "w") as f:
            f.write("hello world")
        subprocess.run(["git", "add", filename])

    @staticmethod
    def commit(commit_msg: str):
        subprocess.run(["git", "commit", "-m", commit_msg])


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join("git_dir")
    subprocess.run(["git", "init", "--", str(git_dir)])
    return git_dir


@pytest.fixture
def commit_editmsg_ref(temp_git_dir):
    return str(temp_git_dir.join(".git/COMMIT_EDITMSG"))


@pytest.fixture(scope="session")
def ticket_id():
    return "YOGIYO-123"


@pytest.fixture(scope="session")
def branch_with_ticket_id(ticket_id):
    return f"{ticket_id.lower()}-test-branch"


@pytest.fixture(scope="session")
def git_helper():
    return GitHelper


@pytest.fixture(params=("Merge", "Revert"), scope="session")
def special_commit(request):
    return request.param
