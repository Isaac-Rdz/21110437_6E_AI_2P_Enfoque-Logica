
from nltk import CFG, ChartParser

# Definir la gramática causal definida (DCG)
dcg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V
    VP -> V NP
    Det -> 'the'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

# Crear un parser para la gramática
parser = ChartParser(dcg_grammar)

# Ejemplo de uso: parsear una oración
sentence = "the cat chased the dog"
parsed_trees = list(parser.parse(sentence.split()))

# Mostrar los árboles sintácticos resultantes
for tree in parsed_trees:
    print(tree)
