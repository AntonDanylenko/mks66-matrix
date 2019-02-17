from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_multi(matrix, "114,193 92,277 82,365 103,455 147,599 211,645 260,674 281,735 282,799 284,829 295,852 310,847 323,832 342,792 362,760 380,736 401,725 443,713 490,709 533,708 570,706 590,718 630,758 659,785 682,808 709,821 734,812 751,770 756,738 758,703 756,661 742,620 745,594 764,561 773,524 776,475 781,443 795,414 814,371 826,316 836,258 850,226 853,174 853,111 850,55")
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
