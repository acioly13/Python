# # Caxeiro Viajante
# import numpy as np
# from itertools import permutations
#
# # numero de cidades
# num_cidades = 5
#
# # matriz de distancia entre as cidades
# dist_matrix = np.array([
#     [0, 10, 15, 20, 25],
#     [0, 10, 15, 20, 25],
#     [0, 10, 15, 20, 25],
#     [0, 10, 15, 20, 25],
#     [0, 10, 15, 20, 25],
# ])
#
#
# # Função para calcular a distancia de uma rota
# def calc_distance(rota):
#     distancia = 0
#     for i in range(num_cidades - 1):
#         distancia += dist_matrix[rota[i], rota[i + 1]]
#     distancia += dist_matrix[rota[-1], rota[0]]
#     return distancia
#
#
# # Gera todas as permutações possiveis das cidades
# cidades_permut = permutations(range(num_cidades))
#
# # Encontra a rota com a menor distancia
# min_distancia = np.inf
# for rota in cidades_permut:
#     distancia = calc_distance(rota)
#     if distancia < min_distancia:
#         min_distancia = distancia
#         min_rota = rota
#
# # Imprime a rota e a distancia minima encontrada
# print('Rota: ', min_rota)
# print('Distancia Minima: ', min_distancia)
#
# # Caxeiro Viajante
# import requests
#
# # substitua <YOUR_API_KEY> pela sua chave de API
# API_KEY = "AIzaSyB2phcxml_Y6qUNzkXvbNIPkAD8_v8lK_Q"
#
#
# # função para obter a distância entre duas cidades usando a API
# def get_distance(origin, destination):
#     url = "https://maps.googleapis.com/maps/api/distancematrix/json"
#     params = {
#         "origins": origin,
#         "destinations": destination,
#         "key": API_KEY
#     }
#     response = requests.get(url, params=params)
#
#     # verifica se a resposta contém informações de distância
#     data = response.json()
#     if data["status"] != "OK":
#         raise Exception(f"Erro ao obter distância entre {origin} e {destination}: {data['status']}")
#     if not data["rows"] or not data["rows"][0]["elements"]:
#         raise Exception(f"Sem informações de distância entre {origin} e {destination}")
#
#     # extrai a distância da resposta
#     distance = data["rows"][0]["elements"][0]["distance"]["value"]
#     return distance
#
#
# # matriz de distância entre as cidades
# dist_matrix = [[0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0]]
#
# # calcula a distância entre as cidades e preenche a matriz de distância
# cities = ["Manaus, AM", "Salvador, BA", "Maricá, RJ", "São Gonçalo, RJ", "Búzios, RJ"]
# for i in range(len(cities)):
#     for j in range(i, len(cities)):
#         try:
#             distance = get_distance(cities[i], cities[j])
#             dist_matrix[i][j] = distance
#             dist_matrix[j][i] = distance
#         except Exception as e:
#             print(str(e))
#
# # imprime a matriz de distância
# print("Matriz de distância:")
# for row in dist_matrix:
#     print(row)
# Caixeiro Viajante
import osmnx as ox
from scipy.spatial import distance_matrix
from itertools import permutations

# Definir as cidades que serão visitadas
cities = ['Maricá', 'Manaus', 'Salvador', 'São Gonçalo', 'Búzios']

# Obter as coordenadas geográficas das cidades utilizando o Open Street Maps
city_points = []
for city in cities:
    result = ox.geocode(city + ', Brazil')
    city_points.append((result[0], result[1]))

# Calcular a matriz de distância entre as cidades
distances = distance_matrix(city_points, city_points)

# Encontrar a ordem ótima de visitação para todas as possíveis combinações de cidades como ponto de partida
best_distance = float('inf')
best_order = []
for i in range(len(cities)):
    order = list(permutations(range(len(cities))))
    for j in range(len(order)):
        if order[j][0] != i:
            continue
        path = [i] + list(order[j])
        path.remove(path[0])
        distance = distances[path[:-1], path[1:]].sum()
        if distance < best_distance:
            best_distance = distance
            best_order = path

# Imprimir a ordem das cidades a serem visitadas e a distância total percorrida
print('Ordem das cidades visitadas: ', [cities[i] for i in best_order])
print('Distância total percorrida: ', best_distance, 'km')
