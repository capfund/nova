from core.novalexer import Lexer
from core.novaparser import Parser

def runshell():
    statement = input("nova 0.1 beta > ")

    if statement.lower() in ["quit", "exit"]:
        quit()

    lexer = Lexer(statement)
    tokens = lexer.lex()
    
    parser = Parser(tokens=tokens)
    result = parser.parse()

    if result:
        print(result)
    else:
        pass

while True:
    runshell()