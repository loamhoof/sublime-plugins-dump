@requires_authorization(roles=["ADMIN"])
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print(f'Gre\'ater {param1}')
    return (param2 - param1 + 1 + 0b10) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
