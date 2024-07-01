from .enums import Component, PageTitle, RawContentLanguage
from .entities import PageReviewHandler, PageStatus, PageData, Severity, TestResult, DataReader

import yaml

def meta(id: str, name: str, severity: Severity, message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result: TestResult = func(*args, **kwargs)
            result.name = f"{id}.{name}"
            result.severity = severity
            if message:
                result.message = f"{message}.{result.message}"
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
    
    def register_component(self, name: Component, component: DataReader):
        self.components[name] = component
    
    def register_components(self, components: dict[Component, DataReader]):
        for name, component in components.items():
            self.register_component(name, component)

    def get_component(self, name: Component) -> DataReader:
        return self.components[name]

    def get_page_data(self):
        page = super().get_page_data()

        page.add_raw_content(
            "Validation", 
            yaml.dump_all(self.results_raw), 
            RawContentLanguage.YAML
        )

        return page

    def run_tests(self):
        r = [
            getattr(self,x)() 
            for x in dir(self) 
            if x.startswith(self.TESTS_PREFIX)
        ]
        print(r)
        self.results_raw = r

    # ----
    # Tests
    # ----

    @tests(Component.Mission)
    @meta("ID001", "Some test", Severity.WARNING)
    def test_basic(self):
        return TestResult(True)

