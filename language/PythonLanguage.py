import re


class PythonLanguage:
    name = "Python"
    extension = "py"
    debugging_calls = [re.compile(r"breakpoint"), re.compile(r"print")]
