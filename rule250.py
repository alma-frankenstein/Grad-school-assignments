#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    total_steps = 15
    wolfram250(total_steps)
    
def wolfram250(total_steps):
    #to start, 33 cells, all white with one black at the center
    ca = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # new values--creates new blank list to be filled
    ca_new = ca[:]
    
    print(ca_new)
    
    step = 1
    #total_steps = 15
    while(step < total_steps):
        ca_new = []
      # loop through 0 to 32 and store the current cell status in ca_new list
        for i in range(0,33):
     # for cells that aren't edge cells
            if i > 0 and i < 32:
                if ca[i-1] == ca[i+1] and ca[i+1]==0:
                    ca_new.append(0)
                else:
                    ca_new.append(1)
    
     # left-most cell : check the second cell
            elif(i == 0):
                if ca[1] == 1:
                    ca_new.append(1)
                else: ca_new.append(0)
    
     # right-most cell : check the second to the last cell
            elif(i == 32):
                if ca[31] == 1:
                    ca_new.append(1)
                else:
                    ca_new.append(0)
    
        print(ca_new)
    
        # update cell list
        ca = ca_new[:]
    
        step +=1
        
if __name__ == '__main__':
    main()
