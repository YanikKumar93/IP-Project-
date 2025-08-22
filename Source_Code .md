import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
print("Welcome to The Survey analysis of the topic"
      "Job placement in various colleges around the world ")
print ("The given report consists of the following dataset:"
       "1. Aound 200 Universties"
       "2. UG and PG placement of all the Universities"
       "3. Placement percentage of each unversity"
       "4. Number of males and females placed per college "
       "5. Highest package obtained by a student of a particular university(in LPA) "
       "6. Average package received per university (in LPA) "
       "7. Count of the international and Domestic packages received by the college "
       "8. Number of domains offered by a particular college "
       "9. Location of the college"
       "10. Top companies that visited the college for recruitment ")
while True:
    print("How do you want to see your report :")
    print("1. Tabular format")
    print("2. Visual Representation")
    print("****** Please enter the number of the choice of your wish ******")
    command_1 = int(input("Please enter your choice : "))
    print()
    if command_1==1:
        print()
    elif command_1 == 2:
        print()
    else:
        print("Sorry, But we cannot perform the entered task ")
    break
print("Hereby we have come to an end of the analysis of the job placement in various colleges\n")
print("This Report is created by Aditi and Yanik Of Class XII A")
