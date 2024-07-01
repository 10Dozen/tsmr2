from .mission_sqm_handler import MissionSqmHandler
from .dzn_gear_handler import dznGearHandler
from .dzn_dynai_handler import dznDynaiHandler
from .tSFModulesHandlers import tSFrameworkSettingsHandler, \
    tSFMissionConditionsHandler, tSFBriefingHandler, \
    tSFIntroTextHandler, tSFCCPHandler, tSFFARPHandler, \
    tSFAuthHandler, tSFAirborneHandler, tSFArtilleryHandler, \
    tSFERSHandler, tSFEUBHandler, tSFEVCHandler, \
    tSFConversationsHandler, tSFACEActionsHandler, tSFAdminToolsHandler, \
    tSFChatterHandler, tSFInteractivesHandler, tSFJIPTeleportHandler, \
    tSFMissionDefaultsHandler, tSFNotesHandler, tSFPOMHandler, \
    tSFSettingsHandler
from .tester import Tester
from .report_generator import ReportGenerator
from .entities import PageReviewHandler
from .enums import Component


class Reviewer:
    def __init__(self, path):
        self.path = path

        self.mission_sqm = None
        self.dzn_gear = None 
        self.dzn_dynai = None
        self.tsf_settings = None
        self.tsf = []
        self.tester = None

        self.report_data = {}
        self.reporter = None

    def review(self):
        self.mission_sqm = MissionSqmHandler(self.path)
        self.tsf_settings = tSFrameworkSettingsHandler(self.path)
        self.dzn_gear = dznGearHandler(self.path)
        self.dzn_dynai = dznDynaiHandler(self.path)
        
        self.tsf = [
            handler(self.path, self.mission_sqm.reader)
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
            if self.tsf_settings.is_module_active(handler.COMPONENT)
        ]

        self.tester = Tester(self.path)
        self.tester.register_components([
            self.mission_sqm,
            self.dzn_gear,
            self.dzn_dynai,
            self.tsf_settings
        ])
        self.tester.register_components(self.tsf)

        self.tester.run_tests()

        self.generate_report()


    def generate_report(self):
        """Creates report from the read data"""
        pages = [
            self.mission_sqm,
            self.dzn_gear,
            self.dzn_dynai,
            self.tsf_settings,
            self.tester
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
    