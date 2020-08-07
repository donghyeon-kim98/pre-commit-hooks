import argparse
from typing import Optional, Sequence

from .consts import PASS, TICKET_ID
from .helper import get_commit_msg, get_current_branch_name, get_ticket_id


def add_ticket_id(filename: str, ticket_id: str) -> None:
    with open(filename, "r+") as f:
        commit_msg = f.read()
        f.seek(0)
        f.write(f"{ticket_id} {commit_msg}")
        f.truncate()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)

    if not TICKET_ID.match(get_commit_msg(args.filename)):
        add_ticket_id(
            filename=args.filename, ticket_id=get_ticket_id(get_current_branch_name()),
        )

    return PASS


if __name__ == "__main__":
    exit(main())
