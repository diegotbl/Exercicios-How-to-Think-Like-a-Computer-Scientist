import turtle

def star(turtle, size):
    """ Faz a tartaruga 'turtle' desenhar uma estrela de lado 'size' """
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 4.9.10")

tortuguita = turtle.Turtle()
tortuguita.color("hotpink")
tortuguita.pensize(3)
# Centralizando a figura
tortuguita.penup()
tortuguita.backward(175)
tortuguita.pendown()

for i in range(5):
    star(tortuguita, 100)
    tortuguita.penup()
    tortuguita.forward(350)
    tortuguita.pendown()
    tortuguita.right(144)

window.mainloop()
