
import itertools

# Función para generar todas las combinaciones de valores booleanos para un número dado de variables
def generate_truth_table(num_vars):
    truth_values = list(itertools.product([True, False], repeat=num_vars))
    return truth_values

# Función para imprimir una tabla de verdad para una expresión lógica dada
def print_truth_table(expression):
    num_vars = expression.count('A')  # Se asume que las variables se representan como 'A', 'B', 'C', ...
    truth_table = generate_truth_table(num_vars)
    
    header = expression.replace('(', '').replace(')', '').replace('and', '∧').replace('or', '∨').replace('not', '¬')
    print(f"{'|'.join(header):^{2*num_vars + len(header) + 1}} | Resultado")
    print('-' * (2*num_vars + len(header) + 12))
    
    for row in truth_table:
        values_dict = {chr(65 + i): value for i, value in enumerate(row)}
        values_str = [str(value) for value in row]
        eval_expression = expression.format(**values_dict)
        print(f"{'|'.join(values_str):^10} | {'True' if eval(eval_expression) else 'False':^8}")

# Ejemplos de expresiones lógicas
expressions = [
    "not A",
    "A and B",
    "A or B",
    "A or (B and C)"
]

# Generar y mostrar las tablas de verdad para las expresiones dadas
for expression in expressions:
    print(f"Tabla de verdad para la expresión: {expression}")
    print_truth_table(expression)
    print()
