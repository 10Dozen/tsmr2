
from .enums import PageStatus, InfoType, Severity, RawContentLanguage

class InfoValue:
    def __init__(self, title: str, value, type: InfoType):
        self.title = title
        self.value = value 
        self.type = type if type else InfoType.PLAIN
    
    def export(self) -> dict:
        return {
            "name": self.title,
            "value": self.value,
            "type": str(self.type)
        }


class RawContent:
    def __init__(self, filename: str, 
                 content: list[str], 
                 language: RawContentLanguage) -> None:
        self.filename = filename
        self.content = content
        self.language = language
    
    def export(self) -> dict:
        return {
            "filename": self.filename,
            "content": self.content,
            "language": str(self.language)
        }


class TestResult:
    def __init__(self, is_success: bool = True, 
                 message: str = "", 
                 extra_data: list = None) -> None:
        self.name: str = "Unnamed"
        self.relates_to: str = ""
        self.severity: Severity = ""
        self.succeed: bool = is_success
        self.message: str = message
        self.extra_data: list[str|int|float] = extra_data
    
    def set_metadata(self, name: str, severity: Severity):
        self.name = name
        self.severity = severity

    def set_relation(self, relates_to):
        self.relates_to = relates_to

    def __repr__(self):
        return str(self.export())
    
    def export(self) -> dict:
        return {
            "name": self.name,
            "type": self.severity,
            "message": self.message,
            "data": self.extra_data
        }
    

class PageData:
    def __init__(self, title: str):
        self.name = title
        self.status = PageStatus.OK
        self.info = []
        self.raw_content = []
    
    def add_info(self, title: str, value, type: InfoType|None = None):
        self.info.append(
            InfoValue(title, value, type)
        )
    
    def add_raw_content(self, filename: str, content: list[str], language: RawContentLanguage):
        self.raw_content.append(
            RawContent(filename, content, language)
        )
    
    def export(self) -> dict:
        return {
            "name": self.name,
            "status": self.status,
            "info": [e.export() for e in self.info],
            "rawContent": [e.export() for e in self.raw_content]
        }


class PageReviewHandler:
    TITLE = ""

    def __init__(self, path):
        self.path = path
        self.reader: DataReader = None

    def get_page_data(self):
        return PageData(self.TITLE)

class DataReader:
    def _read_files(self):
        pass

    @staticmethod
    def _read_file(path):        
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
