import os
import sys

if __package__ == "":
    code_src_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, code_src_path)

from takathon.cli import takathon

if __name__ == "__main__":
    takathon()
