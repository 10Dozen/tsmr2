from ..enums import PageTitle,  Component
from .tsf_module_reader import tSFModuleReader
from .tsf_module_handler import tSFModuleHandler


class tSFCrewOptionsHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_CrewOptions
    COMPONENT = Component.CrewOptions

    def __init__(self, path, mission_sqm=None):
        super().__init__(path, mission_sqm)
        self.reader = tSFModuleReader(self.COMPONENT, path)