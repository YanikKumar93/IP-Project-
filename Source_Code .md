import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
print("Welcome to The Survey Analysis on the topic"
      "Job placement in Various Colleges Around the World ")
print ("The given report consists of the following dataset:"
       "1.  Around 200 Universities"
       "2.  UG and PG placement of all the Universities"
       "3.  Placement percentage of each university"
       "4.  Number of males and females placed per college "
       "5.  Highest package obtained by a student of a particular university(in LPA) "
       "6.  Average package received per university (in LPA) "
       "7.  Count of the international and Domestic packages received by the college "
       "8.  Number of domains offered by a particular college "
       "9.  Location of the college"
       "10. Top companies that visited the college for recruitment \n\n")
Main_Table= pd.read_csv("C:\\Users\ADMIN\Desktop\IP\TRY.csv",index_col=0)
while True:
    print("How do you want to see your report :\n")
    print("1. Tabular format")
    print("2. Visual Representation")
    print("3. Mathematical calculations")
    print("4. View full table ")
    print("****** Please enter the number of the choice of your wish ******\n")
    command_1 = int(input("Please enter your choice : "))
    if command_1 not in [1,2,3,4]:
        print("Please enter a valid Choice")
    else:
        continue
    if command_1==1:
        print("What do you want to see from the table :"
              "1. Details of a particular College"
              "2. Details of a Group of Columns")
        print("****** Please enter the number of the choice of your wish ******")
        command_2 = int(input("Please enter your choice "))
        if command_2 not in [1,2]:
            print("Please enter a Valid Choice")
        else:
            continue
        if command_2 == 1 :
            Name_of_college = input("Please enter the name of the college : ")
            print("The details of the college ",Name_of_college," are as follows :-")
            print(Main_Table.loc[Name_of_college])
        elif command_2 == 2:
             print("Please make the choice for the columns from the below options:"
                  "1.  Highest Package (LPA)"
                  "2.  Domestic Package (LPA)"
                  "3.  International Package (LPA)"
                  "4.  No. Of Males Placed "
                  "5.  No. Of Females Placed"
                  "6.  Average Package Offered"
                  "7.  Job PLacement Percentage"
                  "8.  Location"
                  "9.  Companies Visited"
                  "10. No. Of Domains Offered"
                  "11. UG Placements"
                  "12. PG Placements")
            Number_of_columns = int(input("Please enter the number of columns you want to see : "))
            if Number_of_columns not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                print("Please enter a valid Choice")
            else:
                continue
            print("Please make the choice for the columns from the below options:"
                  "1.  Highest Package (LPA)"
                  "2.  Domestic Package (LPA)"
                  "3.  International Package (LPA)"
                  "4.  No. Of Males Placed "
                  "5.  No. Of Females Placed"
                  "6.  Average Package Offered"
                  "7.  Job PLacement Percentage"
                  "8.  Location"
                  "9.  Companies Visited"
                  "10. No. Of Domains Offered"
                  "11. UG Placements"
                  "12. PG Placements")
            print("****** Please enter the number of the choice of your wish ******")
            list_columns = ["Name of College"]
            for i in range(Number_of_columns):
                column_input = int(input("Please enter your choice of column :"))
                if column_input not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    print("Please enter a valid Choice")
                else:
                    continue
                if column_input == 1:
                     list_columns.append("Highest Package (LPA)")
                elif column_input == 2:
                    list_columns.append("Domestic Package (LPA)")
                elif column_input == 3:
                    list_columns.append("International Package (LPA)")
                elif column_input == 4:
                    list_columns.append("Number of Males Placed")
                elif column_input == 5:
                    list_columns.append("Number of Females Placed")
                elif column_input == 6:
                    list_columns.append("Average Package Offered")
                elif column_input == 7:
                    list_columns.append("Job Placement Percentage")
                elif column_input == 8:
                    list_columns.append("Location")
                elif column_input == 9:
                    list_columns.append("Companies Visited")
                elif column_input == 10:
                    list_columns.append("Number of Domains Offered")
                elif column_input == 11:
                    list_columns.append("UG Placements")
                elif column_input == 12:
                    list_columns.append("PG Placements")
                else:
                    print("Please enter a valid choice")
                    break
            print("The choosen group of columns are : \n")
            print(Main_Table[list_columns])
    elif command_1 == 2:
        print("What do you want to see in the form of graphs :"
              "1. Single column report"
              "2. Comparison of two columns")
        print("****** Please enter the number of the choice of your wish ******")
        command_3 = int(input("Please enter your choice : "))
        if command_3 not in [1,2]:
            print("Please enter a valid Choice")
        else:
            continue
        if command_3 == 1:
            print("Which type of graph do you want see : "
                  "1. Bar graph"
                  "2, Scattered plot"
                  "3. Line graph"
                  "4. Column graph"
                  "5. Histogram"
                  "6. Pie chart ")
            print("****** Please enter the number of the choice of your wish ******")
            Graph_command = int(input("Please enter your choice ;"))
            if Graph_command ==1:
                print()
            elif Graph_command == 2:
                print()
            elif Graph_command == 3:
                print()
            elif Graph_command == 4:
                print()
            elif Graph_command == 5:
                print()
            elif Graph_command == 6:
                print()
            else:
                print("Please enter a valid choice\n")
        elif command_3 == 2:
            print("Please make the choice for the columns from the below options:"
                  "1.  Highest Package"
                  "2.  Domestic package"
                  "3.  International offers"
                  "4.  No. Of Males Placed "
                  "5.  No. Of Females Placed"
                  "6.  Average Package Offered"
                  "7.  Job PLacement Percentage"
                  "8.  Location "
                  "9.  Companies Visited"
                  "10. No. Of domains avaliable"
                  "11. UG Placements"
                  "12. PG Placements")
            print("****** Please enter the number of the choice of your wish ******\n")
            no_column_input = int(input("Please enter the number of columns you want to opt for : "))
            for i in range(no_column_input):
                print()
    elif command_1 == 3:
        print("Which mathematical function do you want to perform : "
              "1. Sum of values of a column"
              "2. Average of a column"
              "3. Maximum value of a column"
              "4. Minimum value of a column"
              "5. Median of a column"
              "6. Mode of a column \n")
        Maths_func_input = int(input("Please enter the number of the choice of your wish:"))
        if Maths_func_input not in [1,2,3,4,5,6]:
            print("Please enter a valid choice")
        else:
            continue
        print("Please make the choice for the columns from the below options:"
                  "1.  Highest Package (LPA)"
                  "2.  Domestic Package (LPA)"
                  "3.  International Offers (LPA)"
                  "4.  Number Of Males Placed "
                  "5.  Number Of Females Placed"
                  "6.  Average Package Offered"
                  "7. Job PLacement Percentage"
                  "8. Number Of Domains Avaliable"
                  "9. UG Placements"
                  "10. PG Placements")
        print("****** Please enter the number of the choice of your wish ****** \n")
        Column_input=int(input("Please enter the number of the column you opt for:"))
        L1=['Name of College', 'Highest Package (LPA)', 'Domestic Package (LPA)', 'International Package (LPA)', 'Number of Males Placed', 'Number of Females Placed', 'Average Package Offered', 'Job Placement Percentage', 'Number of Domains Offered', 'UG Placements', 'PG Placements']
        Column=L1[Column_input]
        if Maths_func_input == 1:
            print("The sum of the values of ",Column," is :")
            print(Main_Table[Column].sum())
        elif Maths_func_input == 2:
            print("The average of the values of ",Column," is :")
            print(Main_Table[Column].mean())
        elif Maths_func_input == 3 :
            print("The maximum of the values of ",Column," is :")
            print(Main_Table[Column].max())
        elif Maths_func_input == 4:
            print("The minimum of the values of ",Column," is :")
            print(Main_Table[Column].min())
        elif Maths_func_input == 5:
            print("The Median of the values of ",Column," is :")
            print(Main_Table[Column].median())
        elif Maths_func_input == 6:
            print("The Mode of the values of ",Column," is :")
            print(Main_Table[Column].mode())
        else:
            print("Please enter a valid choice")
    elif command_1==4:
        print("The full table is : \n")
        print(Main_Table)
    else:
        print("Sorry, But we cannot perform the entered task ")
    break
print("Hereby we have come to an end of the analysis of the job placement in various colleges\n")
print("This Report is created by Aditi and Yanik Of Class XII A")
