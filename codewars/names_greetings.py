# Se o nome for igual retorna Boss, se não retorna Guest

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


print(greet("Daniel", "Daniel"))
print(greet("Daniel", "Rafael"))
