def adivinacion(array1, array2, array3, personajes):
    k = 3  # variable para revolver 3 veces
    while k > 0:
        array1 = []
        array2 = []
        array3 = []

        for i, personaje in enumerate(personajes):
            if i % 3 == 0:
                array1.append(personaje)
            elif i % 3 == 1:
                array2.append(personaje)
            else:
                array3.append(personaje)

        print("Lista 1: ", array1)
        print("Lista 2: ", array2)
        print("Lista 3: ", array3)

        pos = input("En qué lista se encuentra el personaje? (1, 2 o 3): ")
        if pos == "1":
            personajes = array2 + array1 + array3
        elif pos == "2":
            personajes = array1 + array2 + array3
        elif pos == "3":
            personajes = array1 + array3 + array2

        k -= 1

    return personajes[10]

# Lista de 21 personajes de Yu-Gi-Oh!
personajes_yugioh = [
    "Yugi Muto", "Seto Kaiba", "Joey Wheeler", "Jaden Yuki", "Yusei Fudo",
    "Yuma Tsukumo", "Yuya Sakaki", "Playmaker (Varis)", "Atem", "Pegasus",
    "Bakura", "Marik", "Chazz Princeton", "Aster Phoenix", "Jack Atlas",
    "Akiza Izinski", "Yusei Fudo", "Yuma Tsukumo", "Yuya Sakaki",
    "Revolver (Varis)", "Yusaku Fujiki"
]

print(personajes_yugioh)
print("Piensa en un personaje de Yu-Gi-Oh!... ")
array1 = []
array2 = []
array3 = []
print("El personaje que pensaste es:", adivinacion(array1, array2, array3, personajes_yugioh))
