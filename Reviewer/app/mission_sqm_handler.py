from .enums import PageTitle, PageStatus, RawContentLanguage
from .mission_sqm_reader import MissionSqmReader
from .data_entities import PageData, PageReviewHandler


class MissionSqmHandler(PageReviewHandler):
    TITLE = PageTitle.Mission
    SQM_MAX_LINES = 1000

    def __init__(self, path):
        self.reader = MissionSqmReader(path)

        self.mission_filename = self.reader.mission_filename
        self.creation_date = self.reader.creation_date
        self.overview_img_src = self.reader.overview_img_src

    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("Название", self.reader.title)
        page_data.add_info("Автор", self.reader.author)
        page_data.add_info("Описание", self.reader.overview)
        page_data.add_info("Дата", self.reader.date)
        page_data.add_info("Кол-во игроков", self.reader.player_count)
        page_data.add_info("Превью", self.reader.overview_picture)
        page_data.add_info("Description.ext / OVERVIEW", self.reader.description_data)

        mission_sqm_lines_omitted = len(self.reader.mission_file_content) - self.SQM_MAX_LINES
        mission_sqm_content = ''.join(
            self.reader.mission_file_content[0:self.SQM_MAX_LINES]
        ).replace('\t', '  ') + f'\n...оставшиеся {mission_sqm_lines_omitted} строк опущены'

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

