from app.reviewer import Reviewer

import os
import sys



if __name__ == '__main__':
    print('┌-------------------------------------┐')
    print('|     tS Mission Reviewer v2.0.0      |')
    print('└-------------------------------------┘')
    print()

    #path = r'C:\Vaults\a3\tsmr\tsmr2-main\CO29_Space_Shield.ProvingGrounds_PMC'
    path = r'E:\10Dozen Workstation and Porn\Github\tsmr2\Reviewer\CO28_Scimitars_Drawn.DYA'
    # while not os.path.exists(path):
    #     path = input('Enter path to reviewed mission:')

    sys.exit(Reviewer(path).review())
