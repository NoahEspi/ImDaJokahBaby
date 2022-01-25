import turtle
from turtle import Vec2D

trt = turtle.Turtle()
wn = turtle.Screen()

# wn.bgpic("jokah_ccexpress.gif")
wn.bgcolor("black")


trt.color("white")

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
quadBeCurve(-19, 61, -17, 65, -18, 69)
quadBeCurve(-18, 69, -15, 73, -15, 78)
quadBeCurve(-15, 78, -17, 79, -19, 80)
quadBeCurve(-19, 80, -20, 97, -26, 99)
quadBeCurve(-26, 99, -35, 87, -51, 95)
quadBeCurve(-51, 95, -57, 101, -49, 109)
quadBeCurve(-49, 109, -67, 102, -63, 77)
cubeBeCurve(-63, 77, -66, 71, -57, 64, -59, 56)
quadBeCurve(-59, 56, -47, 37, -38, 40)
quadBeCurve(-38, 40, -29, 39, -19, 61)


cubeBeCurve(-32, 41, -35, 29, -50, 30, -50, 44)

# hair
quadBeCurve(-15, 68, -3, 65, -1, 80, 0.05)
trt.goto(-7, 79)
quadBeCurve(-7, 79, 1, 96, -11, 106, 0.05)
trt.goto(-7, 108)
trt.goto(-65, 108)
quadBeCurve(-65, 108, -78, 94, -64, 73, 0.05)

# bars
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

# dots
trt.color("black")
trt.penup()
trt.goto(-62, -98)
trt.dot()
trt.goto(-23, -98)
trt.dot()
trt.goto(-49, 114)
trt.dot()
trt.goto(165, -95)
trt.dot()



"""Minor Features"""

trt.pensize(1)
trt.color("white")

"clothes"

# green vest seams
trt.penup()
trt.goto(5, 2)
trt.pendown()
trt.goto(7, 40)

quadBeCurve(7, 40, -4, 48, -15, 47)
quadBeCurve(-62, 46, -70, 48, -76, 42)

# green vest wrinkles

# blue shirt seams
quadBeCurve(-19, 56, -10, 37, -10, 23)
quadBeCurve(-10, 23, -18, 37, -32, 40)
quadBeCurve(-59, 56, -63, 46, -62, 30)
quadBeCurve(-62, 30, -57, 40, -51, 41)

# blue shirt wrinkles

# tie


"face"

# smile

# eyes

# makeup around eyes