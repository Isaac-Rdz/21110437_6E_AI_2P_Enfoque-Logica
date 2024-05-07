
from defeasible import Rule, KnowledgeBase

# Definir reglas de razonamiento por defecto
rules = [
    Rule("bird(x)", "flies(x)"),
    Rule("penguin(x)", "not flies(x)", type="defeasible"),
    Rule("bird(x)", "not penguin(x)")
]

# Crear una base de conocimiento
kb = KnowledgeBase(rules)

# Agregar hechos a la base de conocimiento
kb.add_fact("bird(john)")
kb.add_fact("penguin(jim)")

# Consultar la base de conocimiento
print("Resultados de la consulta:")
print("¿John vuela?", kb.query("flies(john)"))
print("¿Jim vuela?", kb.query("flies(jim)"))
