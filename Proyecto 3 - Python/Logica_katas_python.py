# %%
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    """
    Función que calcula la frecuencia de cada letra en una cadena de texto.

    Args:
        texto (str): cadena de texto a analizar

    Returns:
        dict: diccionario con las letras como claves y su frecuencia como valores
    """
    
    frecuencias = {}
    
    for caracter in texto:
        if caracter != " ":
            caracter = caracter.lower()
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    
    return frecuencias

# %%
resultado = frecuencia_letras("hola mundo")
print(resultado)

# %%
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar_lista(numeros):
    """
    Función que devuelve una lista con el doble de cada número.

    Args:
        numeros (list): lista de números

    Returns:
        list: nueva lista con cada valor multiplicado por 2
    """
    # Utilizo lambda porque es una forma rápida de crear una función sin ponerle nombre.
    resultado = list(map(lambda x: x * 2, numeros))
    return resultado

# %%
numeros = [1, 2, 3, 4]
print(duplicar_lista(numeros))

# %%
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista, objetivo):
    """
    Función que devuelve las palabras que contienen una subcadena.

    Args:
        lista (list): lista de palabras
        objetivo (str): palabra o texto a buscar

    Returns:
        list: palabras que contienen el objetivo
    """
    
    resultado = []
    
    for palabra in lista:
        if objetivo in palabra:
            resultado.append(palabra)
    
    return resultado

# %%
lista = ["casa", "cascanueces", "pecas", "caseta", "gato"]
print(filtrar_palabras(lista, "cas"))

# %%
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    """
    Función que calcula la diferencia entre los elementos de dos listas.

    Args:
        lista1 (list): primera lista de números
        lista2 (list): segunda lista de números

    Returns:
        list: lista con la diferencia de los elementos
    """
    
    return list(map(lambda x, y: x - y, lista1, lista2))

# %%
print(diferencia_listas([22, 36, 42], [5, 2, 9]))

# %%
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado

def evaluar_notas(numeros, nota_aprobado=5):
    """
    Función que calcula la media de una lista y determina si está aprobada.

    Args:
        numeros (list): lista de números
        nota_aprobado (int, float): nota mínima para aprobar (por defecto 5)

    Returns:
        tupla: (media, estado)
    """
    
    media = sum(numeros) / len(numeros)
    
    # Hacemos un condicional if/else para poner la condición de si está aprobado o no
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

# %%
resultado = evaluar_notas([6, 7, 4, 8])
print(resultado)

# %%
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    """
    Función que calcula el factorial de un número de forma recursiva.

    Args:
        n (int): número entero positivo

    Returns:
        int: factorial del número
    """
    # Esto evita que la función se llame infinitamente
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# %%
print(factorial(6))

# %%
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    """
    Función que convierte una lista de tuplas en una lista de strings.

    Args:
        lista_tuplas (list): lista de tuplas

    Returns:
        list: lista de strings
    """
    
    return list(map(lambda t: str(t), lista_tuplas))

# %%
resultado = tuplas_a_strings([("hola", "mundo"), ("buenos", "días")])
print(resultado)

# %%
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    """
    Programa que pide dos números y realiza su división manejando errores.
    """
    
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = num1 / num2
        
        print("División exitosa:", resultado)

    # Si el usuario escribe letras: error
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    
    # Si el usuario divide entre 0: error
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    
    finally:
        print("Fin del programa.")


# %%
dividir_numeros()

# %%
dividir_numeros()

# %%
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    """
    Función que elimina mascotas prohibidas de una lista.

    Args:
        lista_mascotas (list): lista de nombres de mascotas

    Returns:
        list: lista sin las mascotas prohibidas
    """
    
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

# %%
mascotas = ["Perro", "Mono", "Cocodrilo", "Periquito", "Oso"]
print(filtrar_mascotas(mascotas))

# %%
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# 1. Crear excepción personalizada
class ListaVaciaError(Exception):
    pass

# 2. Función
def calcular_promedio(numeros):
    """
    Función que calcula el promedio de una lista de números.

    Args:
        numeros (list): lista de números

    Returns:
        float: promedio de la lista
    """
    
    if len(numeros) == 0:
        raise ListaVaciaError("La lista está vacía")
    
    return sum(numeros) / len(numeros)

# 3. Manejo del error
def ejecutar():
    try:
        lista = []  # prueba cambiando esto
        resultado = calcular_promedio(lista)
        print("Promedio:", resultado)
    
    except ListaVaciaError as e:
        print("Error:", e)

# %%
lista = [5, 10, 15]
print(calcular_promedio(lista))

# %%
lista = []
print(calcular_promedio(lista))

# %%
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    """
    Programa que solicita la edad y valida errores.
    """
    
    try:
        edad = int(input("Introduce tu edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango válido")
        
        print("Edad válida:", edad)
    
    except ValueError as e:
        print("Error:", e)


# %%
pedir_edad()

# %%
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    """
    Función que devuelve la longitud de cada palabra en una frase.

    Args:
        frase (str): frase de entrada

    Returns:
        list: lista con la longitud de cada palabra
    """
    

    
    palabras = frase.split()
    return list(map(lambda palabra: len(palabra), palabras))

# %%
frase = "hola mundo python"
print(longitud_palabras(frase))

# %%
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def letras_mayus_minus(caracteres):
    """
    Función que devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas.

    Args:
        caracteres (str o list): conjunto de caracteres

    Returns:
        list: lista de tuplas (mayúscula, minúscula)
    """
    
    # eliminar repetidos
    sin_repetidos = set(caracteres)
    
    return list(map(lambda letra: (letra.upper(), letra.lower()), sin_repetidos))

# %%
print(letras_mayus_minus("gato"))

# %%
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_letra(lista_palabras, letra):
    """
    Función que retorne las palabras de una lista de palabras que comience con una letra en especifico

    Args:
        lista_palabras (list): lista de palabras
        letra (str): letra inicial

    Returns:
        list: palabras que empiezan por esa letra
    """
       
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

# %%
print(filtrar_por_letra(["casa", "chocolate", "calabacin", "fresa"], "c"))

# %%
# 15. Crea una función lambda que  sume 3 a cada número de una lista dada

def suma_tres(lista):
    """
    Función que suma 3 a cada número de una lista.

    Args:
        lista (list): lista de números

    Returns:
        list: lista con la suma de 3 para cada elemento
    """
    
    return list(map(lambda x: x + 3, lista))

# %%
lista = [9, 1, 5]
print(suma_tres(lista))

# %%
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto, n):
    """
    Función que devuelve las palabras con longitud mayor que n.

    Args:
        texto (str): cadena de texto
        n (int): longitud mínima

    Returns:
        list: palabras más largas que n
    """
    
    palabras = texto.split()
    
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# %%
print(palabras_largas("bienvenido a casa", 3))

# %%
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos [572]. Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    """
    Función que convierte una lista de dígitos en un número.

    Args:
        digitos (list): lista de números enteros (dígitos)

    Returns:
        int: número formado
    """
    # Multiplico por 10 para desplazar el número y poder añadir el siguiente dígito
    return reduce(lambda x, y: x * 10 + y, digitos)

# %%
print(lista_a_numero([3, 4, 5]))

# %%
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def filtrar_estudiantes(estudiantes):
    """
    Función que filtra estudiantes con calificación mayor o igual a 90.

    Args:
        estudiantes (list): lista de diccionarios con datos de estudiantes

    Returns:
        list: estudiantes con calificación >= 90
    """
    
    return list(filter(lambda x: x["calificacion"] >= 90, estudiantes))

# %%
estudiantes = [
    {"nombre": "Sofia", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 82},
    {"nombre": "Marta", "edad": 19, "calificacion": 91},
    {"nombre": "Pepe", "edad": 23, "calificacion": 75}
]

print(filtrar_estudiantes(estudiantes))

# %%
# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# %%
numeros = [1, 2, 3, 4, 5, 6]
print(filtrar_impares(numeros))

# %%
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    """
    Función que devuelve solo los valores tipo integer de una lista.

    Args:
        lista (list): lista con diferentes tipos

    Returns:
        list: lista solo con integers
    """
    
    return list(filter(lambda x: isinstance(x, int), lista))

# %%
lista_variada = ["coche", 9, "casa", "perro", 10]
print(filtrar_enteros(lista_variada))

# %%
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3
print(cubo(5))

# %%
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce

def producto_total(lista):
    """
    Función que calcula el producto de todos los elementos de una lista.

    Args:
        lista (list): lista de números

    Returns:
        int/float: producto total
    """
    
    return reduce(lambda x, y: x * y, lista)

# %%
lista = [5, 2, 8]
print(producto_total(lista))

# %%
# 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce

def concatenar_palabras(lista):
    """
    Función que concatena una lista de palabras.

    Args:
        lista (list): lista de strings

    Returns:
        str: texto concatenado
    """
    
    return reduce(lambda x, palabra: x + palabra, lista)

# %%
lista = ["casa", "coche", "gato", "cocina"]
print(concatenar_palabras(lista))

# %%
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce

def diferencia_total(lista):
    """
    Función que calcula la diferencia total de una lista de números.

    Args:
        lista (list): lista de números

    Returns:
        int/float: resultado de la resta acumulada
    """
    
    return reduce(lambda x, y: x - y, lista)

# %%
lista = [20, 2.5, 3, 4.5]
print(diferencia_total(lista))

# %%
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada

def contar_caracteres(texto):
    """
    Función que cuenta el número de caracteres en una cadena.

    Args:
        texto (str): cadena de texto

    Returns:
        int: número de caracteres
    """
    
    return len(texto)

# %%
print(contar_caracteres("bienvenido a casa"))

# %%
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b
print(resto(15,2))

# %%
# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    """
    Función que calcula el promedio de una lista de números.

    Args:
        numeros (list): lista de números

    Returns:
        float: promedio de la lista
    """
    
    return sum(numeros) / len(numeros)

# %%
lista = [5, 6, 9, 20, 1, 3]
print(calcular_promedio(lista))

# %%
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Función que devuelve el primer elemento duplicado en una lista.

    Args:
        lista (list): lista de elementos

    Returns:
        elemento duplicado o None si no hay
    """
    
    vistos = set()
    
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    
    return None

# %%
print(primer_duplicado([1, 3, 2, 3, 2, 4]))

# %%
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    """
    Función que enmascara todos los caracteres excepto los últimos 4.

    Args:
        valor: cualquier tipo de dato

    Returns:
        str: cadena enmascarada
    """
    
    texto = str(valor)
    
    # Genera tantos # como caracteres menos 4 y ensena solo los últimos 4
    return "#" * (len(texto) - 4) + texto[-4:]

# %%
print(enmascarar("cocacola"))

# %%
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Función que comprueba si dos palabras son anagramas.

    Args:
        palabra1 (str): primera palabra
        palabra2 (str): segunda palabra

    Returns:
        bool: True si son anagramas, False si no
    """
    
    return sorted(palabra1) == sorted(palabra2)

# %%
print(son_anagramas("roma", "amor"))
print(son_anagramas("hola", "casa"))

# %%
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    """
    Función que solicita una lista de nombres al usuario y busca un nombre específico.

    Args:
        None

    Returns:
        Un mensaje indicando que fue encontrado o de lo contrario una excepción
    """
    
    try:
        nombres = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = nombres.split(",")
        
        nombre_buscar = input("Introduce el nombre a buscar: ")
        
        if nombre_buscar in lista_nombres:
            print("El nombre fue encontrado.")
        else:
            raise ValueError("El nombre no está en la lista.")
    
    except ValueError as e:
        print("Error:", e)

# %%
buscar_nombre()

# %%
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre, lista_empleados):
    """
    Función que busca un empleado y devuelve su puesto.

    Args:
        nombre (str): nombre completo del empleado
        lista_empleados (list): lista de diccionarios con empleados

    Returns:
        str: puesto del empleado o mensaje si no se encuentra
    """
    
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    
    return "La persona no trabaja aquí."

# %%
empleados = [
    {"nombre": "Ana García", "puesto": "Enfermera"},
    {"nombre": "Raquel Gonzalez", "puesto": "Developer"},
    {"nombre": "Iago Alvarez", "puesto": "Ingeniero"}
]

print(buscar_empleado("Raquel Gonzalez", empleados))
print(buscar_empleado("Pepe Pérez", empleados))

# %%
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# %%
lista1 = [3, 4, 5]
lista2 = [1, 8, 7]
print(sumar_listas(lista1, lista2))

# %%
# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.

# Crear la clase
class Arbol:

# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []

# 2. Método crecer_tronco para aumentar la longitud del tronco en una unidad
    def crecer_tronco(self):
        self.tronco += 1

# 3. Método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas
    def nueva_rama(self):
        self.ramas.append(1)

# 4. Método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes
    def crecer_ramas(self):
        for rama in range(len(self.ramas)):
            self.ramas[rama] += 1

# 5. Método quitar_rama para eliminar una rama en una posición específica
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

# 6. Método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas
    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "ramas": self.ramas
        }

# %%
# Caso de uso

arbol = Arbol()

arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(1)

print(arbol.info_arbol())

# %%
# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo

# Crear la clase
class UsuarioBanco:

# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

# 3.  Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
        else:
            print("Saldo insuficiente para transferir")

# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# %%
# Caso de uso:
    # Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    # Agregar 20 unidades de saldo de "Bob".
    # Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    # Retirar 50 unidades de saldo a "Alicia".

usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

usuario2.agregar_dinero(20)
usuario2.transferir_dinero(usuario1, 80)
usuario1.retirar_dinero(50)

print(usuario1.nombre, usuario1.saldo)
print(usuario2.nombre, usuario2.saldo) 

# %%
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

# Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    return contador

# Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# Crear una funcion eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return " ".join(palabras)

# Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
def procesar_texto(texto, opcion, *args):
    """
    Función que procesa texto según la opción indicada.

    Args:
        texto (str): texto a procesar
        opcion (str): "contar", "reemplazar" o "eliminar"
        *args: argumentos extra según la opción

    Returns:
        resultado del procesamiento
    """
    
    if opcion == "contar":
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    
    else:
        return "Opción no válida"


# %%
texto = "bienvenido a casa bienvenido a nuestro hogar"

# contar
print(procesar_texto(texto, "contar"))

# reemplazar
print(procesar_texto(texto, "reemplazar", "bienvenido", "welcome"))

# eliminar
print(procesar_texto(texto, "eliminar", "bienvenido"))

# %%
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

def momento_del_dia():
    """
    Programa que indica si es mañana, tarde o noche según la hora.
    """
    
    hora = int(input("Introduce la hora (0-23): "))
    
    if 6 <= hora < 12:
        print("Es de día")
    elif 12 <= hora < 20:
        print("Es por la tarde")
    elif 0 <= hora < 6 or 20 <= hora <= 23:
        print("Es de noche")
    else:
        print("Hora no válida")

# %%
momento_del_dia()

# %%
momento_del_dia()

# %%
momento_del_dia()

# %%
# 39.  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_texto():
    """
    Programa que convierte una nota numérica en texto.
    """
    
    nota = int(input("Introduce la calificación (0-100): "))
    
    if 0 <= nota <= 69:
        print("insuficiente")
    elif 70 <= nota <= 79:
        print("bien")
    elif 80 <= nota <= 89:
        print("muy bien")
    elif 90 <= nota <= 100:
        print("excelente")
    else:
        print("Nota no válida")

# %%
calificacion_texto()

# %%
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo"), y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """
    Función que calcula el área de una figura.

    Args:
        figura (str): tipo de figura
        datos (tuple): datos necesarios

    Returns:
        float: área calculada
    """
    
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        (radio) = datos
        return math.pi * radio**2
    
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    
    else:
        return "Figura no válida"

# %%
print(calcular_area("rectangulo", (4, 5)))
print(calcular_area("circulo", (3)))
print(calcular_area("triangulo", (4, 6)))

# %%
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_precio_final():
    """
    Programa que calcula el precio final con o sin descuento.
    """
    
    precio = float(input("Introduce el precio original: "))
    
    cupon = input("¿Tienes cupón de descuento? (si/no): ").lower()
    
    if cupon == "si":
        descuento = float(input("Introduce el valor del cupón: "))
        
        if descuento > 0:
            precio_final = precio - descuento
            
            if precio_final < 0:
                precio_final = 0  # evita precios negativos
            
            print("Precio final:", precio_final)
        
        else:
            print("Cupón no válido. Precio final:", precio)
    
    elif cupon == "no":
        print("Precio final:", precio)
    
    else:
        print("Respuesta no válida")

# %%
calcular_precio_final()


