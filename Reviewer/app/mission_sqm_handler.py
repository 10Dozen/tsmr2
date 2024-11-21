import yaml 
from .enums import PageTitle, RawContentLanguage, InfoType, Component
from .mission_sqm_reader import MissionSqmReader
from .entities import PageData, PageReviewHandler


class MissionSqmHandler(PageReviewHandler):
    TITLE = PageTitle.Mission
    COMPONENT = Component.Mission
    SQM_MAX_LINES = 1000

    def __init__(self, path):
        self.reader: MissionSqmReader = MissionSqmReader(path)

        self.mission_filename = self.reader.metadata.filename
        self.creation_date = self.reader.metadata.creation_date
        self.overview_img_src = self.reader.overview_img_src


    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("Название", self.reader.metadata.title)
        page_data.add_info("Автор", self.reader.metadata.author)
        page_data.add_info("Описание", self.reader.metadata.overview)
        page_data.add_info("Дата", self.reader.metadata.date)
        page_data.add_info("Кол-во игроков", self.reader.metadata.player_count)
        page_data.add_info("Превью", self.reader.metadata.overview_picture)
        page_data.add_info(
            "Description.ext / OVERVIEW", 
            self.reader.metadata.extended_overview, 
            InfoType.MULTILINE
        )

        mission_sqm_lines_omitted = len(self.reader.mission_file_content) - self.SQM_MAX_LINES
        mission_sqm_content = ''.join(
            self.reader.mission_file_content[0:self.SQM_MAX_LINES]
        ).replace('\t', '  ') + f'\n...оставшиеся {mission_sqm_lines_omitted} строк опущены'


        slots = dict()
        for k, groups in self.reader.slots.items():
            slots[k] = {}
            for group in groups:
                slots[k].setdefault(group.name, [])
                for unit in group.units:
                    line = "%-50s (%-12s / %s)" % (unit.role, unit.rank, unit.classname)
                    slots[k][group.name].append(line)


        page_data.add_raw_content(
            self.reader.SLOTS_TITLE,
            yaml.dump(slots, indent=4, sort_keys=False, allow_unicode=True),
            RawContentLanguage.YAML
        )
        page_data.add_raw_content(
            self.reader.OVERVIEW_IMG_FILE,
            self.reader.OVERVIEW_IMG_FILE,
            RawContentLanguage.IMAGE
        )
        page_data.add_raw_content(
            filename=self.reader.DESCRIPTION_EXT_FILE, 
            content=''.join(self.reader.description_ext_content).replace('\t', '  '),
            language=RawContentLanguage.CPP
        )
        page_data.add_raw_content(
            filename=self.reader.MISSION_FILE, 
            content=mission_sqm_content,
            language=RawContentLanguage.CPP
        )

        return page_data

