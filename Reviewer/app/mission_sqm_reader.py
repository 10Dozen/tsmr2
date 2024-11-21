import os
import re
from time import strftime, localtime
from collections import namedtuple
import json
import armaclass

from .entities import DataReader


class MissionSqmReader(DataReader):
    '''Parses mission.sqm file and grabs useful data'''
    MISSION_FILE = 'mission.sqm'
    DESCRIPTION_EXT_FILE = 'description.ext'
    OVERVIEW_IMG_FILE = 'overview.jpg'
    SLOTS_TITLE = "Слоты"
    PLAYER_COUNT_IN_MISSION_NAME_PATTERN = re.compile(r'^([a-zA-Z]+)(\d+)')
    DESCRIPTION_EXT_FILE_DATA = {
        "overview": 'OVERVIEW('.lower(),
        "overview_text_pattern": re.compile(r'[\'"](.*)[\'"]', re.IGNORECASE)
    }

    class Metadata:
        def __init__(self):
            self.filename: str = ''
            self.title: str = ''
            self.author: str = ''
            self.overview: str = ''
            self.overview_picture: str = ''
            self.date: str = ''
            self.creation_date: str = ''
            self.player_count: int = 0
            self.extended_overview = []

    class PlayableUnit:
        def __init__(self, role: str, rank: str, classname: str):
            self.role = role
            self.rank = rank
            self.classname = classname

        def __repr__(self):
            return "PlayableUnit{role=%s, rank=%s, classname=%s}" % (
                self.role, self.rank, self.classname
            )

    class PlayableGroup:
        def __init__(self, name: str, side: str):
            self.name = name
            self.side = side
            self.units: list[MissionSqmReader.PlayableUnit] = []

        def addUnit(self, unit):
            self.units.append(unit)

        def __repr__(self):
            units = ", ".join(repr(x) for x in self.units)
            return "PlayableGroup{name=%s, side=%s, units=%s}" % (
                self.name, self.side, units
            )        

    def __init__(self, path):
        self.src = os.path.join(path, self.MISSION_FILE)
        self.desc_src = os.path.join(path, self.DESCRIPTION_EXT_FILE)
        self.overview_img_src = os.path.join(path, self.OVERVIEW_IMG_FILE)

        assert os.path.exists(self.src), self.src
        assert os.path.exists(self.desc_src), self.desc_src

        # Data 
        self.mission_file_content = None
        self.description_ext_content = None
        self.metadata = self.Metadata()
        self.slots: dict[str, list[MissionSqmReader.PlayableGroup]] = dict()

        self._read_files()
        sqm_data = armaclass.parse(self.mission_file_content)
        self.get_scenario_data(sqm_data)

        self.metadata.filename = os.path.basename(path)
        self.metadata.creation_date = strftime(
            '%Y-%m-%d %H:%M',
            localtime(os.path.getmtime(self.src))
        )
        self.metadata.extended_overview = self.get_description_ext_data()

        self.get_slots_info(sqm_data)

        print(f"{self.metadata.title}, {self.metadata.author}, {self.metadata.overview}")

    def _read_files(self):
        self.mission_file_content = DataReader._read_file(self.src)
        self.description_ext_content = DataReader._read_file_lines(self.desc_src)

    def get_scenario_data(self, sqm_data):
        '''Reads scenario data'''
        self.metadata.title = sqm_data["Mission"]["Intel"]["briefingName"]
        self.metadata.author = sqm_data["ScenarioData"]["author"]
        self.metadata.overview = sqm_data["ScenarioData"]["overviewText"]
        self.metadata.overview_picture = sqm_data["ScenarioData"]["overViewPicture"]

        # Date
        year = str(sqm_data["Mission"]["Intel"]["year"])
        month = str(sqm_data["Mission"]["Intel"]["month"])
        day = str(sqm_data["Mission"]["Intel"]["day"])
        if year:
            if not month or not day:
                self.metadata.date = f'{year}'
            else:
                if len(month) == 1:
                    month = f'0{month}'
                if len(day) == 1:
                    day = f'0{day}'
                self.metadata.date = f'{year}-{month}-{day}'

        # Player count
        match = self.PLAYER_COUNT_IN_MISSION_NAME_PATTERN.search(self.metadata.title)
        if match:
            self.metadata.player_count = int(match.group(2))

    def get_slots_info(self, sqm_data):
        '''Reads playable slots info'''
        group_entities_dict = None
        for v in sqm_data["Mission"]["Entities"].values():
            if (not isinstance(v, dict) or
                "name" not in v.keys() or 
                v["name"] != "Playable Units"):
                continue
            group_entities_dict = v["Entities"]
            break

        for v in group_entities_dict.values():
            # Search for groups
            if (not isinstance(v, dict) or 
                ("dataType" in v.keys() and v["dataType"] != "Group")):
                continue

            group_name = ""
            for attr in v["CustomAttributes"].values():
                if (not isinstance(attr, dict) or 
                    attr["property"] != "groupID"):
                    continue
                group_name = attr["Value"]["data"]["value"]
                break

            group = self.PlayableGroup(group_name, v["side"])               
            for unit in v["Entities"].values():
                if not isinstance(unit, dict):
                    continue
            
                group.addUnit(self.PlayableUnit(
                    role=unit["Attributes"]["description"],
                    rank=unit["Attributes"].get("rank", "PRIVATE"),
                    classname=unit["type"]
                ))
            
            per_side: list = self.slots.setdefault(v["side"], [])
            per_side.append(group)
   
    def get_description_ext_data(self):
        '''Reads data from description.ext'''
        overview_prefix = self.DESCRIPTION_EXT_FILE_DATA['overview']
        overview_lines = []
        for line in self.description_ext_content:
            check_line = line.lower().strip()
            if not check_line.startswith(overview_prefix):
                continue

            overview_line = self.DESCRIPTION_EXT_FILE_DATA['overview_text_pattern'].findall(line)
            if not overview_line:
                continue
                
            overview_lines.append(overview_line[0])

        return overview_lines

