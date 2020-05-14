import os
import sys

msg = sys.argv[1]
os.system("git add -A")
os.system(f"git commit -m \"{msg}\"")
os.system("git push")
print(msg)