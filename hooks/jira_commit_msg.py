"""
git commit message에 현재 git branch의 jira 티켓 번호가 포함되어 있는지 검증합니다.
"""
import argparse
import os
from typing import Optional, Sequence

from .consts import TICKET_ID
from .helpers import get_commit_msg, get_current_branch_name, get_ticket_id, is_special_commit


def abort(error_msg: str) -> None:
    print(f"[COMMIT ABORTED] {error_msg}")


def match_current_branch(commit_msg: str) -> bool:
    current_branch = get_current_branch_name()
    current_ticket_id = get_ticket_id(current_branch)
    if not current_ticket_id:
        return True

    return commit_msg.startswith(current_ticket_id)


def is_empty_msg(commit_msg: str) -> bool:
    return not TICKET_ID.sub("", commit_msg).strip()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    commit_msg = get_commit_msg(args.filename)

    if is_special_commit(commit_msg):
        return os.EX_OK

    elif not TICKET_ID.match(commit_msg):
        abort("Commit message should start with ticket number.")
        return os.EX_DATAERR

    elif not match_current_branch(commit_msg):
        abort("Ticket number in commit message should match current branch name.")
        return os.EX_DATAERR

    elif is_empty_msg(commit_msg):
        abort("Commit message should have content (except ticket number).")
        return os.EX_DATAERR

    return os.EX_OK


if __name__ == "__main__":
    exit(main())
