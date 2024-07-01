from .enums import PageTitle, Component, RawContentLanguage, InfoType
from .dzn_gear_reader import dznGearReader
from .entities import PageData, PageReviewHandler


class dznGearHandler(PageReviewHandler):
    TITLE = PageTitle.dzn_gear
    COMPONENT = Component.dznGear
    
    def __init__(self, path):
        self.reader = dznGearReader(path)

    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("Версия", self.reader.version)     
        page_data.add_info("Кол-во китов", f"{len(self.reader.kits)} персональных, {len(self.reader.cargo_kits)} грузовых")        
        page_data.add_info("Персональные киты", self.reader.kits, InfoType.MULTILINE)
        page_data.add_info("Грузовые киты", self.reader.cargo_kits, InfoType.MULTILINE)

        page_data.add_raw_content(
            self.reader.GAT_FILE,
            ''.join(self.reader.gat_content),
            RawContentLanguage.CPP
        )
        page_data.add_raw_content(
            self.reader.KITS_FILE,
            ''.join(self.reader.kits_content),
            RawContentLanguage.CPP
        )
        page_data.add_raw_content(
            self.reader.SETTINGS_FILE,
            ''.join(self.reader.settings_content),
            RawContentLanguage.CPP
        )

        return page_data

