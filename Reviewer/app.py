from app.reviewer import Reviewer

import os
import sys

if __name__ == '__main__':
    print('┌-------------------------------------┐')
    print('|     tS Mission Reviewer v2.0.0      |')
    print('└-------------------------------------┘')
    print()

    path = r'G:\tS\tS Mission Reviewer 2\CO23_The_Unquenchable_Fire.Desert_E'
    # while not os.path.exists(path):
    #     path = input('Enter path to reviewed mission:')

    sys.exit(Reviewer(path).review())
