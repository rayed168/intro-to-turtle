import turtle as tt

tt.Screen().bgcolor("Blue")
screen=tt.Screen()
screen.setup(500,300)
screen.title("My first turtle program")

cursor=tt.Turtle()
cursor.speed(50)
sides=int(input("Enter the amount of sides your shape has : "))
angle=360/sides

while sides:
    tt.forward(50)
    tt.right(angle)
    sides-=1
tt.done()    