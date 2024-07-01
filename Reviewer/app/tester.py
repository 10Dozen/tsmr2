from .enums import Component, PageTitle, RawContentLanguage
from .entities import PageReviewHandler, PageStatus, PageData, Severity, TestResult, DataReader
from .mission_sqm_reader import MissionSqmReader

import re

def meta(id: str, name: str, severity: Severity, message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result: TestResult = func(*args, **kwargs)
            result.name = f"{id}.{name}"
            result.severity = severity
            if message:
                result.message = f"{result.message}.\n{message}" if result.message else f"{message}"
            return result
        
        return wrapper
    return decorator

def tests(component: Component):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result.relates_to = component
            return result
        return wrapper
    return decorator



class Tester(PageReviewHandler):
    TITLE = PageTitle.Tests
    TESTS_PREFIX = 'test'

    def __init__(self, path: str):
        self.path = path
        self.components = {}
        self.results = None 
        self.results_raw = {}
    
    def register_components(self, components: dict[PageReviewHandler]):
        for review_handler in components:
            self.components[review_handler.COMPONENT] = review_handler

    def get_component(self, name: Component, reader: bool = True) -> DataReader:
        comp = self.components[name]
        return comp.reader if reader else comp

    def get_page_data(self):
        page = super().get_page_data()

        successful: list[TestResult] = []
        failed: list[TestResult]  = []
        for result in self.results_raw:
            successful.append(result) if result.succeed else failed.append(result)
        
        page.add_info("Failed", len(failed))
        page.add_info("Succeed", len(successful))

        for r in failed:
            icon = '✖' if r.severity == Severity.ERROR else '⚠'
            page.add_raw_content(
                filename=f"{icon} {r.name}",
                content=str(r),
                language=RawContentLanguage.SQF
            )

        for r in successful:
            page.add_raw_content(
                filename=f"✓ {r.name}",
                content=str(r),
                language=RawContentLanguage.SQF
            )

        page.name = f"✖ {page.name} ✖" if failed else f"{page.name} ✓"

        return page

    def run_tests(self):
        self.results_raw: list[TestResult] = [
            getattr(self,x)() 
            for x in dir(self) 
            if x.startswith(self.TESTS_PREFIX)
        ]

    # ----
    # Tests
    # ----

    @tests(Component.Mission)
    @meta("SQM-001", "Имя превью картинки == overview.jpg", Severity.ERROR,
          "Переименуйте вашу превью-картинку в 'overview.jpg' и укажите это имя в редакторе")
    def test_sqm001(self):
        sqm: MissionSqmReader = self.get_component(Component.Mission)
        
        return TestResult(
            is_success=sqm.overview_picture == 'overview.jpg',
            extra_data=sqm.overview_picture
        )

    @tests(Component.Mission)
    @meta("SQM-002", "Имя миссии соответсвует шаблону", Severity.WARNING,
          """Переименуйте миссию (в редакторе и саму папку миссии), чтобы имя соответствовало шаблону - 
             Тип + Кол-во слотов + Имя миссии + Версия (например, CO11 Mission Name (1A))""")
    def test_sqm002(self):
        sqm: MissionSqmReader = self.get_component(Component.Mission)
        title = sqm.title
        title_regex = r'^(CO|ADV|TVT)[0-9]+\s.+$\s\(.*\)$'
        is_match = re.match(title_regex, title, re.IGNORECASE)

        return TestResult(
            is_success=True if is_match else False,
            extra_data=title
        )

