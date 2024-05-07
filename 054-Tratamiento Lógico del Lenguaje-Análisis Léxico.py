
import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return Token('INTEGER', self.integer())
            elif self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            elif self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            else:
                raise Exception('Invalid character')

        return Token('EOF', None)

# Ejemplo de uso
text = "10 + 20 - 5"
lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    if token.type == 'EOF':
        break
    print(token)
