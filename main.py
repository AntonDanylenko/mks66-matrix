from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(cols=12)

matrix[0] = [250,250,0,1]
matrix[1] = [350,250,0,1]
matrix[2] = [350,250,0,1]
matrix[3] = [300,350,0,1]
matrix[4] = [300,350,0,1]
matrix[5] = [200,350,0,1]
matrix[6] = [200,350,0,1]
matrix[7] = [150,100,0,1]
matrix[8] = [150,100,0,1]
matrix[9] = [250,75,0,1]
matrix[10] = [250,75,0,1]
matrix[11] = [350,75,0,1]
print_matrix(matrix)

#ident(matrix)
#print_matrix(matrix)

transformation = new_matrix()
transformation[0] = [1,0,0,0]
transformation[1] = [0,1,0,0]
transformation[2] = [0,0,1,0]
transformation[3] = [0,0,0,1]
#matrix_mult(transformation, matrix)
#print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
