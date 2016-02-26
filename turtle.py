from turtle import *

def spiral(iL, tA, m):
    if iL<=1:
        return
    else:
        forward (iL)
        left (tA)
        spiral (iL * m, tA, m)
        
        
def svTree(tL, l):
    if l <=0:
        return
    else:
        forward(tL)
        left(30)
        svTree(tL/2, l - 1)
        right (60)
        svTree(tL/2, l - 1)
        left(30)
        backward(tL)
   

def snowflake(lS, l):
    if l==0:
        forward(lS)
    else:
        snowflake(lS/3, l-1)
        right(60)
        snowflake(lS/3, l-1)
        left(120)
        snowflake(lS/3, l-1)
        right(60)
        snowflake(lS/3, l-1)


def edge(lS,l):
    snowflake(lS, l)
    left(120)
    snowflake(lS, l)
    left(120)
    snowflake(lS, l)

        
