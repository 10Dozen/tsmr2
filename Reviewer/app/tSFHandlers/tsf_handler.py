from ..entities import PageReviewHandler
from ..mission_sqm_reader import MissionSqmReader
from ..enums import RawContentLanguage
from .tsf_reader import tSFModuleReader

class tSFModuleHandler(PageReviewHandler):
    MODULE = ""

    def __init__(self, path, mission_sqm: MissionSqmReader = None, dzn_gear=None):
        self.mission_sqm = mission_sqm
        self.gear = dzn_gear
        self.path = path
    
    def get_page_data(self):
        page_data = super().get_page_data()

        lang = (
            RawContentLanguage.YAML 
            if self.reader.SETTINGS_FILE == tSFModuleReader.SETTINGS_FILE else 
            RawContentLanguage.CPP
        )

        page_data.add_raw_content(
            self.reader.SETTINGS_FILE,
            ''.join(self.reader.settings),
            lang
        )

        return page_data