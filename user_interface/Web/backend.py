import sys
sys.path.append('/mnt/c/Users/Vaskar/Documents/Projects/ClubFinder/data_matcher')
import match_data



def get_results(data):
    western_finder = ClubFinder("western")
    return western_finder.suggest_club(data)


if __name__ == "__main__":
    pass