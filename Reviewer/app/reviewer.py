from .mission_sqm_handler import MissionSqmHandler
from .dzn_gear_handler import dznGearHandler
from .dzn_dynai_handler import dznDynaiHandler
from .tSFHandlers import tSFrameworkSettingsReader, \
    tSFMissionConditionsHandler, tSFBriefingHandler, \
    tSFIntroTextHandler, tSFCCPHandler, tSFFARPHandler, \
    tSFAuthHandler, tSFAirborneHandler, tSFArtilleryHandler, \
    tSFERSHandler, tSFEUBHandler, tSFEVCHandler, \
    tSFConversationsHandler, tSFACEActionsHandler, tSFAdminToolsHandler, \
    tSFChatterHandler, tSFInteractivesHandler, tSFJIPTeleportHandler, \
    tSFMissionDefaultsHandler, tSFNotesHandler, tSFPOMHandler, \
    tSFSettingsHandler
from .report_generator import ReportGenerator
from .data_entities import PageReviewHandler

class Reviewer:
    def __init__(self, path):
        self.path = path
        self.mission_sqm = None
        self.dzn_gear = None 
        self.dzn_dynai = None
        self.tsf_settings = None
        self.tsf_briefing = None
        self.tsf_intro_text = None
        self.tsf_mission_conditions = None
        self.tsf_ccp = None
        self.tsf = []

        self.report_data = {}
        self.reporter = None

    def review(self):
        self.mission_sqm = MissionSqmHandler(self.path)
        self.tsf_settings = tSFrameworkSettingsReader(self.path)
        self.dzn_gear = dznGearHandler(self.path)
        self.dzn_dynai = dznDynaiHandler(self.path)

        self.tsf = [
            handler(self.path, self.mission_sqm.reader, self.dzn_gear)
            for handler 
            in (
                tSFBriefingHandler,
                tSFIntroTextHandler,
                tSFMissionConditionsHandler,
                tSFCCPHandler,
                tSFFARPHandler,
                tSFAuthHandler,
                tSFAirborneHandler,
                tSFArtilleryHandler,
                tSFERSHandler,
                tSFEVCHandler,
                tSFEUBHandler,
                tSFNotesHandler,
                tSFSettingsHandler,
                tSFMissionDefaultsHandler,
                tSFJIPTeleportHandler,
                tSFACEActionsHandler,
                tSFInteractivesHandler,
                tSFConversationsHandler,
                tSFChatterHandler,
                tSFPOMHandler,
                tSFAdminToolsHandler
            )
            if self.tsf_settings.is_module_active(handler.MODULE)
        ]

        self.generate_report()

    def generate_report(self):
        """Creates report from the read data"""
        pages = [
            self.mission_sqm,
            self.dzn_gear,
            self.dzn_dynai
        ]
        for handler in self.tsf:
            pages.append(handler)


        self.reporter = ReportGenerator()
        self.reporter.set_report_data(
            mission_name=self.mission_sqm.mission_filename,
            mission_creation_date=self.mission_sqm.creation_date,
            overview_img_path=self.mission_sqm.overview_img_src,
            pages=pages
        )
        self.reporter.create_report()
    