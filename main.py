from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [0,0,0]
matrix = new_matrix()

add_edge(matrix,63,0,0,63,107,0)
add_multi(matrix, "114,193 92,277 82,365 103,455 147,599 211,645 260,674 281,735 282,799 284,829 295,852 310,847 323,832 342,792 362,760 380,736 401,725 443,713 490,709 533,708 570,706 590,718 630,758 659,785 682,808 709,821 734,812 751,770 756,738 758,703 756,661 742,620 745,594 764,561 773,524 776,475 781,443 795,414 814,371 826,316 836,258 850,226 853,174 853,111 850,55", 900)
add_edge(matrix,472,0,0,472,30,0)
add_multi(matrix, "177,434 167,425 164,410 163,402 166,378 175,362 197,351 218,350 243,355 266,378 283,404 262,432 230,442 198,446 178,435 168,428 177,434", 900)
#add_multi(matrix, "293,279 257,293 228,307 208,308 183,308 171,303 213,288 252,281 286,278 313,266 354,274 394,283")
add_multi(matrix, "233,513 247,514 259,519 269,532 272,552 268,563 259,569 248,570 236,563 227,551 226,535 230,522 232,514 223,517 214,525 211,538 214,551 223,563 234,570 259,569", 900)
add_multi(matrix, "451,466 470,468 490,473 503,487 509,499 494,520 474,530 463,532 456,524 451,511 447,498 446,488 449,477 452,467 437,469 427,475 419,486 420,496 425,511 436,522 447,529 463,532", 900)
#print_matrix(matrix)

matrix2 = new_matrix()
matrix2 = matrix
for c in range(len(matrix2)):
    matrix2[c][0] = matrix2[c][0]+1
    print("matrix[" + str(c) + "][0]: " + str(matrix[c][0]))
    print("matrix2[" + str(c) + "][0]: " + str(matrix2[c][0]))

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
draw_lines( matrix2, screen, color )
display(screen)
save_extension(screen, 'img.png')
