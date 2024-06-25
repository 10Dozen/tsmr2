
from ..enums import PageStatus, PageTitle, RawContentLanguage, tSFModules
from ..data_entities import PageReviewHandler, PageData
from .tsf_reader import tSFModuleSQFReader
from .tsf_handler import tSFModuleHandler


class tSFArtilleryHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_ArtillerySupport
    MODULE = tSFModules.ArtillerySupport

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleSQFReader(self.MODULE, path)