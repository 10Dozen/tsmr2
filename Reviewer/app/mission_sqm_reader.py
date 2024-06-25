from time import strftime, localtime

import os
import re


class MissionSqmReader:
    MISSION_FILE = 'mission.sqm'
    DESCRIPTION_EXT_FILE = 'description.ext'
    OVERVIEW_IMG_FILE = 'overview.jpg'

    MISSION_FILE_DATA = {
        "section": 'class ScenarioData'.lower(),
        "title": 'briefingName='.lower(),
        "overview": 'overviewText='.lower(),
        "overview_picture": 'overViewPicture='.lower(),
        "author": 'author='.lower(),
        "max_players": 'maxPlayers='.lower(),
        "year": 'year='.lower(),
        "month": 'month='.lower(),
        "day": 'day='.lower()
    }
    DESCRIPTION_EXT_FILE_DATA = {
        "overview": 'OVERVIEW('.lower()
    }

    def __init__(self, path):
        self.src = os.path.join(path, self.MISSION_FILE)
        self.desc_src = os.path.join(path, self.DESCRIPTION_EXT_FILE)
        self.overview_img_src = os.path.join(path, self.OVERVIEW_IMG_FILE)

        assert os.path.exists(self.src), self.src
        assert os.path.exists(self.desc_src), self.desc_src

        self.mission_filename = os.path.basename(path)
        with open(self.src, 'r', encoding='utf-8') as f:
            self.mission_file_content = f.readlines()
        
        self.title = None
        self.author = None
        self.overview = None
        self.overview_picture = None
        self.date = None
        self.player_count = None

        self.get_scenario_data()

        with open(self.desc_src, 'r', encoding='utf-8') as f:
            self.description_ext_content = f.readlines()
        self.description_data = self.get_description_ext_data()

        self.creation_date = strftime(
            '%Y-%m-%d %H:%M',
            localtime(os.path.getmtime(self.src))
        )

        print(f"{self.title} {self.author} {self.overview}")

    def get_scenario_data(self):
        '''Reads scenario data'''
        # player_count_mission_name = 0
        player_count_in_mission_name_pattern = re.compile(r'^([a-zA-Z]+)(\d+)')
        year = ''
        month = ''
        day = ''

        scenario_data_found = False
        for line in self.mission_file_content:
            line_to_test = line.strip().lower()

            # Skip until scenario data section met
            if not scenario_data_found:
                scenario_data_found = line_to_test == self.MISSION_FILE_DATA['section']
                continue

            if "=" not in line:
                continue

            line_value = line.rsplit("=", maxsplit=1)[1].strip().strip(';"')
            if line_to_test.startswith(self.MISSION_FILE_DATA['title']):
                self.title = line_value
                mission_name_regex = player_count_in_mission_name_pattern.search(line_value)
                if mission_name_regex:
                    self.player_count = int(mission_name_regex.group(2))
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['author']):
                self.author = line_value
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['overview_picture']):
                self.overview_picture = line_value
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['overview']):
                self.overview = line_value
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['year']):
                year = line_value
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['month']):
                month = line_value
                continue

            if line_to_test.startswith(self.MISSION_FILE_DATA['day']):
                day = line_value
                continue

        if year:
            if not month or not day:
                self.date = f'{year}'
            else:
                if len(month) == 1:
                    month = f'0{month}'
                if len(day) == 1:
                    day = f'0{day}'
                self.date = f'{year}-{month}-{day}'
   
    def get_description_ext_data(self):
        overview_prefix = self.DESCRIPTION_EXT_FILE_DATA['overview']
        prefix_offset = len(overview_prefix)

        overview_lines = []
        for line in self.description_ext_content:
            check_line = line.lower().strip()
            if not check_line.startswith(overview_prefix):
                continue

            overview_lines.append(
                line.strip()[prefix_offset:-2]
                    .split(",",maxsplit=1)[1]
                    .strip(' "')
            )

        return overview_lines

