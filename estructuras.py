# Hay diferentes formas de representar los datos, y cada forma 
# tiene su propia forma de recorrerlos para procesarlos 
# Resuelva los siguientes casos, donde la variable 'notas' contiene  
# las notas de los 3 parciales para 3 materias de un mismo estudiante 
# Recuerde: 
# - Analice primero, planee/diseñe una solución, luego escriba el código 
# - Utilice comentarios para explicar las partes importantes 
# - Si es el caso utilice constantes 
# - Realice sus propias pruebas para verificar que todo funciona 

######################################################################## 
# Caso 1: Lista de Listas 
notas = [ 
["Calculo", 3.5, 2.5, 1.5], 
["Química", 2.5, 3.0, 5.0], 
["Deporte", 2.4, 2.0, 2.2], 
["Lógica", 1.5, 4.0, 4.5] 
] 

# Definimos constantes para los porcentajes de cada parcial
PESO_PARCIAL_1 = 0.3  # 30%
PESO_PARCIAL_2 = 0.3  # 30%
PESO_PARCIAL_3 = 0.4  # 40%

# 1.1 Calcular la nota final de cada materia (30%, 30% y 40%),  
# y agregue el valor a los datos 
def c11_final(): 
    # Iteramos sobre cada materia en la lista 'notas'
    for materia in notas:
        # Calculamos la nota final usando los pesos definidos
        nota_final = (materia[1] * PESO_PARCIAL_1 +
                      materia[2] * PESO_PARCIAL_2 +
                      materia[3] * PESO_PARCIAL_3)
        # Agregamos la nota final como un nuevo elemento en la lista de la materia
        materia.append(round(nota_final, 2))
    

# 1.2 Calcule el promedio de las notas del Estudiante 
def c12_promedio(): 
    # Inicializamos la suma de todas las notas de los parciales
    suma_parciales = 0
    # Inicializamos el contador total de notas de parciales
    total_notas = 0
    # Iteramos sobre cada materia para sumar las notas de los parciales
    for materia in notas:
        # Sumamos los parciales de la materia (índices 1, 2 y 3)
        suma_parciales += materia[1] + materia[2] + materia[3]
        # Incrementamos el contador por cada nota sumada
        total_notas += 3
    # Calculamos el promedio dividiendo la suma por el número de parciales
    promedio = suma_parciales / total_notas
    # Retornamos el promedio redondeado a dos decimales
    return round(promedio, 2)

# Llamar funciones, y mostrar Resultados 
c11_final()  # Calculamos las notas finales

# Mostramos solo el nombre de la materia y su nota final
print("Notas finales por materia:")
for materia in notas:
    print(f"{materia[0]}: {materia[-1]}")

# Mostramos el promedio basado en las notas de los parciales
print("Promedio basado en las notas de los parciales:", c12_promedio())

######################################################################## 
# Caso 2: Diccionario de Listas 
notas1 = { 
"Calculo": [3.5, 2.5, 1.5], 
"Química": [2.5, 3.0, 5.0], 
"Deporte": [2.4, 2.0, 2.2], 
"Lógica": [1.5, 4.0, 4.5] 
} 

# 2.1 Calcular la nota final de cada materia (30%, 30% y 40%),  
# y agregue el valor a los datos
def c21_final(): 
    # Iteramos sobre cada materia y sus notas en el diccionario
    for materia, parciales in notas1.items():
        # Calculamos la nota final usando los pesos definidos
        nota_final = (parciales[0] * PESO_PARCIAL_1 +
                      parciales[1] * PESO_PARCIAL_2 +
                      parciales[2] * PESO_PARCIAL_3)
        # Agregamos la nota final a la lista de parciales de la materia
        parciales.append(round(nota_final, 2))
 
# 2.2 Calcule el promedio de las notas del Estudiante 
def c22_promedio(): 
    # Inicializamos la suma de todas las notas de los parciales
    suma_parciales = 0
    # Inicializamos el contador total de notas de parciales
    total_notas = 0
    # Iteramos sobre cada materia y sus parciales en el diccionario
    for parciales in notas1.values():
        # Sumamos las tres notas de los parciales (índices 0, 1 y 2)
        suma_parciales += parciales[0] + parciales[1] + parciales[2]
        # Incrementamos el contador por las tres notas de parciales
        total_notas += 3
    # Calculamos el promedio dividiendo la suma por el número total de notas
    promedio = suma_parciales / total_notas
    # Retornamos el promedio redondeado a dos decimales
    return round(promedio, 2)

# Llamar funciones, y mostrar Resultados 
c21_final()  # Calculamos las notas finales

# Mostramos solo el nombre de la materia y su nota final
print("Notas finales por materia:")
for materia, parciales in notas1.items():
    print(f"{materia}: {parciales[-1]}")  # Accedemos a la última nota en la lista

# Mostramos el promedio basado en las notas de los parciales
print("Promedio basado en las notas de los parciales:", c22_promedio())

######################################################################## 
# Caso 3: Diccionario de Diccionarios 
notas2 = { 
  "Calculo": {"pp": 3.5,  
              "sp": 2.5,  
              "tp": 1.5}, 
  "Química": {"pp": 2.5,  
              "sp": 3.0,  
              "tp": 5.0}, 
  "Deporte": {"pp": 2.4,  
              "sp": 2.0, 
              "tp": 2.2}, 
  "Lógica":  {"pp": 1.5,  
              "sp": 4.0,  
              "tp": 4.5} 
}

# 3.1 Calcular la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos 
def c31_final(): 
    # Iteramos sobre cada materia y su diccionario de notas
    for materia, parciales in notas2.items():
        # Calculamos la nota final usando los pesos definidos
        nota_final = (parciales["pp"] * PESO_PARCIAL_1 +
                      parciales["sp"] * PESO_PARCIAL_2 +
                      parciales["tp"] * PESO_PARCIAL_3)
        # Agregamos la nota final al diccionario de parciales
        parciales["final"] = round(nota_final, 2)

# 3.2 Calcule el promedio de las notas del Estudiante 
def c32_promedio(): 
    # Inicializamos la suma de todas las notas de los parciales
    suma_parciales = 0
    # Inicializamos el contador total de notas de parciales
    total_notas = 0
    # Iteramos sobre cada materia y su diccionario de parciales
    for parciales in notas2.values():
        # Sumamos las notas de los parciales ("pp", "sp", "tp")
        suma_parciales += parciales["pp"] + parciales["sp"] + parciales["tp"]
        # Incrementamos el contador por cada parcial sumado
        total_notas += 3
    # Calculamos el promedio dividiendo la suma por el número total de parciales
    promedio = suma_parciales / total_notas
    # Retornamos el promedio redondeado a dos decimales
    return round(promedio, 2)

#Llamar funciones, y mostrar Resultados. 
c31_final()  # Calculamos las notas finales

# Mostramos solo el nombre de la materia y su nota final
print("Notas finales por materia:")
for materia, parciales in notas2.items():
    print(f"{materia}: {parciales['final']}")  # Accedemos a la nota final calculada

# Mostramos el promedio basado en las notas de los parciales
print("Promedio basado en las notas de los parciales:", c32_promedio())