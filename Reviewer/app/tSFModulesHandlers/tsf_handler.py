from ..enums import Component, PageTitle
from ..mission_sqm_reader import MissionSqmReader
from ..entities import PageData, PageReviewHandler, DataReader
from .tsf_module_reader import tSFModuleReader
from .tsf_module_handler import tSFModuleHandler
import os


class tSFrameworkSettingsReader(tSFModuleReader):
    COMPONENTS_DIR = ''

    VERSION_FILE_SUBDIR = 'Modules'
    VERSION_FILE = 'script_macro.hpp'
    VERSION_PATTERN = "#define TSF_VERSION_NUMBER "

    def __init__(self, path):
        super().__init__(None, path)
        self.version_src = os.path.join(
            path, 
            self.FRAMEWORK_DIR, self.VERSION_FILE_SUBDIR, 
            self.VERSION_FILE
        )
        self.version = "Неизвестно"

        self._read_version()

    def _read_version(self):
        with open(self.version_src, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith(self.VERSION_PATTERN):                    
                    self.version = line.rsplit(' ')[-1].strip()[1:-1]
                    print(self.version)
                    break

    

class tSFrameworkSettingsHandler(tSFModuleHandler):
    TITLE = PageTitle.tSF
    COMPONENT = Component.tSF

    def __init__(self, path, mission_sqm: MissionSqmReader = None):
        super().__init__(path, mission_sqm)
        self.reader = tSFrameworkSettingsReader(path)
    
    def is_module_active(self, module_name):
        return self.reader.settings_yaml.get(module_name)
    
    def get_page_data(self):
        page_data = super().get_page_data()

        page_data.add_info(
            "Версия",
            self.reader.version
        )

        return page_data