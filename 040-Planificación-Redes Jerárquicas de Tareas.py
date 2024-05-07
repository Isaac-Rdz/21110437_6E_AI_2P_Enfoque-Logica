
class HTNNode:
    def __init__(self, task_name, is_primitive=False):
        self.task_name = task_name
        self.is_primitive = is_primitive
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_decomposable(self):
        return not self.is_primitive

def execute_task(task):
    print("Executing task:", task.task_name)

def execute_htn(htn_node):
    if htn_node.is_primitive:
        execute_task(htn_node)
    else:
        for child in htn_node.children:
            execute_htn(child)

# Crear una estructura de HTN
root = HTNNode("Root")

subtask1 = HTNNode("Subtask 1", is_primitive=True)
subtask2 = HTNNode("Subtask 2", is_primitive=True)

decomposable_task = HTNNode("Decomposable Task")
decomposable_task.add_child(subtask1)
decomposable_task.add_child(subtask2)

root.add_child(decomposable_task)

# Ejecutar la HTN
execute_htn(root)
