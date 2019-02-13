from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

matrix[0] = [0,1,2,1]
matrix[1] = [3,4,5,1]
matrix[2] = [6,7,8,1]
matrix[3] = [9,10,11,1]
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
