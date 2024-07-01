 
from ..enums import PageStatus, PageTitle, RawContentLanguage, Component
from ..entities import PageReviewHandler, PageData
from .tsf_module_reader import tSFModuleSQFReader
from .tsf_module_handler import tSFModuleHandler


class tSFInteractivesHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_Interactives
    COMPONENT = Component.Interactives

    def __init__(self, path, mission_sqm=None):
        super().__init__(path, mission_sqm)
        self.reader = tSFModuleSQFReader(self.COMPONENT, path)
