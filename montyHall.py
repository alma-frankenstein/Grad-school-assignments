#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#to illustrate that switching, counterintuitively, increases the odds of winning.
#contestant CHOICES  are automated to allow for a large number of test runs, but could be
#changed to get user input

import random

DOORS = ['A', 'B', 'C']
CHOICES  = ["stay", "switch"]

def main():
    num_runs = 100
    monty(num_runs)
    
def monty(num_runs):
    switchAndWin = 0 #times winning if you switch
    stayAndWin = 0 #times winning if you stay
    runs = 0
    
    while runs <= num_runs:
        prize = random.choice(DOORS)
        picked_door = random.choice(DOORS)
        #Monty open a door that was neither chosen nor containing the prize
        for door in DOORS:
            if door != prize and door != picked_door:
                openedDoor = door
                break
            
        #the contestant can either stay with picked_door or switch to the other unopened one
        stayOrSwitch = random.choice(CHOICES )
        if stayOrSwitch == "stay":
            final = picked_door
            if final == prize:
                stayAndWin += 1
        else: #switch
            for door in DOORS:
                if door != openedDoor and door != picked_door:
                    final = door
                    if final == prize:
                        switchAndWin += 1
                    break
                    
        runs += 1
        
    percentSwitchWin = (switchAndWin/num_runs) * 100
    percentStayWin = (stayAndWin/num_runs) * 100
    
    print("Odds of winning if you stay: " + str(percentStayWin))
    print("Odds of winning if you switch: " + str(percentSwitchWin))

if __name__ == '__main__':
    main()
