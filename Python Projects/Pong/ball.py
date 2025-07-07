from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white","red")
        self.shape("circle")
        self.penup()
        self.xVel=10
        self.yVel=10

    def move(self):
        x=self.xcor()+self.xVel
        y=self.ycor()+self.yVel
        self.goto(x,y)

    def bounce(self):
        self.yVel=self.yVel*-1

    def hit(self):
        self.xVel=self.xVel*-1
        if(self.xVel>0):
            self.xVel+=2
        else:
            self.xVel-=2
        if(self.yVel>0):
            self.yVel+=2
        else:
            self.yVel-=2

    def reset_pos(self):
        if(self.xVel>0):
            self.xVel=-10
        else:
            self.xVel=10
        if(self.yVel>0):
            self.yVel=10
        else:
            self.yVel=-10
        
        self.goto(0,0)