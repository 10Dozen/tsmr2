from .enums import PageTitle, PageStatus, RawContentLanguage, InfoType
from .dzn_dynai_reader import dznDynaiReader
from .data_entities import PageData, PageReviewHandler


class dznDynaiHandler(PageReviewHandler):
    TITLE = PageTitle.dzn_dynai

    def __init__(self, path):
        self.reader = dznDynaiReader(path)

    def get_page_data(self):
        page_data: PageData = super().get_page_data()

        page_data.add_info("Версия", self.reader.version)
        
        zones_per_side = {}
        sides = set([z[1] for z in self.reader.zones])
        for side in sides:
            zones_per_side[side] = len([z for z in self.reader.zones if z[1] == side])
        active_zones = len([z for z in self.reader.zones if z[2]])

        page_data.add_info(
            "Кол-во зон", 
            f"{len(self.reader.zones)}, из которых активных {active_zones}, по сторонам {zones_per_side}" 
        )        
        page_data.add_info(
            "Зоны", self.reader.zones, 
            InfoType.DYNAI_ZONES
        )

        page_data.add_raw_content(
            self.reader.ZONES_FILE,
            ''.join(self.reader.zones_content),
            RawContentLanguage.CPP
        )
        page_data.add_raw_content(
            self.reader.SETTINGS_FILE,
            ''.join(self.reader.settings_content),
            RawContentLanguage.CPP
        )

        return page_data

