import numpy as np

def halflife_to_damping(halflife):
    return (4.0*0.69314718056)/(halflife+1e-5)
def fast_negexp(x):
    return 1.0/(1.0+x+0.48*x*x+0.235*x*x*x)

def critical_spring_damper_exact(x,v,x_goal,v_goal,halflife,dt):
    g = x_goal
    q = v_goal
    d = (4.0*0.69314718056)/(halflife+1e-5)
    c = g + (d*q) / ((d*d) / 4.0)
    y = d / 2.0
    j0 = x - c
    j1 = v + j0*y
    eydt = 1.0/(1.0+y*dt+0.48*(y*dt)**2+0.235*(y*dt)**3)
    x = eydt*(j0+j1*dt)+c
    v = eydt*(v-j1*y*dt)
    return x, v