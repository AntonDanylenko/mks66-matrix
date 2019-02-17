from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge(matrix,150,250,0,350,250,0)
add_edge(matrix,350,250,0,300,350,0)
add_edge(matrix,300,350,0,200,350,0)
add_edge(matrix,200,350,0,150,250,0)
add_edge(matrix,150,250,0,200,100,0)
add_edge(matrix,200,100,0,250,100,0)
add_edge(matrix,250,100,0,350,150,0)
print_matrix(matrix)

A = new_matrix()
B = new_matrix()
A[0] = [1,2,3,4]
A[1] = [5,6,7,8]
A[2] = [9,10,11,12]
A[3] = [13,14,15,16]
B[0] = [11,12,13,14]
B[1] = [15,16,17,18]
B[2] = [19,20,21,22]
B[3] = [23,24,25,26]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)
print_matrix(A)
print_matrix(B)
ident(B)
matrix_mult(B,A)
print_matrix(A)

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
