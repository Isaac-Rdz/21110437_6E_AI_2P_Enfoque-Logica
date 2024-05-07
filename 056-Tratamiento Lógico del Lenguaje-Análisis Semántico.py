
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens[0]
        self.index = 0

    def error(self):
        raise Exception('Error de sintaxis')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.index += 1
            if self.index < len(self.tokens):
                self.current_token = self.tokens[self.index]
            else:
                self.current_token = None
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat('INTEGER')
        return token.value

    def term(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                result *= self.factor()
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                divisor = self.factor()
                if divisor == 0:
                    raise Exception('Error semántico: división por cero')
                result /= divisor
        return result

    def expr(self):
        result = self.term()
        while self.current_token is not None and self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            elif token.type == 'MINUS':
                self.eat('MINUS')
                result -= self.term()
        return result

# Ejemplo de uso
tokens = [
    Token('INTEGER', 10),
    Token('DIVIDE', '/'),
    Token('INTEGER', 0),
    Token('EOF')
]

parser = Parser(tokens)
try:
    result = parser.expr()
    print("Resultado:", result)
except Exception as e:
    print("Error:", e)
