import math
from .exceptionbase import *

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.output = None
        self.arithmetic_operators = ["PLUS", "MINUS", "DIVIDE", "MULTIPLY"]

    def convertNumToInt(self):
        converted_list = []
        i = 0
        while i < len(self.tokens):
            if isinstance(self.tokens[i], tuple) and self.tokens[i][0] == "NUMBER":
                current_number = str(self.tokens[i][1])
                while i + 1 < len(self.tokens) and isinstance(self.tokens[i + 1], tuple) and self.tokens[i + 1][0] == "NUMBER":
                    current_number += str(self.tokens[i + 1][1])
                    i += 1
                converted_list.append(int(current_number))
            elif self.tokens[i] == "PI":
                converted_list.append(math.pi)
            else:
                converted_list.append(self.tokens[i])
            i += 1
        self.tokens = converted_list

    def parse_arithmetics(self):
        self.convertNumToInt()
        
        if not self.tokens or not isinstance(self.tokens[0], int) and not isinstance(self.tokens[0], float):
            return None  # No valid starting number

        self.output = self.tokens[0]
        for i in range(1, len(self.tokens), 2):
            if i + 1 < len(self.tokens):
                if isinstance(self.tokens[i + 1], int) or isinstance(self.tokens[i + 1], float) and self.tokens[i] in self.arithmetic_operators:
                    if self.tokens[i] == "PLUS":
                        self.output += self.tokens[i + 1]
                    elif self.tokens[i] == "MINUS":
                        self.output -= self.tokens[i + 1]
                    elif self.tokens[i] == "MULTIPLY":
                        self.output *= self.tokens[i + 1]
                    elif self.tokens[i] == "DIVIDE":
                        if self.tokens[i + 1] == 0:
                            return divisionByZeroException()
                        self.output /= self.tokens[i + 1]
                    else:
                        return None  # Invalid operator
                elif isinstance(self.tokens[i + 1], str) and self.tokens[i] == "PRINT":
                    print(self.tokens[i + 1][1])
                else:
                    print([self.tokens[i], self.tokens[i + 1]])
                    return None  # Invalid expression
            
        return self.output
    
    def parse(self):
        arithmetic_res = self.parse_arithmetics()
        if arithmetic_res:
            return arithmetic_res
        
        for idx in range(len(self.tokens)):
            if self.tokens[idx] == "PRINT" and len(self.tokens) > (idx + 1):
                print(self.tokens[idx + 1][1])
            elif self.tokens[idx] == "LEN" and len(self.tokens) > (idx + 1):
                self.output = len(self.tokens[idx + 1][1])

        return self.output