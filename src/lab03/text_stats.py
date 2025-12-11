import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import libs.text


string = sys.stdin.readline()
libs.text.summarize(string)
