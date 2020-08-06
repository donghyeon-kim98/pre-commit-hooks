import re

PASS = 0
FAIL = 1
BRANCH_TICKET_ID = re.compile(r"[a-z]{2,}-[0-9]+")
TICKET_ID = re.compile(r"(?!PEP-8)[A-Z]{2,}-[0-9]+")
