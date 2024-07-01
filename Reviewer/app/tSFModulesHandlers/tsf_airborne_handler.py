
from ..enums import PageStatus, PageTitle, RawContentLanguage, Component
from ..entities import PageReviewHandler, PageData
from .tsf_module_reader import tSFModuleSQFReader
from .tsf_module_handler import tSFModuleHandler


class tSFAirborneHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_AirborneSupport
    COMPONENT = Component.AirborneSupport

    def __init__(self, path, mission_sqm=None, dzn_gear=None):
        super().__init__(path, mission_sqm, dzn_gear)
        self.reader = tSFModuleSQFReader(self.COMPONENT, path)
