from enum import StrEnum, auto


class tSFModules(StrEnum):
    Briefing = 'Briefing'
    IntroText = 'IntroText'
    MissionConditions = 'MissionConditions'
    CCP = 'CCP'
    FARP = 'FARP'
    Authorization = 'Authorization'
    AirborneSupport = 'AirborneSupport'
    ArtillerySupport = 'ArtillerySupport'
    EditorRadioSettings = 'EditorRadioSettings'
    EditorUnitBehavior = 'EditorUnitBehavior'
    EditorVehicleCrew = 'EditorVehicleCrew'
    tSNotes = 'tSNotes'
    tSSettings = 'tSSettings'
    MissionDefaults = 'MissionDefaults'
    JIPTeleport = 'JIPTeleport'
    ACEActions = 'ACEActions'
    Interactives = 'Interactives'
    Conversations = 'Conversations'
    Chatter = 'Chatter'
    POM = 'POM'
    tSAdminTools = 'tSAdminTools'

    def __repr__(self):
        return self.value


class PageTitle(StrEnum):
    Mission = "Миссия"
    dzn_gear = "dzn_Gear"
    dzn_dynai = "dzn_Dynai"
    tSF_Briefing = f"tSF / {tSFModules.Briefing}"
    tSF_IntroText = f"tSF / {tSFModules.IntroText}"
    tSF_MissionConditions = f"tSF / {tSFModules.MissionConditions}"
    tSF_CCP = f"tSF / {tSFModules.CCP}"
    tSF_FARP = f"tSF / {tSFModules.FARP}"
    tSF_Authorization = f"tSF / {tSFModules.Authorization}"
    tSF_AirborneSupport = f"tSF / {tSFModules.AirborneSupport}"
    tSF_ArtillerySupport = f"tSF / {tSFModules.ArtillerySupport}"
    tSF_EditorRadioSettings = f"tSF / {tSFModules.EditorRadioSettings}"
    tSF_EditorUnitBehavior = f"tSF / {tSFModules.EditorUnitBehavior}"
    tSF_EditorVehicleCrew = f"tSF / {tSFModules.EditorVehicleCrew}"
    tSF_tSNotes = f"tSF / {tSFModules.tSNotes}"
    tSF_tSSettings = f"tSF / {tSFModules.tSSettings}"
    tSF_MissionDefaults = f"tSF / {tSFModules.MissionDefaults}"
    tSF_JIPTeleport = f"tSF / {tSFModules.JIPTeleport}"
    tSF_ACEActions = f"tSF / {tSFModules.ACEActions}"
    tSF_Interactives = f"tSF / {tSFModules.Interactives}"
    tSF_Conversations = f"tSF / {tSFModules.Conversations}"
    tSF_Chatter = f"tSF / {tSFModules.Chatter}"
    tSF_POM = f"tSF / {tSFModules.POM}"
    tSF_tSAdminTools = f"tSF / {tSFModules.tSAdminTools}"

    def __repr__(self):
        return f'"{self.value}"'


class PageStatus(StrEnum):
    OK = auto()
    DISABLED = auto()
    ERROR = auto()
    WARNING = auto()

    def __repr__(self):
        return f'"{self.value.upper()}"'


class InfoType(StrEnum):
    PLAIN = 'plain'
    MULTILINE = 'multiline'
    MISSION_TAGS = 'missionTags'

    def __repr__(self):
        return f'"{self.value}"'


class RawContentLanguage(StrEnum):    
    IMAGE = 'image'
    CPP = 'cpp'
    YAML = 'yaml'

    def __repr__(self):
        return f'"{self.value}"'