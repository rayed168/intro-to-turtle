import turtle as tt

tt.Screen().bgcolor("Blue")

cursor=tt.Turtle()

cursor.forward(100)
cursor.left(120)
cursor.forward(100)
cursor.left(120)
cursor.forward(100)



cursor.penup()
cursor.right(150)
cursor.forward(50)

cursor.pendown()
cursor.right(90)

for i in range(3):
    cursor.forward(100)
    cursor.right(120)

tt.done()    