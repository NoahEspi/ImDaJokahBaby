import turtle
from turtle import Vec2D

trt = turtle.Turtle()
wn = turtle.Screen()

wn.bgpic("jokah_ccexpress.gif")
wn.bgcolor("black")

trt.speed(0)

trt.ht()

trt.color("white")

# finds position of a point in order to make the Bézier curves easier
def buttonclick(x,y):
    print(f"({x}, {y})")

# defines the quadratic Bézier curve
def quadBeCurve(p0x, p0y, p1x, p1y, p2x, p2y):

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

      t += 0.05

# defines cubic Bézier curve
def cubeBeCurve(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y):

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

      t += 0.05

# "binds" butotnclick to the window
turtle.onscreenclick(buttonclick, 1)

# right shoulder
trt.pensize(2)
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
quadBeCurve(-61, -92, -72, -86, -71, -75)
quadBeCurve(-69, -73, -79, -68, -75, -40)
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
cubeBeCurve(23, -76, 18, -82, 22, -92, 17, -95)
quadBeCurve(-23, -97, -19, -85, -12, -79)
cubeBeCurve(-12, -79, -13, -67, -1, -63, -7, -54)
quadBeCurve(-7, -54, -7, -30, 5, -12)
trt.goto(5, 2)