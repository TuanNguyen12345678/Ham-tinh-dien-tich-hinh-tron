import turtle
import math
def draw():
    r=float(input('nhập vào đường tròn bán kính r: '))
    t=turtle.Turtle()
    t.pensize (5)
    t.pencolor('red')
    t.begin_fill()
    t.fillcolor('blue')
    t.circle(r)
    t.end_fill()
    s=math.pi*r*r
    print('diện tích hình tròn bán kính r = {} là: {} '.format(r,s))
if __name__=="__main__":
    draw()