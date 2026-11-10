def add(a, b):
    return a + b


def record(value, history=None):
    if history == None:
        history = []
    history.append(value)
    return history
