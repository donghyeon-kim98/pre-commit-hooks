import subprocess

from .consts import BRANCH_TICKET_ID, SPECIAL_COMMIT


def is_special_commit(commit_msg: str) -> bool:
    return commit_msg.startswith(SPECIAL_COMMIT)


def get_commit_msg(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def get_current_branch_name() -> str:
    # fmt: off
    return subprocess.run(
        ["git", "branch", "--show-current"],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    ).stdout.strip()
    # fmt: on


def get_ticket_id(branch: str) -> str:
    ticket_id = BRANCH_TICKET_ID.match(branch)
    return ticket_id.group().upper() if ticket_id else ""
