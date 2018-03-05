import turtle

window = turtle.Screen()
tortuguita = turtle.Turtle()
tortuguita.hideturtle()
tortuguita.pensize(4)

side = 120

lista = [(270, side), (135, side*(2**0.5)), (135, side), (135, side*(2**0.5)),
(270, side/(2**0.5)), (270, side/(2**0.5)), (225, side), (90, side)]

for (angle, distance) in lista:
    tortuguita.right(angle)
    tortuguita.forward(distance)

window.mainloop()
