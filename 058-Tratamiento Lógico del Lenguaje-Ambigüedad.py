
import nltk

# Definir la gramática del "jardín del abuelo"
grammar = nltk.CFG.fromstring("""
    S -> NP VP | S CONJ S
    NP -> Det N
    VP -> V NP | V
    Det -> 'the'
    N -> 'grandfather' | 'garden'
    V -> 'saw' | 'ate'
    CONJ -> 'and' | 'or'
""")

# Crear un parser para la gramática
parser = nltk.ChartParser(grammar)

# Ejemplo de uso: analizar una oración ambigua
sentence = "the grandfather saw the garden and ate"
parsed_trees = list(parser.parse(sentence.split()))

# Mostrar los árboles sintácticos resultantes
for tree in parsed_trees:
    print(tree)
