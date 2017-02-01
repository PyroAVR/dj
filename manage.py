#!/usr/bin/env python3
from shutil import copyfile, copytree
import os
import sys

source_files = [
    "index.html",
    "blurry-circles-1.jpg",
    "scripts/add.py",
    "data/songs.db"
]

dest_dir = "/var/www/dj/"


def export():
    for i in source_files:
        if os.path.isdir(i[0:i.rfind('/')]):
            if not os.path.exists(dest_dir + i[0:i.rfind('/')]):
                os.makedirs(dest_dir + i[0:i.rfind('/')])
        try:
            copytree(i, os.path.join(dest_dir + i))
        except OSError as exc:
            copyfile(i, os.path.join(dest_dir + i))

def help_text():
    print("""
manage.py - like Django, but simple b/c Django requires me to learn a framework.
help    - print this blurb.
export  - all files to directory.
    """)

def main():
        if len(sys.argv) < 2:
            help_text()
        elif sys.argv[1] == "help":
            help_text()
        elif sys.argv[1] == "export":
            export()
        else:
            pass

if __name__ == '__main__':
    main()
