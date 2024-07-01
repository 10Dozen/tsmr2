
from ..enums import PageStatus, PageTitle, RawContentLanguage, Component
from ..entities import  PageData
from .tsf_reader import tSFModuleSQFReader
from .tsf_handler import tSFModuleHandler


class tSFFARPHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF_FARP
    MODULE = Component.FARP

    SQM_PATTERN = 'name="tSF_FARP";'.lower()
    SQM_COMPOSITION = 'init="tSF_FARP_Composition = ""'.lower()

    def __init__(self, path, mission_sqm=None):
        super().__init__(path, mission_sqm)
        self.reader = tSFModuleSQFReader(self.MODULE, path)

        self.module_set = False 
        self.composition_name = 'Не указана / Отсутствует'
        self.look_for_ccp_data()

    def look_for_ccp_data(self):
        for line in self.mission_sqm.mission_file_content:
            line_trimmed = line.strip().lower()
            if line_trimmed == self.SQM_PATTERN:
                self.module_set = True
            elif line_trimmed.startswith(self.SQM_COMPOSITION):
                self.composition_name = line.strip()[len(self.SQM_COMPOSITION):-4]
                break


    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("FARP установлен", 'Да' if self.module_set else 'Нет')
        page_data.add_info("Композиция", self.composition_name)

        return page_data