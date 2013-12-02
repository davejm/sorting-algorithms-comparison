#Sorting Algorithms Speed Comparison

##Description

This python script defines functions that enable the user to test and compare the 'Bubble' and 'Shuttle' ('Insertion') sorts on some randomly generated lists.

##Optional / Required Modules

Apart from in-built modules, this code defines a function to plot a comparison of execution times for each algorithm.
The necessary module for this to work is **matplotlib**. If you are on windows I recommend getting a distribution of python that comes with many packages pre-installed such as **python(x,y)** or **WinPython**.
If you are on linux then I recommend using your package manager to install matplotlib (e.g. `sudo apt-get install python-matplotlib`).

##Example Usage

````
from sorting import getnewlist, bubble, shuttle, test, produceresults

randomlist = getnewlist(500) #Get a list of 500 random numbers

print("Bubble took: " + str(test(bubble, randomlist)) + " seconds.")
print("Shuttle took: " + str(test(shuttle, randomlist)) + "seconds.")

produceresults(1, 1000, 20) #Comparison graph between algorithms acting on list of size 1 to 1000, incrementing by 20
````