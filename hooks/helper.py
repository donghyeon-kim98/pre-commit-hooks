import subprocess

from .consts import BRANCH_TICKET_ID


def is_special_commit(commit_msg: str) -> bool:
    return commit_msg.startswith(("Merge", "Revert"))


def get_commit_msg(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def get_current_branch_name() -> str:
    # fmt: off
    return subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
    ).stdout.strip().decode("utf-8")
    # fmt: on


def get_ticket_id(branch: str) -> str:
    ticket_id = BRANCH_TICKET_ID.match(branch)
    return ticket_id.group().upper() if ticket_id else ""
