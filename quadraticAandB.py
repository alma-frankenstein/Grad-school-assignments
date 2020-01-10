#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

def quadratic(a, b, c, y_value, max_time):
    """ a, b, and c are constants. y_value is the initial y-value."""
    #positive time values
    time_span=list(range(0,max_time+1))
    
    time_span.reverse()
    
    #x_values is full range of values, negative and positive
    x_values = [tic*(-1) for tic in time_span]
    
    time_span.reverse()
    
    #adds positive values to x_values
    for tic in time_span:
        x_values.append(tic)
    
    y_values = [(a*tic**2)+(b*tic)+c for tic in x_values]
        
    
    print(y_values)
    print(x_values)
        
    plt.plot(x_values, y_values)
    

quadratic(5,4,3,0,10)

  
