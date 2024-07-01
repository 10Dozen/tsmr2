from ..entities import PageReviewHandler
from ..mission_sqm_reader import MissionSqmReader
from ..enums import RawContentLanguage, Component
from .tsf_module_reader import tSFModuleReader

class tSFModuleHandler(PageReviewHandler):
    COMPONENT = Component.tSF

    def __init__(self, path, mission_sqm: MissionSqmReader = None):
        self.mission_sqm = mission_sqm
        self.path = path
    
    def get_page_data(self):
        page_data = super().get_page_data()

        lang = (
            RawContentLanguage.YAML 
            if self.reader.SETTINGS_FILE == tSFModuleReader.SETTINGS_FILE else 
            RawContentLanguage.SQF
        )

        page_data.add_raw_content(
            self.reader.SETTINGS_FILE,
            ''.join(self.reader.settings),
            lang
        )

        return page_data