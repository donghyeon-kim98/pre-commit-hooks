import argparse
from typing import Optional, Sequence

from .consts import PASS, TICKET_ID
from .helper import get_commit_msg, get_current_branch_name, get_ticket_id


def add_ticket_id(filename: str, commit_msg: str, ticket_id: str) -> None:
    with open(filename, "w") as f:
        f.write(f"{ticket_id} {commit_msg}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    commit_msg = get_commit_msg(args.filename)
    current_branch = get_current_branch_name()
    current_ticket_id = get_ticket_id(current_branch)

    if not TICKET_ID.match(commit_msg):
        add_ticket_id(args.filename, commit_msg, current_ticket_id)

    return PASS


if __name__ == "__main__":
    exit(main())
