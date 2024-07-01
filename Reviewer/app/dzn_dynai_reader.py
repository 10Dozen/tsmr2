from .entities import DataReader
import os


class dznDynaiReader(DataReader):
    SUBDIR = 'dzn_dynai'
    INIT_FILE = 'dzn_dynai_init.sqf'
    SETTINGS_FILE = 'Settings.sqf'
    ZONES_FILE = 'Zones.sqf'

    ZONE_NAME_STR = '/* Zone Name */'.lower()


    def __init__(self, path):
        self.init_file_src = os.path.join(path, self.SUBDIR, self.INIT_FILE)
        self.settings_src = os.path.join(path, self.SUBDIR, self.SETTINGS_FILE)
        self.zones_src = os.path.join(path, self.SUBDIR, self.ZONES_FILE)

        assert os.path.exists(self.init_file_src), self.init_file_src
        assert os.path.exists(self.settings_src), self.settings_src
        assert os.path.exists(self.zones_src), self.kits_src

        self.version = 'Неизвестно'
        self.settings_content = None 
        self.zones_content = None 

        self.zones = []

        self._read_version()
        self._read_files()
        self._get_zones()

    def _read_version(self):
        with open(self.init_file_src, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith('dzn_dynai_version ='):
                    self.version = line.split('=')[1].strip()[1:-2]
                    break

    def _read_files(self):
        with open(self.settings_src, 'r', encoding='utf-8') as f:
            self.settings_content = f.readlines()
        
        with open(self.zones_src, 'r', encoding='utf-8') as f:
            self.zones_content = f.readlines()

    def _get_zones(self):
        for line in self.zones_content:
            trimmed_line = line.strip().lower()
            if trimmed_line.endswith(self.ZONE_NAME_STR):
                self.zones.append([ line.split("/*")[0].strip()[1:-1] ])
            
            if trimmed_line.endswith('/* Side, is Active */ [],[]'.lower()):
                side, is_active = [
                    e.strip().strip('"')
                    for e in line.split("/*")[0].strip().strip(",").split(",")
                ]
                (self.zones[-1]).append(side)
                (self.zones[-1]).append(is_active)


    