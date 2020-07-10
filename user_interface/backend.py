from __future__ import print_function	# For Py2/3 compatibility
import sys
sys.path.insert(0, '../../data_matcher')
from match_data import *
# insert at 1, 0 is the script path (or '' in REPL)



def get_results(data):
    western_finder = ClubFinder("western")
    return western_finder.suggest_club(data)


if __name__ == "__main__":
    pass