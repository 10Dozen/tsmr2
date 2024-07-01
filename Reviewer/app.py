from app.reviewer import Reviewer

import os
import sys
import shutil
import zipfile
import requests

TEMP_DIR = "temp"
TEMP_ARCHIVE = "temp_mission.zip"

def resolve_mission_path(path):
    if not path.startswith('https'):
        return path

    mission_filename_zip = path.rsplit('/', maxsplit=1)[-1]
    if path.startswith('https://github.com/TacticalShift/mmo/'):
        path = 'https://raw.githubusercontent.com/TacticalShift/mmo/main/' + mission_filename_zip
    
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    os.mkdir(TEMP_DIR)
    r = requests.get(path)
    with open(TEMP_ARCHIVE, mode="wb") as f:
        f.write(r.content)

    zf = zipfile.ZipFile(TEMP_ARCHIVE)
    zf.extractall(path=TEMP_DIR)
    
    return os.path.join(TEMP_DIR, mission_filename_zip.rsplit('.', maxsplit=1)[0])


if __name__ == '__main__':
    print('┌-------------------------------------┐')
    print('|     tS Mission Reviewer v2.0.0      |')
    print('└-------------------------------------┘')
    print()

    #path = r'C:\Vaults\a3\tsmr\CO29_Space_Shield.ProvingGrounds_PMC'
    # path = r'E:\10Dozen Workstation and Porn\Github\tsmr2\CO28_Scimitars_Drawn.DYA'
    path = r'https://github.com/TacticalShift/mmo/blob/main/COTVT25_Steal_Beasts.WL_Rosche.zip'
    # while not os.path.exists(path):
    #     path = input('Enter path to reviewed mission:')

    path = resolve_mission_path(path)
    op_result = Reviewer(path).review()

    if path.startswith(TEMP_DIR) and os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
        os.remove(TEMP_ARCHIVE)
        
    sys.exit(op_result)

