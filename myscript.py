import os
BAD_HASH = "badhash"
GOOD_HASH = "goodhash"
os.system(f"git bisect start {BAD_HASH} {GOOD_HASH}")
os.system("git bisect run python -m pytest")
os.system("git bisect reset")
