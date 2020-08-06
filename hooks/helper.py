import subprocess

from .consts import BRANCH_TICKET_ID


def is_special_commit(commit_msg: str):
    return commit_msg.startswith(("Merge ", "Revert ", "Revert:"))


def get_commit_msg(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


def get_current_branch_name() -> str:
    return subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
    ).stdout.strip().decode("utf-8")


def get_ticket_id(branch: str) -> str:
    ticket_id = BRANCH_TICKET_ID.match(branch)
    return ticket_id.group().upper() if ticket_id else ""
