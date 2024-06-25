
from ..enums import PageStatus, PageTitle, RawContentLanguage, tSFModules
from ..data_entities import PageReviewHandler, PageData
from .tsf_reader import tSFModuleReader
from .tsf_handler import tSFModuleHandler


class tSFIntroTextHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_IntroText
    MODULE = tSFModules.IntroText
    VALIDATOR = ""

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleReader(self.MODULE, path)

    def get_page_data(self):
        page_data: PageData = super().get_page_data()
        
        page_data.add_info("Дата", self.reader.settings_yaml.get("Date"))
        page_data.add_info("Локация", self.reader.settings_yaml.get("Location"))
        page_data.add_info("Операция", self.reader.settings_yaml.get("Operation"))

        return page_data