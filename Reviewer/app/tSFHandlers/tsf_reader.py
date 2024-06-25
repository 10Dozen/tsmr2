
import os
import yaml
# from yaml import parser, safe_load


class tSFModuleReader:
    FRAMEWORK_DIR = 'dzn_tSFramework'
    MODULES_DIR = 'Modules'
    MODULE = ''
    SETTINGS_FILE = 'Settings.yaml'

    def __init__(self, module, path):
        self.module = module if module else ''
        self.path = os.path.join(path, self.FRAMEWORK_DIR,
                                 self.MODULES_DIR, self.module)
        self.settings = None
        self.settings_yaml = None
        self._read_settings()

    def _get_settings_file(self):
        return os.path.join(self.path, self.SETTINGS_FILE)

    def _read_settings(self):
        settings_file = self._get_settings_file()

        with open(settings_file, 'r', encoding='utf-8') as f:
            self.settings = f.readlines()

        with open(settings_file, 'r', encoding='utf-8') as f:
            try:
                self.settings_yaml = yaml.safe_load(f)
            except yaml.parser.ParserError:
                print(f"[Reader-{self.module}]Failed to parse SFML (not a YAML-compatible syntax)")


class tSFModuleSQFReader(tSFModuleReader):
    SETTINGS_FILE = 'Settings.sqf'

    def _read_settings(self):
        settings_file = self._get_settings_file()

        with open(settings_file, 'r', encoding='utf-8') as f:
            self.settings = f.readlines()


class tSFrameworkSettingsReader(tSFModuleReader):
    MODULES_DIR = ''
    def __init__(self, path):
        super().__init__(None, path)

    def is_module_active(self, module_name):
        return self.settings_yaml.get(module_name)
