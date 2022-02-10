from turtle import Turtle, Screen
from random import randint


wn = Screen()
wn.bgcolor('blue')
wn.screensize(2000)
wn.register_shape('monee.gif')
wn.register_shape('metor.gif')
wn.register_shape('ship.gif')


import brown
import red
import orange

us = Turtle()
us.speed(0)
us.penup()
us.setheading(90)
us.setpos(0,0)
us.shape('ship.gif')

meteor = Turtle()
meteor.speed(0)
meteor.color('black')
meteor.penup()
meteor.setheading(-90)
meteor.setpos(randint(-100,100),150)
meteor.shape('metor.gif')

meteor2 = Turtle()
meteor2.speed(0)
meteor2.color('black')
meteor2.penup()
meteor2.setheading(-90)
meteor2.setpos(randint(-100,100),150)
meteor2.shape('metor.gif')

energy = Turtle()
energy.speed(0)
energy.penup()
energy.setheading(-90)
energy.setpos(randint(-100,100),150)
energy.shape('monee.gif')




energy2 = Turtle()
energy2.speed(0)
energy2.color('green')
energy2.penup()
energy2.setheading(-90)
energy2.setpos(randint(-100,100),150)
energy2.shape('monee.gif')

energy3 = Turtle()
energy3.speed(0)
energy3.color('green')
energy3.penup()
energy3.setheading(-90)
energy3.setpos(randint(-100,100),150)
energy3.shape('monee.gif')

energy4 = Turtle()
energy4.speed(0)
energy4.color('green')
energy4.penup()
energy4.setheading(-90)
energy4.setpos(randint(-100,100),150)
energy4.shape('monee.gif')

score = 0
m_speed = 1





going = True
while going == True:

  wn.onkey(lambda: us.left(90), 'Left')
  wn.onkey(lambda: us.right(90), 'Right')
  wn.onkey(lambda: us.forward(10), 'Up') 
  wn.onkey(lambda: us.forward(-10), 'Down')
    
  x_corr_good = us.xcor()
  if int(x_corr_good) <= -140: 
    print('You are out of bounds')
    us.setpos(0,0)

  x_corr_good = us.xcor()
  if int(x_corr_good) >= 160: 
    print('You are out of bounds')
    us.setpos(0,0)



  y_corr_good = us.ycor()
  if int(y_corr_good) <= -160: 
    print('You are out of bounds')
    us.setpos(0,0)

  y_corr_good = us.ycor()
  if int(y_corr_good) >= 160: 
    print('You are out of bounds')
    us.setpos(0,0)

  meteor.setpos(meteor.xcor(), meteor.ycor() - m_speed)
  meteor2.setpos(meteor2.xcor(), meteor2.ycor() -    
  m_speed)
  energy.setpos(energy.xcor(), energy.ycor() - 1)
  energy2.setpos(energy2.xcor(), energy2.ycor() - 1)
  energy3.setpos(energy3.xcor(), energy3.ycor() - 1)
  energy4.setpos(energy4.xcor(), energy4.ycor() - 1)



  usx = us.xcor()
  usy = us.ycor()
  meteorx = meteor.xcor()
  meteory = meteor.ycor()
  meteorx2 = meteor2.xcor()
  meteory2 = meteor2.ycor()
  energyx = energy.xcor()
  energyy = energy.ycor()
  energyx2 = energy2.xcor()
  energyy2 = energy2.ycor()
  energyx3 = energy3.xcor()
  energyy3 = energy3.ycor()
  energyx4 = energy4.xcor()
  energyy4 = energy4.ycor()



  if int(meteory) < -100:
	  meteor.setpos(randint(-100,100),150)

  if int(meteory2) < -100:
	  meteor2.setpos(randint(-100,100),150)

  if int(energyy) < -100:
	  energy.setpos(randint(-100,100),150)

  
  if int(energyy2) < -100:
	  energy2.setpos(randint(-100,100),150)


  if int(energyy3) < -100:
	  energy3.setpos(randint(-100,100),150)


  if int(energyy4) < -100:
	  energy4.setpos(randint(-100,100),150)



  if int(usx) > int(meteorx - 10) and int(usx) < int(meteorx + 10) and \
  int(usy) > int(meteory - 10) and int(usy) < int(meteory + 10):
    print('Your time has come')
    us.hideturtle()
    us.setpos(199,99)

  if int(usx) > int(meteorx2 - 10) and int(usx) < int(meteorx2 + 10) and \
  int(usy) > int(meteory2 - 10) and int(usy) < int(meteory2 + 10):
    print('Your time has come')
    us.hideturtle()
    us.setpos(199,99)





  if int(usx) > int(energyx - 10) and int(usx) < int(energyx + 10) and \
  int(usy) > int(energyy - 10) and int(usy) < int(energyy + 10):
    score += 1
    m_speed += 1
    energy.setpos(randint(-100,100),150)
    print(score)

  if int(usx) > int(energyx2 - 10) and int(usx) < int(energyx2 + 10) and \
  int(usy) > int(energyy2 - 10) and int(usy) < int(energyy2 + 10):
    score += 1
    m_speed += 1
    energy2.setpos(randint(-100,100),150)
    print(score)

  if int(usx) > int(energyx3 - 10) and int(usx) < int(energyx3 + 10) and \
  int(usy) > int(energyy3 - 10) and int(usy) < int(energyy3 + 10):
    score += 1
    m_speed += 1
    energy3.setpos(randint(-100,100),150)
    print(score)


  if int(usx) > int(energyx4 - 10) and int(usx) < int(energyx4 + 10) and \
  int(usy) > int(energyy4 - 10) and int(usy) < int(energyy4 + 10):
    score += 1
    m_speed += 1
    energy4.setpos(randint(-100,100),150)
    print(score)



  wn.listen()


wn.mainloop()


