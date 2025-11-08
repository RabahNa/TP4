import os
import sys
BAD_HASH = "c1a4be04b972b6c17db242fc37752ad517c29402"
GOOD_HASH = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
os.system(f"git bisect start {BAD_HASH} {GOOD_HASH}")
exit_code = os.system("python manage.py test > result.log 2>&1")
sys.exit(exit_code)
