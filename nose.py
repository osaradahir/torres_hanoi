class Pila:
    def __init__(self):
        # Inicializa una lista vacía para representar la pila
        self.items = []

    def esta_vacia(self):
        # Verifica si la pila está vacía
        return len(self.items) == 0

    def apilar(self, elemento):
        # Agrega un elemento a la pila (al final de la lista)
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            # Elimina y devuelve el elemento en la cima de la pila
            return self.items.pop()
        else:
            print("La pila está vacía. No se puede desapilar.")

    def elemento_en_cima(self):
        if not self.esta_vacia():
            # Devuelve el elemento en la cima de la pila sin eliminarlo
            return self.items[-1]
        else:
            print("La pila está vacía. No hay elementos en la cima.")

    def tamaño(self):
        # Devuelve el tamaño (cantidad de elementos) de la pila
        return len(self.items)

def mostrar_pila(pila):
    if not pila.esta_vacia():
        # Muestra el contenido de la pila (los elementos en la lista)
        print("Contenido de la pila:", pila.items)
    else:
        print("La pila está vacía.")

def main():
    pila = Pila()  # Crea una instancia de la clase Pila
    
    while True:
        print("\nMenú de operaciones:")
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Comprobar si la pila está vacía")
        print("4. Elemento en la cima")
        print("5. Tamaño de la pila")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            elemento = int(input("Ingrese un número para apilar: "))
            pila.apilar(elemento)  # Llama al método apilar de la instancia de Pila
            mostrar_pila(pila)
        elif opcion == '2':
            pila.desapilar()  # Llama al método desapilar de la instancia de Pila
            mostrar_pila(pila)
        elif opcion == '3':
            if pila.esta_vacia():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        elif opcion == '4':
            elemento_cima = pila.elemento_en_cima()  # Llama al método elemento_en_cima de la instancia de Pila
            if elemento_cima is not None:
                print("Elemento en la cima:", elemento_cima)
        elif opcion == '5':
            print("Tamaño de la pila:", pila.tamaño())  # Llama al método tamaño de la instancia de Pila
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()  # Inicia la ejecución del programa
