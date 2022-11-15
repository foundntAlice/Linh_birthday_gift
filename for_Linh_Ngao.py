#Anh thực sự xin lỗi vì quãng thời gian qua, a vẫn chưa trưởng thành, vẫn thi thoảng có những lời nói 
#làm em tổn thương. Còn em vẫn vậy, vẫn xinh đẹp, tốt bụng, luôn suy nghĩ cho người khác. Tuy thi thoảng 
#có hơi ngang một chút, nhưng cái đó làm em mạnh mẽ hơn, độc lập hơn.
#Rứa là Linh tròn 24 rồi, bắt đầu bước qua tuổi 25. Nỏ biết nói chi cả, chỉ mong Linh tuổi mới luôn vui vẻ, 
#vô tâm hơn một chút cũng tốt, để đỡ bị tủi. Cứ hồn nhiên bay nhảy như ri nhé Ngáo!
#I love u as always!
import turtle
from turtle import *
import os

# Creating a function to draw a circle on top of stick
def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(border_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    my_turtle_cursor.circle(radius)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing the first side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the second side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    # Drawing the third side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the fourth side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

def draw_the_flame(fill_color, border_color, x, y):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.right(90)
    for _ in range(3):
        my_turtle_cursor.forward(25)
        my_turtle_cursor.right(120)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.left(90)

    my_turtle_cursor.getscreen().update()

# Creating a Function to draw stick on the candle
def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("Happy", font=("sans-serif", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("Birthday!", font=("sans-serif", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(200)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Function to draw topping of our cake
def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing a circle using circle function
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Creating a Function to draw different layers of a cake
def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()

    my_turtle_cursor.pensize(cursor_size)
    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()

    # Starting the cursor to fill color
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

def drawBirthDayCake():

    y_coordinate = -125

    # # Creating an empty list of different parts of our cake
    parts_of_cake = []
    parts_of_cake.append(["DeepSkyBlue", "#000000", 3, 30])
    parts_of_cake.append(["white", "#000000", 3, 20])
    parts_of_cake.append(["#B87333", "#000000", 3, 60])

    # drawing an plate for our cake using draw_layer_of_the_cake() function
    draw_layer_of_the_cake("DarkViolet", "#000000", 3, -220, y_coordinate - 70, 400, 10)

    # Drawing different parts of our cake
    for parts in parts_of_cake:
        draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
        y_coordinate += parts[3]

    # drawing top topping of our cake
    draw_toppings_on_cake("#C20067", "#000000", -120, y_coordinate - 60, 10)
    draw_toppings_on_cake("#FFFF00", "#000000", -80, y_coordinate - 60, 10)
    draw_toppings_on_cake("#FF0000", "#000000", 25, y_coordinate - 60, 10)
    draw_toppings_on_cake("#0000FF", "#000000", 59, y_coordinate - 60, 10)

    # drawing middle topping of our cakes
    draw_toppings_on_cake("#FFA500", "#000000", -135, y_coordinate - 80, 10)
    draw_toppings_on_cake("#E4E6EB", "#000000", -135, y_coordinate - 100, 10)
    draw_toppings_on_cake("#FFA500", "#000000", -135, y_coordinate - 120, 10)
    draw_toppings_on_cake("#181A18", "#000000", -80, y_coordinate - 80, 10)
    draw_toppings_on_cake("#0000FF", "#000000", -65, y_coordinate - 110, 10)
    draw_toppings_on_cake("#FFD700", "#000000", -95, y_coordinate - 140, 10)
    draw_toppings_on_cake("#181A18", "#000000", 10, y_coordinate - 80, 10)
    draw_toppings_on_cake("#E4E6EB", "#000000", -20, y_coordinate - 110, 10)
    draw_toppings_on_cake("#181418", "#000000", 35, y_coordinate - 140, 10)
    draw_toppings_on_cake("#FFA500", "#000000", 75, y_coordinate - 80, 10)
    draw_toppings_on_cake("#E4E6EB", "#000000", 75, y_coordinate - 110, 10)
    draw_toppings_on_cake("#FFD700", "#000000", 75, y_coordinate - 140, 10)

    # Drawing candle on of our cake using draw_candle_for_cake() function
    draw_candle_for_cake("#FFF44F", "#000000", -40, y_coordinate - 60)

    # Drawing stick on top of our candle
    draw_stick_on_candle("#181A18", -26, y_coordinate + 15, 7)

    # Drawing the flame on top of the cake
    draw_the_flame("#FF8C00", "#FF8C00", -26 + 12, y_coordinate + 12)

    # Drawing a stick for writing Happy Birthday
    draw_stick("#181A18", "#181A18", 0, y_coordinate - 60)

    # Drawing a circle on top of stick
    draw_circle_on_top_of_stick("MediumSpringGreen", "MediumSpringGreen", 100, y_coordinate + 235, 100)

    # Writing "Happy" inside of our circle
    write_happy_inside_circle("#000000", -70, y_coordinate + 240)

    # Writing "Birthday" inside of our circle
    write_birthday_inside_circle("#000000", -80, y_coordinate + 190)

    # Calling done function at the end


if __name__ == '__main__':
    #play sound during the process
    file = "bleeding_love.wav"
    os.system("mpg123 " + file)
    canvas = turtle.Screen()
    turtle.bgcolor("DodgerBlue")
    turtle.title("For my Polar Bear :v")

    # Creating our turtle cursor to draw
    my_turtle_cursor = turtle.Turtle()


    # Creating a separate Canvas to draw "Happy Birthday"
    my_turtle_screen = turtle.Screen()

    drawBirthDayCake()

    turtle.bgcolor("black")
    turt = turtle.Turtle()
    x = -300
    y = -250

    turt.penup()
    turt.setposition(x, y)
    turt.color("fuchsia")
    turt.shape("turtle")
    turt.pendown()

    turt.pensize(10)
    turt.right(90)
    turt.fd(100)
    turt.left(90)
    turt.fd(40)

    turt.penup()
    turt.setposition(x + 70, y)
    turt.pendown()
    turt.right(90)
    turt.fd(100)

    turt.penup()
    turt.setposition(x + 100, y - 100)
    turt.pendown()
    turt.left(180)
    turt.fd(100)
    turt.right(150)
    turt.fd(120)
    turt.left(150)
    turt.fd(100)

    turt.penup()
    turt.setposition(x + 190, y)
    turt.pendown()
    turt.right(180)
    turt.fd(100)
    turt.bk(50)
    turt.left(90)
    turt.fd(50)
    turt.left(90)
    turt.fd(50)
    turt.bk(100)

    turt.penup()
    turt.setposition(x + 300, y - 100)
    turt.pendown()
    turt.fd(100)
    turt.right(150)
    turt.fd(120)
    turt.left(150)
    turt.fd(100)

    turt.penup()
    turt.setposition(x + 430, y)
    turt.left(90)
    turt.pendown()
    turt.circle(50, 180)
    turt.left(90)
    turt.fd(40)
    turt.left(90)
    turt.fd(15)

    turt.penup()
    turt.setposition(x + 450, y - 100)
    turt.pendown()
    turt.right(110)
    turt.fd(105)
    turt.right(140)
    turt.fd(105)
    turt.bk(45)
    turt.right(110)
    turt.fd(30)

    turt.penup()
    turt.setposition(x + 590, y)
    turt.pendown()
    turt.circle(50)

    turt.penup()
    turt.setposition(x + 490, y + 30)
    turt.pendown()
    turt.right(140)
    turt.fd(25)

    turt.color("DodgerBlue")
    turt.penup()
    turt.setposition(x - 50, y + 100)
    turt.right(130)
    turt.pendown()
    turt.fd(60)
    turt.bk(60)
    turt.left(90)
    turt.fd(20)
    turt.bk(40)

    turt.penup()
    turt.setposition(x + 20, y + 100)
    turt.pendown()
    turt.left(180)
    turt.circle(25)

    turt.penup()
    turt.setposition(-350, 350)
    turt.color("yellow")
    style = ('Courier', 26, 'italic')
    turt.write("I hope you a new age with full of happiness, don't change your personality for any reason, you will never know how beautiful you are, inside and out!")
    turt.hideturtle()

    done()