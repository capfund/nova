import re

def preprocess(text):
    result = ''
    in_quotes = False
    in_double_quotes = False

    for char in text:
        if char == '"' and not in_quotes:
            in_double_quotes = not in_double_quotes
        elif char == "'" and not in_double_quotes:
            in_quotes = not in_quotes
        elif char == ' ' and not in_quotes and not in_double_quotes:
            continue

        result += char

    return result


def get_quoted_text(text):
    # Regular expression pattern to match quoted text
    pattern = r'["\'](.*?)["\']'
    # Find all matches
    matches = re.findall(pattern, text)
    return matches

class Lexer:
    def __init__(self, line: str):
        self.line = line
        self.pos = 0

    def advance(self):
        self.pos += 1
    
    def lex(self):
        self.line = preprocess(self.line)
        toks = []
        while self.pos < len(self.line):
            current_char = self.line[self.pos]

            if current_char.isspace():
                pass       # advance automatically
            if current_char.isdigit():
                toks.append(self.PROCESS_DIGIT(int(current_char)))
            elif current_char == "+":
                toks.append("PLUS")
            elif current_char == "-":
                toks.append("MINUS")
            elif current_char == "*":
                toks.append("MULTIPLY")
            elif current_char == "/":
                toks.append("DIVIDE")
            elif current_char == "(":
                toks.append("LPAREN")
            elif current_char == ")":
                toks.append("RPAREN")
            elif current_char.lower() == "p" and self.line[self.pos + 1].lower() == "i":
                toks.append("PI")
                self.pos += 1
            elif current_char in ['"', "'"]:
                quoted_text = self.get_quoted_text(self.line[self.pos:])
                if quoted_text is not None:
                    toks.append(("STRING", quoted_text))
                    self.pos += len(quoted_text) + 2
                else:
                    pass
            elif current_char == "P" and self.line[self.pos + 1] == "R" and self.line[self.pos + 2] == "I" and self.line[self.pos + 3] == "N" and self.line[self.pos + 4] == "T":
                toks.append("PRINT")
                self.pos += len("PRINT") - 1
            self.advance()

        return toks

    @staticmethod
    def PROCESS_DIGIT(digit: int):
        return ("NUMBER", digit)

    @staticmethod
    def get_quoted_text(text):
        # Regular expression pattern to match quoted text
        pattern = r'["\'](.*?)["\']'
        # Find all matches
        matches = re.match(pattern, text)
        if matches:
            return matches.group(1)
        return None

