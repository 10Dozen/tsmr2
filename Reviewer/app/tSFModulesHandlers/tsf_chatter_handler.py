
from ..enums import PageTitle, Component
from .tsf_module_reader import tSFModuleReader
from .tsf_module_handler import tSFModuleHandler


class tSFChatterHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_Chatter
    COMPONENT = Component.Chatter

    def __init__(self, path, mission_sqm=None):
        super().__init__(path, mission_sqm)
        self.reader = tSFModuleReader(self.COMPONENT, path)
