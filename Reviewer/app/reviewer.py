from .mission_sqm_handler import MissionSqmHandler
from .dzn_gear_handler import dznGearHandler
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
from .enums import tSFModules

class Reviewer:
    def __init__(self, path):
        self.path = path
        self.mission_sqm = None
        self.tsf_settings = None
        self.tsf_briefing = None
        self.tsf_intro_text = None
        self.tsf_mission_conditions = None
        self.tsf_ccp = None
        self.tsf = []
        self.reporter = None

    def review(self):
        self.mission_sqm = MissionSqmHandler(self.path)
        self.tsf_settings = tSFrameworkSettingsReader(self.path)
        self.dzn_gear = dznGearHandler(self.path)

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
        report_data = self.prepare_report_data()

        self.reporter = ReportGenerator(
            mission_name=self.mission_sqm.mission_filename,
            mission_creation_date=self.mission_sqm.creation_date
        )
        self.reporter.create_report(
            report_content=report_data,
            overview_img_path=self.mission_sqm.overview_img_src
        )

    def prepare_report_data(self):
        """Formats report data file"""
        report_data = {
            "filename": self.mission_sqm.mission_filename,
            "creationData": self.mission_sqm.creation_date,
            "pages": []
        }

        # Mission file page
        report_data['pages'].append(self.mission_sqm.get_page_data().export())

        # dzn Gear 
        report_data['pages'].append(self.dzn_gear.get_page_data().export())

        # TSF
        for handler in self.tsf:
            report_data['pages'].append(handler.get_page_data().export())

        return report_data

