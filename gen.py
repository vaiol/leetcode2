#!/usr/bin/python3

import os
import subprocess
import sys


def get_clipboard_data():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()


num = sys.argv[1]
folder_name = f"src/{num}"
file_name = f"{folder_name}/Solution.py"

clipboard_content = get_clipboard_data().decode("utf-8")
os.mkdir(folder_name)
text_file = open(file_name, 'w')
text_file.write(clipboard_content)
text_file.close()

print(file_name)
print(clipboard_content)
