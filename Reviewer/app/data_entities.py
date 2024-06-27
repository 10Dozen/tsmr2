
from .enums import PageStatus, InfoType

class InfoValue:
    def __init__(self, title, value, type):
        self.title = title
        self.value = value 
        self.type = type if type else InfoType.PLAIN
    
    def export(self):
        return {
            "name": self.title,
            "value": self.value,
            "type": str(self.type)
        }


class RawContent:
    def __init__(self, filename, content, language):
        self.filename = filename
        self.content = content
        self.language = language
    
    def export(self):
        return {
            "filename": self.filename,
            "content": self.content,
            "language": str(self.language)
        }


class PageData:
    def __init__(self, title):
        self.name = title
        self.status = PageStatus.OK
        self.info = []
        self.raw_content = []
    
    def add_info(self, title, value, type=None):
        self.info.append(
            InfoValue(title, value, type)
        )
    
    def add_raw_content(self, filename, content, language):
        self.raw_content.append(
            RawContent(filename, content, language)
        )
    
    def export(self):
        return {
            "name": self.name,
            "status": self.status,
            "info": [e.export() for e in self.info],
            "rawContent": [e.export() for e in self.raw_content]
        }


class PageReviewHandler:
    TITLE = ""
    
    def get_page_data(self):
        return PageData(self.TITLE)
    
