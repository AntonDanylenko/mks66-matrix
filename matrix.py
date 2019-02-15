"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    line = ""
    for line_num in range(4):
        for c in range(len(matrix)):
            line = line + str(matrix[c][line_num]) + " "
            #print("line c=" + str(c) + ", line_num=" + str(line_num) + ": " + line)
        print(line)
        line=""

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    if len(matrix)==0:
        print("empty matrix")
        return
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            if r==c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    x = 0
    y = 0
    z = 0
    e = 0
    for c in range(len(m2)):
        x = m2[c][0]
        y = m2[c][1]
        z = m2[c][2]
        e = m2[c][3]
        #print("x: " + str(x) + ", y: " + str(y) + ", z: " + str(z) + ", e: " + str(e))
        for r in range(4):
            #print("add: " + str(y*m1[1][r]))
            m2[c][r] = x*m1[0][r] + y*m1[1][r] + z*m1[2][r] + e*m1[3][r]
            #print("R= " + str(r) + ", m2[" + str(c) + "][" + str(r) + "]=" + str(m2[c][r]))


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
