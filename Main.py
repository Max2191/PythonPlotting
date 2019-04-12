import numpy as np
import matplotlib.pyplot as plt
from math import *

#initiate an empy list that will store the provided isotopes
isotopes=[]

#begin a loop
#prompt user to input an isotop from the list and then enter its halflife, entering the string 'stop' will kill this process
while True:
 isotope = input("Please provide an isotope from the list. Once you have finished entering isotopes, type 'stop'")
 if isotope=="stop":
    break
 else:
    halflife = float(input("Please provide the isotope's halflife in seconds"))

#prompt user for initial amount of isotope and the elapsed time 
    a_grams = float(input("Please provide the initial mass of the isotope in grams"))
    e_time = float(input("Please provide the elapsed time in seconds"))

#add the provided isotope to the list
    isotopes.append(isotope)

#calculates the amount of isotope remaining after e_time has elapsed and assigns it to the variable i_remaining 

    i_remaining=a_grams*np.exp(-log(2)*(e_time/halflife))
    
#calculates the initial amount of the isotope, i_req, necessry for 5g to be remaining after 30s has elapsed

    i_req = 5/(np.exp(-log(2)*(30/halflife)))
    print "the amount of", isotope,"remaining after", e_time,"seconds has elapsed is", i_remaining
    print "the initial mass, in grams, of", isotope,"to ensure 5g remains after 30 seconds is", i_req
    
#defines the array of independent variable on the x-axis
    X=np.linspace(0,11,11)
   
#defines the array of dependent variable on the y-axis
    Y=a_grams*np.exp(-log(2)*(X/halflife))

#creates a plot with these parameters

    plt.plot(X,Y)
    plt.title ('Plot of isotopes')
    plt.xlabel("Time / s")
    plt.ylabel("Amount / g")

#renders a plot for all the entered isotopes
    plt.show()

#print the list of isotopes studies (blank spaces are aesthetic only)
    print ""
    print ""
    print "Isotopes entered into the program:", isotopes