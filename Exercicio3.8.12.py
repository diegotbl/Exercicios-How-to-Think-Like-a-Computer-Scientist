import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 3.8.12")

tortuguita = turtle.Turtle()
tortuguita.shape("turtle")
tortuguita.color("blue")
tortuguita.pensize(3)

# Definindo algumas distâncias
radius = 200
line = 20
space = 20

tortuguita.penup()
tortuguita.stamp()
for i in range(12):
    tortuguita.forward(radius)
    tortuguita.pendown()
    tortuguita.forward(line)
    tortuguita.penup()
    tortuguita.forward(space)
    tortuguita.stamp()
    tortuguita.backward(radius + line + space)
    tortuguita.right(30)

window.mainloop()
