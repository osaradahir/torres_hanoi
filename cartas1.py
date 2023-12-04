from collections import deque

def adivinacion(queue1, queue2, queue3, personajes):
    k = 3  # variable para revolver 3 veces
    while k > 0:
        queue1.clear()
        queue2.clear()
        queue3.clear()

        for i, personaje in enumerate(personajes):
            if i % 3 == 0:
                queue1.appendleft(personaje)
            elif i % 3 == 1:
                queue2.appendleft(personaje)
            else:
                queue3.appendleft(personaje)

        print("Cola 1: ", list(queue1))
        print("Cola 2: ", list(queue2))
        print("Cola 3: ", list(queue3))

        pos = input("En qué cola se encuentra el personaje? (1, 2 o 3): ")
        if pos == "1":
            personajes = list(queue2) + list(queue1) + list(queue3)
        elif pos == "2":
            personajes = list(queue1) + list(queue2) + list(queue3)
        elif pos == "3":
            personajes = list(queue1) + list(queue3) + list(queue2)

        k -= 1

    return personajes[10]
personajes_anime = [
    "Monkey D. Luffy", "Naruto Uzumaki", "Goku", "Edward Elric", "Spike Spiegel",
    "Light Yagami", "Lelouch vi Britannia", "Natsu Dragneel", "Gon Freecss", "Saitama",
    "Ichigo Kurosaki", "Eren Yeager", "Vegeta", "Inuyasha", "Kakashi Hatake",
    "Ryuko Matoi", "Mikasa Ackerman", "Levi Ackerman", "Killua Zoldyck",
    "Homura Akemi", "Sasuke Uchiha"
]

print(personajes_anime)
print("Piensa en un personaje famoso de anime... ")
queue1 = deque()
queue2 = deque()
queue3 = deque()
print("El personaje que pensaste es:", adivinacion(queue1, queue2, queue3, personajes_anime))
