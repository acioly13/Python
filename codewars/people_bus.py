# Recebe uma lista de pares [pessoa, parada] e retorna o número de pessoas que sobraram no ônibus

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


print(number([[10, 0], [3, 5], [5, 8]]))  # 5
