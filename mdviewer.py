# MarkdownViewer
# github.com/mazen428/MarkdownViewer
# License: GPL V 3.0


import ctypes
import os
import random
import string
import sys
import time
from os import path

import markdown

VER = "1.0.2"
ERROR = 0x10
pathname = str(" ".join(sys.argv[1:])).strip()
if not pathname:
    ctypes.windll.user32.MessageBoxW(None, "No path provided.", "Error", ERROR)
    sys.exit()

if not path.exists(pathname):
    ctypes.windll.user32.MessageBoxW(
        None,
        f'The path: "{pathname}" is either invalid or does not exist.',
        "Error",
        ERROR,
    )
    sys.exit()
tmpdir = path.normpath(path.expandvars("%temp%"))


def gen_filename():
    name = []
    charset = list(string.ascii_lowercase + string.digits + "-" + "_")
    random.shuffle(charset)
    for i in range(random.randint(16, 24)):
        name.append(random.choice(charset))
    return "".join(name)


def readfile(filepath):
    with open(filepath, "r") as fil:
        text = fil.read()
    return text.strip()


def writefile(filepath, data):
    with open(filepath, "w") as fil:
        fil.write(data)
    return True


if path.getsize(pathname) > 5242880:  # 5 megabytes
    ctypes.windll.user32.MessageBoxW(None, "The file is too large.", "Error", ERROR)
    sys.exit()

mdtext = readfile(pathname)
if not mdtext:
    ctypes.windll.user32.MessageBoxW(None, "This file is empty.", "Error", ERROR)
    sys.exit()
# extracting the title.
ttl = mdtext.splitlines()
ttl = [t for t in ttl[:10] if t.strip().strip(string.punctuation)][0]
ttl = ttl.strip(string.punctuation.replace(".", "")).strip()
pre_html = f"<html>\n<head>\n<title>{ttl}</title>\n</head>\n<body>\n<main>\n"
post_html = f'\n</main>\n<footer>\n<p>Converted using MarkdownViewer version {VER}.</p>\n<p><a href="https://github.com/mazen428/MarkdownViewer">GitHub</a></p>\n</footer>\n</body>\n</html>\n'
mdtext = markdown.markdown(mdtext)
mdtext = pre_html + mdtext + post_html
randomname = gen_filename() + ".html"
randompath = path.join(tmpdir, randomname)
writefile(randompath, mdtext)
os.startfile(randompath)
time.sleep(7)
os.remove(randompath)
sys.exit()
