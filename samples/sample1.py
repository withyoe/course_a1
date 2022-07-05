import turtle

colors=['red','violet','blue','cyan','yellow','green','pink','brown','turquoise','purple']

t=turtle.Pen()

turtle.bgcolor('blue')

for x in range(100):
    t.pencolor(colors[x%len(colors)])
    t.forward(x)
    t.left(90)