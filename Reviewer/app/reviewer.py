from .mission_sqm_reader import MissionSqmReader
from .tsf_reader import tSFrameworkSettingsReader, tSFBriefingReader, \
  tSFIntroTextReader
from .report_generator import ReportGenerator

import os
import sys
from enum import Enum, StrEnum, auto


class PageTitle(StrEnum):
    Mission = "Миссия"
    tSF_Briefing = "tSF / Briefing"
    tSF_IntroText = "tSF / IntroText"

    def __repr__(self):
        return f'"{self.value}"'


class PageStatus(StrEnum):
    OK = auto()
    DISABLED = auto()
    ERROR = auto()
    WARNING = auto()

    def __repr__(self):
        return f'"{self.value.upper()}"'


class Reviewer:
    def __init__(self, path):
        self.path = path
        self.mission_sqm = None
        self.tsf_settings = None
        self.tsf_briefing = None
        self.tsf_intro_text = None
        self.reporter = None

    def review(self):
        print('Review initiated')
        self.mission_sqm = MissionSqmReader(self.path)
        self.tsf_settings = tSFrameworkSettingsReader(self.path, True)
        self.tsf_briefing = tSFBriefingReader(
            self.path,
            self.tsf_settings.get_module_state(tSFBriefingReader.MODULE)
        )
        self.tsf_intro_text = tSFIntroTextReader(
            self.path,
            self.tsf_settings.get_module_state(tSFIntroTextReader.MODULE)
        )

        self.generate_report()

    def generate_report(self):
        """Creates report from the read data"""
        report_data = self.prepare_report_data()

        self.reporter = ReportGenerator(
            mission_name=self.mission_sqm.mission_filename,
            mission_creation_date=self.mission_sqm.creation_date
        )
        self.reporter.create_report(
            report_content=report_data,
            overview_img_path=self.mission_sqm.overview_img_src
        )

    def prepare_report_data(self):
        """Formats report data file"""
        data = {
            "filename": self.mission_sqm.mission_filename,
            "creationData": self.mission_sqm.creation_date,
            "pages": []
        }

        # Mission file page
        max_lines = 1000
        mission_sqm_lines_omitted = len(self.mission_sqm.mission_file_content) - max_lines
        mission_sqm_content = ''.join(
            self.mission_sqm.mission_file_content[0:max_lines]
        ).replace('\t', '  ')

        data['pages'].append({
            "name": PageTitle.Mission,
            "status": PageStatus.OK,
            "info": [
                {
                    "name": "Название",
                    "value": self.mission_sqm.scenario_data['title']
                },
                {
                    "name": "Автор",
                    "value": self.mission_sqm.scenario_data['author']
                },
                {
                    "name": "Описание",
                    "value": self.mission_sqm.scenario_data['overview']
                },
                {
                    "name": "Дата",
                    "value": self.mission_sqm.scenario_data['date']
                },
                {
                    "name": "Кол-во игроков",
                    "value": self.mission_sqm.scenario_data['player_count']
                },
                {
                    "name": "Превью",
                    "value": self.mission_sqm.scenario_data['overview_picture']
                },
                {
                    "name": "Description.ext / OVERVIEW",
                    "value": self.mission_sqm.description_data
                }
            ],
            "validation": [],
            "issues": [],
            "rawContent": [
                {
                    "filename": self.mission_sqm.OVERVIEW_IMG_FILE,
                    "content": self.mission_sqm.OVERVIEW_IMG_FILE,
                    "language": "image"
                },
                {
                    "filename": self.mission_sqm.DESCRIPTION_EXT_FILE,
                    "content": (
                        ''.join(self.mission_sqm.description_ext_content)
                          .replace('\t', '  ')
                    ),
                    "language": "cpp"
                },
                {
                    "filename": self.mission_sqm.MISSION_FILE,
                    "content": (
                        mission_sqm_content +
                        f'\n...оставшиеся {mission_sqm_lines_omitted} строк опущены'
                    ),
                    "language": "cpp"
                }
            ]
        })

        # tSF Briefing
        data['pages'].append({
            "name": PageTitle.tSF_Briefing,
            "status": PageStatus.OK,
            "info": [
                {
                    "name": "Теги",
                    "value": self.tsf_briefing.tags,
                    "type": "missionTags"
                },
                {
                    "name": "Брифинг",
                    "value": self.tsf_briefing.briefing
                }
            ],
            "validation": [],
            "issues": [],
            "rawContent": [
                {
                    "filename": self.tsf_briefing.BRIEFING_FILE,
                    "content": ''.join(self.tsf_briefing.briefing_content),
                    "language": "cpp"
                },
                {
                    "filename": self.tsf_briefing.SETTINGS_FILE,
                    "content": ''.join(self.tsf_briefing.settings),
                    "language": "yaml"
                }
            ]
        })

        # tSF IntroText
        data['pages'].append({
            "name": PageTitle.tSF_IntroText,
            "status": PageStatus.OK,
            "info": [
                {
                    "name": "Дата",
                    "value": self.tsf_intro_text.settings_yaml['Date']
                },
                {
                    "name": "Локация",
                    "value": self.tsf_intro_text.settings_yaml['Location']
                },
                {
                    "name": "Операция",
                    "value": self.tsf_intro_text.settings_yaml['Operation']
                },
            ],
            "validation": [],
            "issues": [],
            "rawContent": [
                {
                    "filename": self.tsf_intro_text.SETTINGS_FILE,
                    "content": ''.join(self.tsf_intro_text.settings),
                    "language": "yaml"
                }
            ]
        })

        return data

