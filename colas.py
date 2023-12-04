class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        nuevo = Nodo(x)
        if self.ultimo:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo
        self.mostrar_contenido()

    def desencolar(self):
        if self.primero:
            valor = self.primero.dato
            self.primero = self.primero.prox
            if not self.primero:
                self.ultimo = None
            self.mostrar_contenido()
            return valor
        else:
            raise ValueError("La cola está vacía")

    def esta_vacia(self):
        return self.primero is None

    def elemento_enfrente(self):
        if not self.esta_vacia():
            return self.primero.dato
        else:
            print("La cola está vacía. No hay elemento en frente.")

    def tamano(self):
        tam = 0
        actual = self.primero
        while actual:
            tam += 1
            actual = actual.prox
        return tam

    def mostrar_contenido(self):
        actual = self.primero
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.prox
        print("Contenido de la cola:", elementos)

def menu():
    cola = Cola()

    while True:
        print("\nMenú:")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Comprobar si está vacía")
        print("4. Elemento en frente")
        print("5. Tamaño de la cola")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            elemento = int(input("Ingrese el elemento a encolar: "))
            cola.encolar(elemento)
        elif opcion == "2":
            try:
                cola.desencolar()
            except ValueError as e:
                print(e)
        elif opcion == "3":
            if cola.esta_vacia():
                print("La cola está vacía.")
            else:
                print("La cola no está vacía.")
        elif opcion == "4":
            print("Elemento en frente:", cola.elemento_enfrente())
        elif opcion == "5":
            print("Tamaño de la cola:", cola.tamano())
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    menu()
