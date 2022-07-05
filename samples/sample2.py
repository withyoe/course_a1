import turtle

colors=['red','pink','yellow','green','cyan','blue','purple','orange','turquoise','brown','aqua','aquamarine','azure']

t=turtle.Pen()

turtle.bgcolor('black')

for x in range (360):
    t.pencolor(colors[x%len(colors)])
    t.width(x/100+6)
    t.forward(x)
    t.left(60)
    t.forward(x)
    t.left(59)