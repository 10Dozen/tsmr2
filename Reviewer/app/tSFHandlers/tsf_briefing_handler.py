
from .tsf_reader import tSFModuleReader
from .tsf_handler import tSFModuleHandler
from ..enums import PageTitle, PageStatus, InfoType, RawContentLanguage, Component
from ..entities import PageData, PageReviewHandler

import os

class tSFBriefingReader(tSFModuleReader):
    BRIEFING_FILE = 'tSF_briefing.sqf'
    BRIEFING_FILE_DATA = {
        "tags": 'TAGS',
        "topic_start": "TOPIC",
        "topic_end": "END"
    }

    def __init__(self, path):
        super().__init__(Component.Briefing, path)

        raw_briefing_content, briefing_text, tags = self._parse_briefing_file()
        self.briefing_content = raw_briefing_content
        self.briefing = briefing_text
        self.tags = tags

    def _parse_briefing_file(self):
        briefing_content = []
        with open(
            os.path.join(self.path, self.BRIEFING_FILE),
            'r', encoding='utf-8'
        ) as f:
            briefing_content = f.readlines()

        tags = []
        briefing_lines = []
        topic_started = False
        for line in briefing_content:
            if line.startswith(self.BRIEFING_FILE_DATA['tags']):
                raw_tags = (
                    line[len(self.BRIEFING_FILE_DATA['tags']):]
                    .strip(";()[]\n")
                    .split(",")
                )
                for tag in raw_tags:
                    tag = tag.strip('"')
                    if not tag:
                        continue
                    tags.append(tag.strip('"'))

                # Clear duplicates
                tags = list(set(tags))
                continue

            if line.startswith(self.BRIEFING_FILE_DATA['topic_start']):
                topic_name = (
                    line[len(self.BRIEFING_FILE_DATA['topic_start']):]
                    .strip('(")\n')
                )
                topic_started = True
                briefing_lines.append(f'<h4>{topic_name}</h4>')
                continue

            if line.startswith(self.BRIEFING_FILE_DATA['topic_end']):
                topic_started = False
                continue

            if topic_started:
                line = line.strip().replace('""', "'").strip('"')
                briefing_lines.append(line)

        return briefing_content, ''.join(briefing_lines), tags



class tSFBriefingHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_Briefing
    MODULE = Component.Briefing

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader: tSFBriefingReader = tSFBriefingReader(path)

    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("Тэги", self.reader.tags, InfoType.MISSION_TAGS)
        page_data.add_info("Брифинг", self.reader.briefing)

        page_data.add_raw_content(
            self.reader.BRIEFING_FILE,
            ''.join(self.reader.briefing_content),
            RawContentLanguage.CPP
        )

        return page_data