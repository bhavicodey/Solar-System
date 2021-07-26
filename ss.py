import turtle

area = turtle.Screen()
area.setup(width=650, height=650)
area.bgcolor("black")





tr = turtle.Turtle()

tr.speed(10)


tr.fillcolor('yellow')
tr.begin_fill()
tr.circle(100)
tr.end_fill()

tr.goto(7, -20)
tr.color('white')
tr.circle(200)

tr.color('black')





tr.penup()
tr.goto(7, -22)
tr.pendown()

tr.fillcolor('gray')
tr.begin_fill()
tr.circle(5)
tr.end_fill()


tr.goto(7, -40)
tr.color('white')
tr.circle(300)




tr.color('black')


tr.penup()
tr.goto(7, -42)
tr.pendown()

tr.fillcolor('orange')
tr.begin_fill()
tr.circle(7)
tr.end_fill()





tr.goto(7, -64)
tr.color('white')
tr.circle(400)




tr.color('black')


tr.penup()
tr.goto(6, -72)
tr.pendown()

tr.fillcolor('blue')
tr.begin_fill()
tr.circle(10)
tr.end_fill()

tr.penup()
tr.goto(6, -66)
tr.pendown()

tr.fillcolor('lightgreen')
tr.begin_fill()
for i in range(4):
    tr.forward(5)
    tr.right(90)
tr.end_fill()



tr.goto(7, -94)
tr.color('white')
tr.circle(400)




tr.color('black')

tr.penup()
tr.goto(7, -96)
tr.pendown()

tr.fillcolor('red')
tr.begin_fill()
tr.circle(7)
tr.end_fill()


tr.goto(7, -150)
tr.color('white')
tr.circle(400)


tr.color('black')

tr.penup()
tr.goto(6, -182)
tr.pendown()

tr.fillcolor('#f7e8c3')
tr.begin_fill()
tr.circle(40)
tr.end_fill()

tr.penup()
tr.goto(26, -162)
tr.pendown()

tr.fillcolor('red')
tr.begin_fill()
tr.circle(10)
tr.end_fill()





tr.goto(7, -230)
tr.color('white')
tr.circle(400)


tr.color('black')



tr.penup()
tr.goto(6, -262)
tr.pendown()

tr.fillcolor('#f7e8c3')
tr.begin_fill()
tr.circle(40)
tr.end_fill()


tr.penup()
tr.goto(-15, -252)
tr.pendown()


tr.width(10)
tr.fillcolor('brown')
tr.pencolor('brown')
tr.begin_fill()
  
def draw(rad):
  
  for i in range(2):
      
    # two arcs
    tr.circle(rad,90)
    tr.circle(rad//65,90)
  
draw(55)
tr.end_fill()

tr.width(1)
tr.goto(7, -278)
tr.color('white')
tr.circle(400)


tr.color('black')




tr.penup()
tr.goto(6, -288)
tr.pendown()

tr.fillcolor('cyan')
tr.begin_fill()
tr.circle(10)
tr.end_fill()

tr.goto(7, -298)
tr.color('white')
tr.circle(400)


tr.color('black')

tr.penup()
tr.goto(6, -308)
tr.pendown()

tr.fillcolor('blue')
tr.begin_fill()
tr.circle(10)
tr.end_fill()

turtle.done()
