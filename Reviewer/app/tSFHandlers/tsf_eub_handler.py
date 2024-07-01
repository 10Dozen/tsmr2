
from ..enums import PageStatus, PageTitle, RawContentLanguage, Component
from ..entities import PageReviewHandler, PageData
from .tsf_reader import tSFModuleSQFReader
from .tsf_handler import tSFModuleHandler


class tSFEUBHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_EditorUnitBehavior
    MODULE = Component.EditorUnitBehavior

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleSQFReader(self.MODULE, path)
