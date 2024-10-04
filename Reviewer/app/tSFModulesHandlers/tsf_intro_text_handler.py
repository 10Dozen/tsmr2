
from ..enums import PageTitle, Component
from ..entities import PageData
from .tsf_module_reader import tSFModuleReader
from .tsf_module_handler import tSFModuleHandler


class tSFIntroTextHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_IntroText
    COMPONENT = Component.IntroText
    VALIDATOR = ""

    def __init__(self, path, mission_sqm=None):
        super().__init__(path, mission_sqm)
        self.reader = tSFModuleReader(self.COMPONENT, path)

    def get_page_data(self):
        page_data: PageData = super().get_page_data()
        
        page_data.add_info(
            "Дата", 
            "<дата из редактора - %1/%2/%3>" 
            if self.reader.settings_yaml.get("Date") == '%1/%2/%3' else 
            self.reader.settings_yaml.get("Date")
        )
        page_data.add_info("Локация", self.reader.settings_yaml.get("Location"))
        page_data.add_info("Операция", self.reader.settings_yaml.get("Operation"))

        return page_data