import re


class RubyLanguage:
    name = "Ruby"
    extension = "rb"
    debugging_calls = [
        re.compile(r"\s*puts"),
        re.compile(r"\s*byebug"),
        re.compile(r"\s*pry"),
    ]
