import re
import subprocess
import sys

# Patterns representing common secret formats
BAD_PATTERNS = [
    r"AKIA[0-9A-Z]{16}",            # AWS Access Key
    r"-----BEGIN (RSA|EC|OPENSSH)", # Private key headers
    r"xox[baprs]-",                 # Slack tokens
    r"sk-[A-Za-z0-9]{20,}",         # Generic API keys
]

try:
    diff = subprocess.check_output(
        ["git", "diff", "--cached"], text=True
    )
except subprocess.CalledProcessError:
    sys.exit(0)

for pattern in BAD_PATTERNS:
    if re.search(pattern, diff):
        print(f"Blocked: Potential secret detected (pattern: {pattern})")
        sys.exit(1)

sys.exit(0)
