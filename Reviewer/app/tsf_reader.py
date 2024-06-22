
import os
import yaml


class tSFModuleReader:
    FRAMEWORK_DIR = 'dzn_tSFramework'
    MODULES_DIR = 'Modules'
    MODULE = ''
    SETTINGS_FILE = 'Settings.yaml'

    def __init__(self, path):
        self.path = os.path.join(path, self.FRAMEWORK_DIR,
                                 self.MODULES_DIR, self.MODULE)
        self.settings = None
        self.settings_yaml = None
        self._read_settings()

    def _get_settings_file(self):
        return os.path.join(self.path, self.SETTINGS_FILE)

    def _read_settings(self):
        settings_file = self._get_settings_file()

        with open(settings_file, 'r', encoding='utf-8') as f:
            self.settings = f.readlines()

        with open(settings_file, 'r', encoding='utf-8') as f:
            self.settings_yaml = yaml.safe_load(f)


class tSF_Briefing_Reader(tSFModuleReader):
    MODULE = 'Briefing'
    BRIEFING_FILE = 'tSF_briefing.sqf'
    BRIEFING_FILE_DATA = {
        "tags": 'TAGS',
        "topic_start": "TOPIC",
        "topic_end": "END"
    }

    def __init__(self, path):
        super().__init__(path)

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


