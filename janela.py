import turtle

window = turtle.Screen()
window.bgcolor("yellow")
window.title("Para o amor da minha via, Day!")


pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.pensize(2)
pen.speed(9)

pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()


pen.up()
pen.goto(0, -50)
pen.down()
pen.color("black")
pen.write("Meu amor, eu amo você! Amo tanto que aprendi a programar em Pyhton. Agora bora comer um lanchinho? Tenho 50 conto.",
          align="center", font=("Arial", 16, "bold"))


pen.hideturtle()

turtle.done()

