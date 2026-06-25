import sympy as sp

def containsConditionSet(obj):
    # 1. Se è una lista o una tupla nativa di Python, controlla ricorsivamente gli elementi
    if isinstance(obj, (list, tuple)):
        return any(containsConditionSet(item) for item in obj)

    # 2. Se è direttamente un ConditionSet
    if isinstance(obj, sp.ConditionSet):
        return True

    # 3. Se è un contenitore di SymPy (es. Complement, Union, Intersection)
    if hasattr(obj, 'args'):
        return any(containsConditionSet(arg) for arg in obj.args)
    return False