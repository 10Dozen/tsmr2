
class TestResult:
    def __init__(self, is_success, message = None, extra_data = None) -> None:
        self.name = "Unnamed"
        self.success = is_success
        self.message = message
        self.extra_data = extra_data
        self.relates_to = ""
        self.severity = ""
    
    def __repr__(self):
        return str({
            "name": self.name,
            "type": self.severity,
            "message": self.message,
            "data": self.extra_data
        })
    
    def export(self):
        return {
            "name": self.name,
            "type": self.severity,
            "message": self.message,
            "data": self.extra_data
        }

def metadata(name, severity):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result.name = name
            result.severity = severity
            return result
        
        return wrapper
    return decorator

def tests(module_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result.relates_to = module_name
            return result
        return wrapper
    return decorator

class My:
    def test_m1(self):
        print(1)
    
    @tests("tSF / EditorVehicleCrew")
    @metadata(name="Missing kits", severity="WARN")
    def test_m2(self):
        print(2)
        return TestResult(is_success=True, message="Some message")

    def run(self):
        r = [getattr(self,x)() for x in dir(self) if x.startswith('test')]
        print(r)

     



















from enum import StrEnum, auto



class DataVaultKeys(StrEnum):
    dzn_dynai = auto()
    dzn_gear = auto()
    kits = auto()
    mission = auto()
    

class DataVault:
    def __init__(self):
        self.resources = {}

    def register(self, id, value):
        self.resources[id] = value
    
    def get(self, id):
        return self.resources.get(id)

d = DataVault()
d.register(DataVaultKeys.kits, [100])

print(d.get(DataVaultKeys.kits))

























def onFail(test_name, test_type, test_msg):
    def decorator(func):
        def wrapper(**kwargs):
            result = func(**kwargs)
            output = {
                "name": test_name
            }

            if result:
                return output
            
            output['msg'] = test_msg.format(**kwargs)
            return output
        return wrapper
    return decorator



class Validator:
    @onFail("EVC.KitsExists", "ERR", "Missing kits")
    def kits_exists(self, dv: DataVault, kits: list):
        existing = dv.get(DataVaultKeys.kits)
        result = existing == kits



class tSFEVCHandler:
    VALIDATIONS = [
        "EVC.001"
    ]
    def __init__(self, v):
        self.validator = None
        self.kits_in_config = []

        self.vault.register_resource("EVC",self.reader)


    def validate(self):
        self..kits_exists(
            self.validator.get_resource("dzn_gear_kits"),
            self.reader.kits_in_config
        )
        
        v.validate(vid, self.reader.kits_in_config)

    def get_page_data(self):
        ...

        paga_data.add_validation_result(
            self.validator.evc_validtor.kits_exists(
                self.validator.get_resource("dzn_gear_kits"),
                self.reader.kits_in_config
            )
        )

