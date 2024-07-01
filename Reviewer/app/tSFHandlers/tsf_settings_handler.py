
from ..enums import PageStatus, PageTitle, RawContentLanguage, Component
from ..entities import PageReviewHandler, PageData
from .tsf_reader import tSFModuleReader
from .tsf_handler import tSFModuleHandler


class tSFSettingsHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_tSSettings
    MODULE = Component.tSSettings

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleReader(self.MODULE, path)
