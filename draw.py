from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    c=0
    while c<len(matrix)-1:
        draw_line(matrix[c][0], matrix[c][1], matrix[c+1][0], matrix[c+1][1], screen, color)
        c+=2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z=z0)
    add_point(matrix,x1,y1,z=z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

def add_multi(matrix, coords, size):
    coords_list = coords.split(" ")
    for i in range(len(coords_list)):
        coords_list[i] = coords_list[i].split(",")
        for ii in range(len(coords_list[i])):
            coords_list[i][ii] = int(int(coords_list[i][ii])*500.0/size)
            #print(str(coords_list[i][ii]) + " ")
        #print("\n")
    for i in range(len(coords_list)-1):
        add_edge(matrix,coords_list[i][0],coords_list[i][1],0,coords_list[i+1][0],coords_list[i+1][1],0)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
