from tkinter import *
from PIL import Image, ImageTk

SCREENWIDTH = 1300
SCREENHEIGHT = 900
ROBOTWIDTH = int(SCREENWIDTH / 10)
ROBOTHEIGHT = int(SCREENHEIGHT /10)
MOVE = 30



# Función para mover el robot hacia la derecha
def move_right():
    x, y = canvas.coords(robot)
    if x + ROBOTWIDTH / 2 < SCREENWIDTH:
        canvas.move(robot, MOVE, 0)

# Función para mover el robot hacia la izquierda
def move_left():
    x, y = canvas.coords(robot)
    if x - ROBOTWIDTH / 2 > 0:
        canvas.move(robot, -MOVE, 0)

# Función para mover el robot hacia arriba
def move_up():
    x, y = canvas.coords(robot)
    if y - ROBOTHEIGHT / 2 > 0:
        canvas.move(robot, 0, -MOVE)

# Función para mover el robot hacia abajo
def move_down():
    x, y = canvas.coords(robot)
    if y + ROBOTHEIGHT / 2 < SCREENHEIGHT:
        canvas.move(robot, 0, MOVE)


# Crear la ventana principal
root = Tk()
root.title("Control de Robot")

# Crear un lienzo donde se moverá el robot
canvas = Canvas(root, width=SCREENWIDTH, height=SCREENHEIGHT)
canvas.pack()

# Dibujar el robot como un rectángulo en el lienzo
img = Image.open('asimo.jpg')
img = img.resize((ROBOTWIDTH,ROBOTHEIGHT))
pic = ImageTk.PhotoImage(img)
robot = canvas.create_image(SCREENWIDTH/2, SCREENHEIGHT/2, image=pic) #canvas.create_rectangle(180, 180, 220, 220, fill="blue")

# Crear botones para controlar el movimiento del robot
button_left = Button(root, text="Izquierda", command=move_left)
button_left.pack(side=LEFT, padx=10, pady=10)

button_right = Button(root, text="Derecha", command=move_right)
button_right.pack(side=RIGHT, padx=10, pady=10)

button_up = Button(root, text="Arriba", command=move_up)
button_up.pack(side=TOP, padx=10, pady=10)

button_down = Button(root, text="Abajo", command=move_down)
button_down.pack(side=BOTTOM, padx=10, pady=10)

root.mainloop()