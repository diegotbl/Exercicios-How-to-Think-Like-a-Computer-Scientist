import turtle

def star(turtle, size):
    """ Faz a tartaruga 'turtle' desenhar uma estrela de lado 'size' """
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

# Testando a função
window = turtle.Screen()
window.title("Exercicio 4.9.9")

tortuguita = turtle.Turtle()
tortuguita.hideturtle()
star(tortuguita, 100)

window.mainloop()
