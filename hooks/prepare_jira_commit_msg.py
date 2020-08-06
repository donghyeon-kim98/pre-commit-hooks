import argparse
import re
import subprocess

PASS = 0
FAIL = 1
BRANCH_TICKET_ID = re.compile(r'[a-z]{2,}-[0-9]+')
TICKET_ID = re.compile(r'(?!PEP-8)[A-Z]{2,}-[0-9]+')


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


def add_ticket_id(filename: str, commit_msg: str, ticket_id: str) -> None:
    with open(filename, "w") as f:
        f.write(f"{ticket_id} {commit_msg}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    commit_msg = get_commit_msg(args.filename)
    current_branch = get_current_branch_name()
    current_ticket_id = get_ticket_id(current_branch)

    if not TICKET_ID.match(commit_msg):
        add_ticket_id(args.filename, commit_msg, current_ticket_id)

    return PASS


if __name__ == '__main__':
    exit(main())
