from app.reviewer import Reviewer

import os
import sys
import shutil
import requests

DEBUG = False
def log_msg(msg):
    DEBUG and print(f'[{__file__}] {msg}')


TEMP_DIR = "temp"
TEMP_ARCHIVE = "temp_mission"


def resolve_mission_path(path):
    if not path.startswith('https'):
        return path

    mission_filename, file_ext = path.rsplit("/", maxsplit=1)[-1].rsplit('.', maxsplit=1)

    if path.startswith('https://github.com/TacticalShift/mmo/'):
        path = 'https://raw.githubusercontent.com/TacticalShift/mmo/main/' + mission_filename + '.' + file_ext

    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    os.mkdir(TEMP_DIR)
    archive = f"{TEMP_ARCHIVE}.{file_ext}"
    r = requests.get(path)
    with open(os.path.join(TEMP_DIR, archive), mode="wb") as f:
        f.write(r.content)

    if file_ext == 'zip':
        import time
        import zipfile

        with zipfile.ZipFile(os.path.join(TEMP_DIR, archive)) as zf:
            log_msg(f"(Zip) Infolist: {zf.infolist()}")
            for file in zf.infolist():
                name, date_time = file.filename, file.date_time
                log_msg(f"(Zip) Extracting file: {name}")
                log_msg(f"(Zip) Is dir: {file.is_dir()}")

                nested_dirs = name.split('/')
                if not file.is_dir():
                    nested_dirs = nested_dirs[:-1]
                log_msg(f"(Zip) Path to file: {nested_dirs}")

                dr = TEMP_DIR
                for nd in nested_dirs:
                    dr = os.path.join(dr, nd)
                    if not os.path.exists(dr):
                        log_msg(f"(Zip) Creating new dir {nested_dirs}")
                        os.mkdir(dr)

                pathname = os.path.join(TEMP_DIR, *os.path.split(name))

                if file.is_dir():
                    log_msg(f"(Zip) Directory created, nothing to extract")
                    continue

                log_msg(f"(Zip) Going to extract file {file} ==> {pathname}")
                with open(pathname, "wb") as out:
                    out.write(zf.open(file).read())
                    log_msg("(Zip) file written")

                date_time = time.mktime(date_time + (0,0,-1))

                log_msg("(Zip) set timestamp")
                os.utime(pathname, (date_time, date_time))

                # zf.extract(name, path=TEMP_DIR)
        # zipfile.ZipFile(os.path.join(TEMP_DIR, archive)).extractall(path=TEMP_DIR)
    elif file_ext == '7z':
        import py7zr
        with py7zr.SevenZipFile(os.path.join(TEMP_DIR, archive), 'r') as zf:
            zf.extractall(path=TEMP_DIR)
    else:
        print(f"Unexpected file extension '{file_ext}' (expected zip, 7z)")
        return ""

    return os.path.join(TEMP_DIR, mission_filename)


if __name__ == '__main__':
    print('┌-------------------------------------┐')
    print('|     tS Mission Reviewer v2.0.0      |')
    print('└-------------------------------------┘')
    print()

    path = ''
    while not os.path.exists(path):
        path = input('Enter path to reviewed mission:')
        path = resolve_mission_path(path)

    op_result = Reviewer(path).review()

    save_temp = input("Press 'S' to save temp directory with all mission files.")
    if save_temp.lower() != 's' and (path.startswith(TEMP_DIR) and os.path.exists(TEMP_DIR)):
        shutil.rmtree(TEMP_DIR)

    sys.exit(op_result)

