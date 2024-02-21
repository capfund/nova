from core.novalexer import Lexer
from core.novainterpreter import Interpreter

def runshell():
    statement = input("nova 0.1.4 beta > ")

    if statement.lower() in ["quit", "exit"]:
        quit()

    lexer = Lexer(statement)
    tokens = lexer.lex()
    
    parser = Interpreter(tokens=tokens)
    result = parser.parse()

    if result:
        print(result)
    else:
        pass

while True:
    runshell()
