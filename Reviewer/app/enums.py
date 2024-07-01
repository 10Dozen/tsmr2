from enum import StrEnum, auto


class Component(StrEnum):
    Mission = auto()
    dznGear = auto()
    dznDynai = auto()
    tSF = auto()

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

    tSF_Briefing = f"tSF / {Component.Briefing}"
    tSF_IntroText = f"tSF / {Component.IntroText}"
    tSF_MissionConditions = f"tSF / {Component.MissionConditions}"
    tSF_CCP = f"tSF / {Component.CCP}"
    tSF_FARP = f"tSF / {Component.FARP}"
    tSF_Authorization = f"tSF / {Component.Authorization}"
    tSF_AirborneSupport = f"tSF / {Component.AirborneSupport}"
    tSF_ArtillerySupport = f"tSF / {Component.ArtillerySupport}"
    tSF_EditorRadioSettings = f"tSF / {Component.EditorRadioSettings}"
    tSF_EditorUnitBehavior = f"tSF / {Component.EditorUnitBehavior}"
    tSF_EditorVehicleCrew = f"tSF / {Component.EditorVehicleCrew}"
    tSF_tSNotes = f"tSF / {Component.tSNotes}"
    tSF_tSSettings = f"tSF / {Component.tSSettings}"
    tSF_MissionDefaults = f"tSF / {Component.MissionDefaults}"
    tSF_JIPTeleport = f"tSF / {Component.JIPTeleport}"
    tSF_ACEActions = f"tSF / {Component.ACEActions}"
    tSF_Interactives = f"tSF / {Component.Interactives}"
    tSF_Conversations = f"tSF / {Component.Conversations}"
    tSF_Chatter = f"tSF / {Component.Chatter}"
    tSF_POM = f"tSF / {Component.POM}"
    tSF_tSAdminTools = f"tSF / {Component.tSAdminTools}"

    Tests = "Проверки"

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
    DYNAI_ZONES = 'dynaiZones'

    def __repr__(self):
        return f'"{self.value}"'


class RawContentLanguage(StrEnum):    
    IMAGE = 'image'
    CPP = 'cpp'
    YAML = 'yaml'

    def __repr__(self):
        return f'"{self.value}"'
    

class Severity(StrEnum):
    ERROR = auto()
    WARNING = auto()
    NOTICE = auto()

    def __repr__(self):
        return f'"{self.value.upper()}"'