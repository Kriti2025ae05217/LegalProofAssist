import language_tool_python

tool = language_tool_python.LanguageTool('en-US')


def check_grammar(text):

    matches = tool.check(text)

    grammar_errors = []

    for match in matches:

        grammar_errors.append({

            "word": text[
                match.offset:
                match.offset + match.errorLength
            ],

            "suggestion":
                match.replacements[0]
                if match.replacements
                else "",

            "error_type": "Grammar",

            "confidence": 0.90

        })

    return grammar_errors
