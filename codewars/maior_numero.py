# Ordena numeros de forma decrescente
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(5915))
