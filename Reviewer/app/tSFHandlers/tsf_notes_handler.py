
from ..enums import PageStatus, PageTitle, RawContentLanguage, tSFModules
from ..data_entities import PageReviewHandler, PageData
from .tsf_reader import tSFModuleReader
from .tsf_handler import tSFModuleHandler


class tSFNotesHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_tSNotes
    MODULE = tSFModules.tSNotes

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleReader(self.MODULE, path)
