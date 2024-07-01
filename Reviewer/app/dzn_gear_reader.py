from .entities import DataReader
import os


class dznGearReader(DataReader):
    SUBDIR = 'dzn_gear'
    INIT_FILE = 'dzn_gear_init.sqf'
    SETTINGS_FILE = 'Settings.sqf'
    KITS_FILE = 'Kits.sqf'
    GAT_FILE = 'GearAssignementTable.sqf'

    KIT_DATA_PATTERN = "kit_"
    CARGO_KIT_DATA_PATTERN = "cargo_kit_"

    def __init__(self, path):
        self.init_file_src = os.path.join(path, self.SUBDIR, self.INIT_FILE)
        self.settings_src = os.path.join(path, self.SUBDIR, self.SETTINGS_FILE)
        self.kits_src = os.path.join(path, self.SUBDIR, self.KITS_FILE)
        self.gat_src = os.path.join(path, self.SUBDIR, self.GAT_FILE)

        assert os.path.exists(self.init_file_src), self.init_file_src
        assert os.path.exists(self.settings_src), self.settings_src
        assert os.path.exists(self.kits_src), self.kits_src
        assert os.path.exists(self.gat_src), self.gat_src

        self.version = 'Неизвестно'
        self.settings_content = None 
        self.kits_content = None 
        self.gat_content = None

        self.kits = []
        self.cargo_kits = []

        self._read_version()
        self._read_files()
        self._get_kits()

    def _read_version(self):
        with open(self.init_file_src, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith('dzn_gear_version ='):
                    self.version = line.split('=')[1].strip()[1:-2]
                    break

    def _read_files(self):
        with open(self.settings_src, 'r', encoding='utf-8') as f:
            self.settings_content = f.readlines()
        
        with open(self.kits_src, 'r', encoding='utf-8') as f:
            self.kits_content = f.readlines()

        with open(self.gat_src, 'r', encoding='utf-8') as f:
            self.gat_content = f.readlines()

    def _get_kits(self):
        for line in self.kits_content:
            trimmed_line =  line.strip().lower()
            if trimmed_line.startswith(self.KIT_DATA_PATTERN):
                self.kits.append(line.split('=')[0].strip())

            if trimmed_line.startswith(self.CARGO_KIT_DATA_PATTERN):
                self.cargo_kits.append(line.split('=')[0].strip())
    