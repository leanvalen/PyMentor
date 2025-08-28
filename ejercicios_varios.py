# tareas = ["Lavar la ropa", "Pagar impuestos", "Llamar al dentista"]
# print(tareas[1])
# tareas[0] = "Sacar al perro"
# print(tareas)
# tareas.append("Regar las plantas")
# print(tareas)
# for tarea in tareas:
#     print(f"Lista de tareas {tarea.upper()}")
# lavar_la_ropa = "Pagar impuestos" in tareas
# if lavar_la_ropa:
#     print(tareas.index("Pagar impuestos"))
# print(lavar_la_ropa)
# invitados = ["Ana", "Luis", "Maria", "Carlos"]
# esta_maria = "Maria" in invitados
# if esta_maria:
#     print(f"Maria esta en la posicion: {invitados.index("Maria")}")
# cantidad_invitados = len(invitados)
# print(f"En total, hay {cantidad_invitados} invitados.")
# participantes = ["Juan", "Pedro", "Sofia", "Laura"]
# participantes.remove("Pedro")
# del participantes[0]
# print(f"Esta es la lista final: {participantes}")
# podio = ["Carlos", "Ana", "Luis", "Marta", "Leo"]
# medallistas = podio[:3]
# menciones_honorificas = podio[3:]
# print(f"Estos son los integrantes del podio {medallistas}")
# print(f"Estos recibieron mencion honorifica {menciones_honorificas}")
# Ordenando listas
# lista_compras = ["Manzanas", "Leche", "Pan", "Huevos", "Aceite"]
# lista_compras.sort()
# print(f"Lista ordenada: {lista_compras}")

# tiempos = [12.5, 11.9, 13.1, 12.2]
# tiempos_ordenados = sorted(tiempos)
# print(f"El ganador hizo este tiempo: {tiempos_ordenados[0]}")
# print(f"Esta es la lista originañ: {tiempos}")
lista_de_compras = []
while True:
    item = input("Ingresa un articulo o 'Listo' para finalizar: ")
    if item.lower() == "listo":
        break
    lista_de_compras.append(item)
    print(f"Esta es la lista de compras hasta el momento: {lista_de_compras}")

print(f"Esta es la lista de compras final: {lista_de_compras}")
