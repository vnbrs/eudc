class RubyLanguage:
    name = 'Ruby'
    extension = 'rb'
    debugging_calls = [
        r'\s*puts',
        r'\s*byebug',
        r'\s*pry',
    ]
