import matplotlib.pyplot as plt
import pandas as pd
print("Welcome to The Survey Analysis on the topic\n"
      "\nJob placement in Various Colleges Around the World \n ")
print ("The given report consists of the following dataset:\n "
       "1.  Around 200 Universities\n "
       "2.  UG and PG placement of all the Universities\n "
       "3.  Placement percentage of each university\n "
       "4.  Number of males and females placed per college \n "
       "5.  Highest package obtained by a student of a particular university(in LPA) \n "
       "6.  Average package received per university (in LPA) "
       "7.  Count of the international and Domestic packages received by the college \n "
       "8.  Number of domains offered by a particular college \n "
       "9.  Location of the college\n "
       "10. Top companies that visited the college for recruitment \n\n")
Main_Table= pd.read_csv("C:\\Users\ADMIN\Desktop\IP\TRY.csv",index_col=0)
while True:
    print("How do you want to see your report :\n"
          "1. Tabular format\n"\
          "2. Visual Representation\n "
          "3. Mathematical calculations\n "
          "4. View full table \n "
          "5. Exit code \n")
    print("****** Please enter the number of the choice of your wish ****** ")
    command_1 = input("Please enter your choice : ")
    if command_1 not in [1,2,3,4]:
        try:
            int(command_1)
        except:
            print("Please enter a valid number")
    else:
        pass
    if command_1==1:
        print("What do you want to see from the table :\n "
              "1. Details of a particular College\n"
              # Add upper command
              "2. Details of a Group of Columns\n\n")
        print("****** Please enter the number of the choice of your wish ******\n \n ")
        command_2 = input("Please enter your choice : ")
        if command_2 not in [1,2]:
            try:
                int(command_2)
            except:
                print("Please enter a valid number")
        else:
            pass
        if command_2 == 1 :
            Name_of_college = input("Please enter the name of the college : ")
            print("The details of the college ",Name_of_college," are as follows :-\n \n ")
            print(Main_Table.loc[Name_of_college])
        elif command_2 == 2:
            Number_of_columns = input("Please enter the number of columns you want to see : ")
            if Number_of_columns not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                try:
                    int(Number_of_columns)
                except:
                    print("Please enter a valid number")
            else:
                pass
            print("Please make the choice for the columns from the below options:\n "
                  "1.  Highest Package (LPA)\n "
                  "2.  Domestic Package (LPA)\n "
                  "3.  International Package (LPA)\n "
                  "4.  No. Of Males Placed \n "
                  "5.  No. Of Females Placed\n "
                  "6.  Average Package Offered\n "
                  "7.  Job PLacement Percentage\n "
                  "8.  Location\n "
                  "9.  Companies Visited\n "
                  "10. No. Of Domains Offered\n "
                  "11. UG Placements\n "
                  "12. PG Placements\n ")
            list_columns = ["Name of College"]
            for i in range(Number_of_columns):
                column_input = input("Please enter your choice of column :")
                if column_input not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    try:
                        int(column_input)
                    except:
                        print("Please enter a valid number")
                else:
                    pass
                if column_input not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    print("Please enter a valid Choice")
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
            print("The choosen group of columns are : \n\n ")
            print(Main_Table[list_columns])
    elif command_1 == 2:
        print("What do you want to see in the form of graphs :\n "
              "1. Single column report\n "
              "2. Comparison of two columns\n ")
        print("****** Please enter the number of the choice of your wish ******\n \n ")
        command_3 = input("Please enter your choice : ")
        if command_3 not in [1,2]:
            try:
                int(command_3)
            except:
                print("Please enter a valid choice")
        else:
            pass
        if command_3 == 1:
            print("Which type of graph do you want see : \n "
                  "1. Bar graph\n "
                  "2, Scattered plot\n "
                  "3. Line graph\n "
                  "4. Column graph\n "
                  "5. Histogram\n "
                  "6. Pie chart\n  ")
            print("****** Please enter the number of the choice of your wish ******\n \n ")
            Graph_command = input("Please enter your choice ;")
            if Graph_command not in [1, 2, 3, 4,5,6]:
                try:
                    int(Graph_command)
                except:
                    print("Please enter a valid number")
            else:
                pass
            print("Please make the choice for the columns from the below options:\n "
                  "1.  Highest Package (LPA)\n "
                  "2.  Domestic Package (LPA)\n "
                  "3.  International Package (LPA)\n "
                  "4.  No. Of Males Placed\n  "
                  "5.  No. Of Females Placed\n "
                  "6.  Average Package Offered\n "
                  "7.  Job PLacement Percentage\n "
                  "8.  Location\n "
                  "9.  Companies Visited\n "
                  "10. No. Of Domains Offered\n "
                  "11. UG Placements\n "
                  "12. PG Placements\n \n ")
            Column_command_2 = input("Please enter the column from the list for which you want to see the graph : ")
            if Column_command_2 not in [1, 2, 3, 4,5,6,7,8,9,10,11,12]:
                try:
                    int(Column_command_2)
                except:
                    print("Please enter a valid number")
            else:
                pass
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
            print("Please make the choice for the columns from the below options:\n "
                  "1.  Highest Package\n "
                  "2.  Domestic package\n "
                  "3.  International offers\n "
                  "4.  No. Of Males Placed \n "
                  "5.  No. Of Females Placed\n "
                  "6.  Average Package Offered\n "
                  "7.  Job PLacement Percentage\n"
                  "8.  Location \n"
                  "9.  Companies Visited\n"
                  "10. No. Of domains avaliable\n"
                  "11. UG Placements\n"
                  "12. PG Placements\n\n")
            print("****** Please enter the number of the choice of your wish ******\n\n")
            no_column_input = input("Please enter the number of columns you want to opt for : ")
            if no_column_input not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                try:
                    int(no_column_input)
                except:
                    print("Please enter a valid number")
            else:
                pass
            for i in range(no_column_input):
                print("")
    elif command_1 == 3:
        print("Which mathematical function do you want to perform :\n "
              "1. Sum of values of a column\n"
              "2. Average of a column\n"
              "3. Maximum value of a column\n"
              "4. Minimum value of a column\n"
              "5. Median of a column\n"
              "6. Mode of a column \n\n")
        Maths_func_input = input("Please enter the number of the choice of your wish:")
        if Maths_func_input not in [1,2,3,4,5,6]:
            try:
                int(Maths_func_input)
            except:
                print("Please enter a valid number")
        else:
            pass
        print("Please make the choice for the columns from the below options:\n"
                  "1.  Highest Package (LPA)\n"
                  "2.  Domestic Package (LPA)\n"
                  "3.  International Offers (LPA)\n"
                  "4.  Number Of Males Placed\n"
                  "5.  Number Of Females Placed\n"
                  "6.  Average Package Offered\n"
                  "7. Job PLacement Percentage\n"
                  "8. Number Of Domains Avaliable\n"
                  "9. UG Placements\n"
                  "10. PG Placements\n\n")
        print("****** Please enter the number of the choice of your wish ****** \n\n")
        Column_input=input("Please enter the number of the column you opt for:")
        if Column_input not in [1, 2, 3, 4,5,6,7,8,9,10]:
            try:
                int(Column_input)
            except:
                print("Please enter a valid number")
        else:
            pass
        L1=['Name of College',
            'Highest Package (LPA)',
            'Domestic Package (LPA)',
            'International Package (LPA)',
            'Number of Males Placed',
            'Number of Females Placed',
            'Average Package Offered',
            'Job Placement Percentage',
            'Number of Domains Offered',
            'UG Placements',
            'PG Placements']
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
        print("The full table is : \n\n\n")
        print(Main_Table)
    elif command_1 == 5:
        print("\n")
        print("Hereby we have come to an end of the analysis of the job placement in various colleges\n\n")
        print("This Report is created by Aditi and Yanik Of Class XII A")
        break
