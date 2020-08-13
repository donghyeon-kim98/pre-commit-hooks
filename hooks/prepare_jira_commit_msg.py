"""
git commit message에 현재 git branch의 jira 티켓 번호를 추가합니다.
"""
import argparse
import os
from typing import Optional, Sequence

from .consts import TICKET_ID
from .helpers import get_commit_msg, get_current_branch_name, get_ticket_id


def add_ticket_id(filename: str, ticket_id: str) -> None:
    with open(filename, "r+") as f:
        commit_msg = f.read().strip()
        f.seek(0)
        f.write(f"{ticket_id} {commit_msg}\n")
        f.truncate()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    if not TICKET_ID.match(get_commit_msg(args.filename)):
        add_ticket_id(filename=args.filename, ticket_id=get_ticket_id(get_current_branch_name()))

    return os.EX_OK


if __name__ == "__main__":
    exit(main())
