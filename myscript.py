import os
import sys
BAD_HASH = "badhash"
GOOD_HASH = "goodhash"
os.system(f"git bisect start {BAD_HASH} {GOOD_HASH}")
exit_code = os.system("python -m pytest > result.log 2>&1")
sys.exit(exit_code)
