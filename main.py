from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge(matrix, [150,250,0,1], [350,250,0,1])
add_edge(matrix, [350,250,0,1], [300,400,0,1])
add_edge(matrix, [300,400,0,1], [200,400,0,1])
add_edge(matrix, [200,400,0,1], [150,250,0,1])
add_edge(matrix, [150,250,0,1], [200,100,0,1])
add_edge(matrix, [200,100,0,1], [250,075,0,1])
add_edge(matrix, [250,075,0,1], [350,150,0,1])
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
