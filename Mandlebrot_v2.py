import graphics

c=1
precision = 100
win_max = 200
scale = 100
x_offset = 0
y_offset = 0

win=graphics.GraphWin("Mandelbrot",win_max, win_max)

for num_y in range (0, win_max +1):

    y = (num_y/(scale)) - ((win_max/2)/scale) + y_offset

    for num_x in range(0, win_max +1):

        count = 0
        check = 0

        x = (num_x/(scale)) - ((win_max/2)/scale) + x_offset

        z= complex(x,y)**2 - c

        while count < precision:

            point = graphics.Point(num_x, num_y)

            z = z**2 - c

            if abs(z) > 100000:
                check = count
                count = precision

            count += 1

        if abs(z) <= 1:
            point.setFill("black")

        elif check > 12:
            point.setFill("red")

        elif check > 9:
            point.setFill("orange")

        point.draw(win)
