import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(500,500)
turtle.Screen().title("Spiral Pattern")
pen = turtle.Turtle()
pen.color("orange")

size = 0
while True:
    for i in range(4):
        pen.forward(size+1)
        pen.left(90)
        size = size - 5
        
    size = size + 1

turtle.done() 
