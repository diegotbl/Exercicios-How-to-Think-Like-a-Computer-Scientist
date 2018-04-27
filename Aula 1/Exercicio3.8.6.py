import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Exercicio 3.8.6")

tortuguita = turtle.Turtle()
tortuguita.shape("turtle")
tortuguita.speed(3)   # Reduzindo a velocidade da tartaruga

size = 100
# Item a
tortuguita.color("green")
for i in range(3):
    tortuguita.forward(size)
    tortuguita.left(120)

# Item b
tortuguita.color("blue")
for i in range(4):
    tortuguita.forward(size)
    tortuguita.left(90)

# Item c
tortuguita.color("red")
for i in range(6):
    tortuguita.forward(size)
    tortuguita.left(60)

# Item d
tortuguita.color("black")
for i in range(8):
    tortuguita.forward(size)
    tortuguita.left(45)

window.mainloop()
