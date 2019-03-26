from tkinter import *
# Rabbits and foxes

# Tk frame
root = Tk()
root.title("Rabbits and Foxes graph")

# Canvas
mycanvas = Canvas(width = 1000, height = 500, bg = 'white')
mycanvas.create_text(325, 50, anchor = NW, font = ("Arial", 24), text = "Rabbits and Foxes graph")
mycanvas.pack()

# Labels 
mycanvas.create_text(140, 50, font=("Arial", 12), text="Rabbit = blue", fill='blue')
mycanvas.create_text(127, 80, font=("Arial", 12), text="Fox = red", fill='red')

# Axes
xaxes = mycanvas.create_line(50, 350, 600, 350, fill = 'green')
yaxes = mycanvas.create_line(50, 400, 50, 50, fill = 'green')

#############################################################

# Chicken and foxes list
rabbit = 500
fox = 10

a = 0.1
b = 0.00002
c = 0.01
d = 0.01
e = 0.00002
f = 0.0001

rabbitArray = []
foxArray = []


# Equation - Rabbit and fox curve
for x in range(400) :
    rabbitEquation = rabbit * (1 + a - b * rabbit - c * fox)
    foxEquation = fox * (1 - d + e * rabbit - f * fox)

    rabbit = rabbitEquation
    fox = foxEquation

    rabbitArray.append(50 + x)
    rabbitArray.append(-196 + rabbitEquation)

    foxArray.append(50 + x)
    foxArray.append(34 + foxEquation * 35)

rabbitCurve = mycanvas.create_line(rabbitArray, fill = 'blue')
foxCurve = mycanvas.create_line(foxArray, fill = 'red')


# Rabbit and fox steady state
steadyRabbit = str(int(rabbitArray[-1]))
steadyFox = str(int(foxArray[-1] / 35))

mycanvas.create_text(600, 400, font=("Arial", 12), text="Rabbit steady state : " + steadyRabbit, fill='blue')
mycanvas.create_text(585, 430, font=("Arial", 12), text="Fox steady state : " + steadyFox, fill='red')


root.mainloop()