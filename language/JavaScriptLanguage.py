import re


class JavaScriptLanguage:
    name = "JavaScript"
    extension = "js"
    debugging_calls = [re.compile(r"debugger"), re.compile(r"console\.log")]
