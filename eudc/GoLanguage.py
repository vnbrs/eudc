import re


class GoLanguage:
    name = "Go"
    extension = "go"
    debugging_calls = [re.compile(r"fmt\.Println"), re.compile(r"fmt\.Printf")]
