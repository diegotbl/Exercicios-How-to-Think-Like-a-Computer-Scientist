
import turtle

window = turtle.Screen()
window.title("Exercicio 3.8.11")

tortuguita = turtle.Turtle()
tortuguita.hideturtle()

for i in range(5):
    tortuguita.forward(300)
    tortuguita.right(144)

window.mainloop()
