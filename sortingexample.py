# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:00:23 2013

@author: David Moodie
"""

from sorting import getnewlist, bubble, shuttle, test, produceresults

randomlist = getnewlist(500) #Get a list of 500 random numbers

print("Bubble took: " + str(test(bubble, randomlist)) + " seconds.")
print("Shuttle took: " + str(test(shuttle, randomlist)) + "seconds.")

produceresults(1, 1000, 20) #Comparison graph between algorithms acting on list of size 1 to 1000, incrementing by 20