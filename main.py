import turtle
import time
from turtle import Vec2D

trt = turtle.Turtle()
wn = turtle.Screen()

# wn.bgpic("jokah_ccexpress.gif")
wn.bgcolor("black")
wn.setup(400, 290)

trt.color("white")

trt.penup()
trt.goto(-148, 111)
trt.write("It takes a while to get to the final. \n It'll get there, though, I promise.")


# finds position of a point in order to make the Bézier curves easier
def buttonclick(x,y):
    print(f"({x}, {y})")

# defines the quadratic Bézier curve
def quadBeCurve(p0x, p0y, p1x, p1y, p2x, p2y, interval=0.1):

  p0 = Vec2D(p0x, p0y)
  p1 = Vec2D(p1x, p1y)
  p2 = Vec2D(p2x, p2y)

  b = lambda t: p1 + (1 - t)**2 * (p0 - p1) + t**2 * (p2 - p1)

  trt.penup()

  trt.goto((p0x, p0y))

  trt.pendown()

  t = 0

  while t <= 1:
      position = b(t)

      trt.setheading(trt.towards(position))
      trt.goto(position)

      t += interval

# defines cubic Bézier curve
def cubeBeCurve(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, interval=0.1):

  p0 = Vec2D(p0x, p0y)
  p1 = Vec2D(p1x, p1y)
  p2 = Vec2D(p2x, p2y)
  p3 = Vec2D(p3x, p3y)

  b = lambda t: (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

  trt.penup()

  trt.goto((p0x, p0y))

  trt.pendown()

  t = 0

  while t <= 1:
      position = b(t)

      trt.setheading(trt.towards(position))
      trt.goto(position)

      t += interval

def gotodot(posx, posy, size=2):
  trt.penup()
  trt.goto(posx, posy)
  trt.dot(size)
  trt.pendown()

# "binds" butotnclick to the window
turtle.onscreenclick(buttonclick, 1)

"""Frame"""

trt.speed(1)
trt.pensize(2)

trt.penup()
trt.goto(0,108)
trt.seth(0)
trt.pendown()
trt.fd(162)
trt.right(90)
trt.fd(217)
trt.right(90)
trt.fd(325)
trt.right(90)
trt.fd(217)
trt.right(90)
trt.fd(163)

"""Major Features"""

trt.ht()
trt.speed(0)

# right shoulder
trt.color("steel blue")
trt.penup()
trt.goto(-61, 60)
trt.pendown()
trt.goto(-76, 50)
quadBeCurve(-96, 42, -116, 39, -108, 2)

# right arm
cubeBeCurve(-108, 4, -103, -6, -113, -24, -107, -33)
trt.goto(-104, -56)
cubeBeCurve(-104, -56, -107, -64, -97, -73, -101, -88)
trt.goto(-97, -95)
quadBeCurve(-61, -98, -65, -97, -61, -92)
quadBeCurve(-61, -92, -72, -86, -73, -75)
quadBeCurve(-73, -75, -79, -68, -75, -40)
trt.goto(-76, -3)

# left shoulder
trt.penup()
trt.goto(-19, 61)
trt.pendown()
trt.goto(8, 44)
quadBeCurve(8, 44, 36, 31, 32, -9)

# left arm
quadBeCurve(32, -7, 33, -41, 25, -55)
quadBeCurve(25, -55, 22, -62, 23, -76)
cubeBeCurve(23, -76, 23, -82, 14, -88, 12, -94)
quadBeCurve(-23, -97, -19, -85, -12, -79)
cubeBeCurve(-12, -79, -13, -67, -1, -63, -7, -54)
quadBeCurve(-7, -54, -7, -30, 5, -12)
trt.goto(5, 2)

# head 
trt.color("white")
quadBeCurve(-19, 61, -17, 65, -18, 69)
quadBeCurve(-18, 69, -15, 73, -15, 78)
quadBeCurve(-15, 78, -17, 79, -19, 80)

quadBeCurve(-19, 80, -20, 97, -26, 99)
quadBeCurve(-26, 99, -35, 87, -51, 95)
quadBeCurve(-51, 95, -57, 101, -49, 109)
quadBeCurve(-49, 109, -67, 102, -63, 77)
cubeBeCurve(-63, 77, -66, 71, -57, 64, -59, 56)
quadBeCurve(-59, 56, -47, 37, -38, 40)

trt.color("green")
trt.pensize(1)
quadBeCurve(-19, 80, -20, 97, -26, 99)
quadBeCurve(-26, 99, -35, 87, -51, 95)
quadBeCurve(-51, 95, -57, 101, -49, 109)
quadBeCurve(-49, 109, -67, 102, -63, 77)

trt.color("white")
trt.pensize(2)
quadBeCurve(-38, 40, -29, 39, -19, 61)


cubeBeCurve(-32, 41, -35, 29, -50, 30, -50, 44)

# hair
trt.color("green")
quadBeCurve(-7, 80, -8, 73, -15, 69)
quadBeCurve(-7, 79, 1, 96, -11, 106, 0.05)
trt.goto(-7, 108)
trt.goto(-65, 108)
quadBeCurve(-65, 108, -78, 94, -64, 73, 0.05)

# bars
trt.color("#4F4949")
trt.penup()
trt.goto(-162, -95)
trt.pendown()
trt.goto(-96, -95)
trt.goto(-96, 107)
trt.penup()
trt.goto(-78, 107)
trt.pendown()
trt.goto(-78, -95) 
trt.goto(44, -95)
trt.goto(44, 107)
trt.penup()
trt.goto(57, 107)
trt.pendown()
trt.goto(57, -95)
trt.goto(112, -95)
trt.goto(112, 107)
trt.penup()
trt.goto(128, 107)
trt.pendown()
trt.goto(128, -95)
trt.goto(163, -95)
trt.end_fill()


"""Minor Features"""

trt.pensize(1)

"clothes"

# green vest seams
trt.color("forestgreen")
trt.penup()
trt.goto(5, 2)
trt.pendown()
trt.goto(7, 40)

quadBeCurve(-75, -2, -80, 23, -76, 41)
quadBeCurve(7, 40, -4, 48, -15, 47)
quadBeCurve(-62, 46, -75, 47, -78, 41)

trt.penup()
trt.goto(-22, 34)
trt.pendown()
trt.goto(-34, -7)
trt.goto(-45, -20)
trt.goto(-45, -36)

quadBeCurve(-45, -20, -18, -2, -6, 22)
quadBeCurve(-6, 22, -5, 30, -10, 36)
quadBeCurve(-12, 40, -8, 40, -6, 38)
quadBeCurve(-6, 38, -2, 40, -4, 45)
quadBeCurve(-45, -36, -42, -46, -47, -57)

trt.goto(-46, -94)

gotodot(-42, -60)
gotodot(-42, -76)
gotodot(-39, -43)

quadBeCurve(-45, -18, -59, 2, -57, 37)
quadBeCurve(-45, -18, -71, 9, -70, 28)
quadBeCurve(-70, 28, -69, 37, -62, 38)
quadBeCurve(-70, 45, -71, 38, -62, 38)
quadBeCurve(-23, -60, -15, -59, -8, -63)
quadBeCurve(-23, -60, -27, -72, -11, -73)
quadBeCurve(-23, -59, -13, -57, -6, -62)


# blue shirt seams
trt.color("steel blue")
quadBeCurve(-19, 56, -10, 37, -10, 23)
quadBeCurve(-10, 23, -18, 37, -32, 40)
quadBeCurve(-59, 56, -63, 46, -62, 30)
quadBeCurve(-62, 30, -57, 40, -51, 41)

# tie
trt.color("dark olive green")
quadBeCurve(-33, -6, -32, 10, -36, 24)
quadBeCurve(-36, 24, -33, 33, -34, 32)
quadBeCurve(-48, -8, -50, 7, -49, 23)
quadBeCurve(-49, 23, -53, 28, -51, 35)
quadBeCurve(-51, 35, -45, 30, -34, 32)
quadBeCurve(-36, 24, -42, 20, -49, 23)
quadBeCurve(-33, 30, -29, 32, -27, 37)
quadBeCurve(-51, 32, -54, 35, -54, 39)

# green vest wrinkles
trt.color("dark green")
quadBeCurve(-22, -19, -12, -5, 5, -7)
quadBeCurve(-18, -41, -10, -41, -4, -32)
quadBeCurve(-32, -56, -22, -46, -6, -43)
quadBeCurve(-45, -55, -61, -49, -67, -31)
quadBeCurve(-37, -81, -35, -85, -28, -84)
quadBeCurve(-15, -25, -8, -20, 0, -20)
quadBeCurve(-64, -55, -59, -52, -46, -54)
quadBeCurve(-56, -21, -65, -15, -68, -4)

# blue shirt wrinkles
trt.color("dark slate gray")
quadBeCurve(7, 11, 18, 26, 23, 24)
quadBeCurve(7, -6, 22, -3, 28, 10)
quadBeCurve(4, -35, 26, -8, 30, 3)
quadBeCurve(11, 0, 23, 7, 27, 16)
quadBeCurve(15, -43, 23, -36, 26, -22)
quadBeCurve(-1, -45, 5, -42, 9, -44)
quadBeCurve(4, -57, 12, -54, 19, -62)
quadBeCurve(-13, -86, -2, -82, 12, -88)
quadBeCurve(1, -71, 13, -68, 17, -76)
quadBeCurve(7, -65, 12, -68, 17, -68)
quadBeCurve(13, 43, 7, 38, 15, 33)
cubeBeCurve(-108, 31, -106, 23, -99, 25, -99, 19)
quadBeCurve(-65, -89, -69, -91, -73, -88)
cubeBeCurve(-2, -82, 5, -76, 16, -85, 20, -74)
quadBeCurve(-105, -34, -100, -36, -98, -43)


"face"

# smile
trt.speed(0)
trt.color("darkred")
quadBeCurve(-22, 64, -28, 50, -40, 51)
quadBeCurve(-40, 51, -53, 51, -58, 64)
quadBeCurve(-58, 64, -55, 55, -48, 49)
cubeBeCurve(-48, 49, -35, 45, -42, 45, -35, 49)
quadBeCurve(-35, 49, -28, 46, -22, 64)
quadBeCurve(-46, 50, -38, 47, -30, 51)
quadBeCurve(-46, 51, -50, 52, -49, 48)
quadBeCurve(-33, 51, -29, 50, -29, 48)

# nose
trt.color("white")
quadBeCurve(-43, 72, -41, 61, -46, 58)
quadBeCurve(-39, 54, -43, 55, -46, 58)
quadBeCurve(-39, 54, -34, 58, -35, 59)
quadBeCurve(-35, 59, -39, 61, -39, 67)

# left eye
trt.begin_fill()
quadBeCurve(-35, 72, -32, 69, -29, 72)
quadBeCurve(-35, 72, -32, 72, -31, 75)
quadBeCurve(-29, 72, -27, 75, -31, 75)
trt.end_fill()

gotodot(-30, 73)
gotodot(-50, 72, 3)

trt.color("black")
gotodot(-31, 74, 3)
gotodot(-32, 74, 3)

trt.color("white")
quadBeCurve(-39, 71, -30, 80, -24, 74)
quadBeCurve(-24, 74, -31, 64, -39, 71)

# right eye
quadBeCurve(-46, 71, -51, 70, -52, 71)
quadBeCurve(-51, 71, -49, 73, -46, 71)

gotodot(-52, 72)

trt.color("black")
gotodot(-49, 73, 3)

trt.color("white")
quadBeCurve(-43, 69, -51, 83, -58, 73)
quadBeCurve(-58, 73, -56, 62, -43, 69)


# face wrinkles
quadBeCurve(-37, 70, -34, 66, -22, 64)
quadBeCurve(-48, 58, -44, 62, -44, 67)
quadBeCurve(-27, 56, -32, 56, -36, 63)
cubeBeCurve(-56, 83, -44, 79, -39, 86, -32, 82)
cubeBeCurve(-49, 88, -45, 88, -39, 84, -35, 86)

# hair details
trt.color("green")
quadBeCurve(-26, 101, -23, 105, -28, 108)
quadBeCurve(-23, 105, -12, 104, -6, 100)
quadBeCurve(-8, 79, -2, 79, -1, 82)
quadBeCurve(-25, 104, -19, 101, -15, 96)
quadBeCurve(-76, 93, -71, 92, -70, 100)
quadBeCurve(-64, 74, -64, 67, -67, 65)
quadBeCurve(-67, 65, -63, 64, -61, 66)


"""Frame redraw"""

trt.color("white")

trt.speed(0)
trt.pensize(2)

trt.penup()
trt.goto(0,108)
trt.seth(0)
trt.pendown()
trt.fd(162)
trt.right(90)
trt.fd(217)
trt.right(90)
trt.fd(325)
trt.right(90)
trt.fd(217)
trt.right(90)
trt.fd(163)

"dots"
trt.color("black")
gotodot(-62, -98, 5)
gotodot(-23, -98, 5)
gotodot(-48, 112)
gotodot(164, -94)

trt.color("black")
trt.penup()
trt.goto(-150, 113)
trt.begin_fill()
trt.goto(-154, 140)
trt.goto(41, 136)
trt.goto(42, 112)
trt.end_fill()

trt.color("white")
trt.penup()
trt.goto(-148, 111)
trt.write("Done!")

time.sleep(2)

trt.color("black")
trt.penup()
trt.goto(-150, 113)
trt.begin_fill()
trt.goto(-154, 140)
trt.goto(41, 136)
trt.goto(42, 112)
trt.end_fill()