import matplotlib.pyplot as plt
import pandas as pd
print("Welcome to The Survey Analysis on the topic\n"
      "\nJob placement in Various Colleges Around the World \n")
print ("The given report consists of the following dataset:\n"
       "1.  Around 200 Universities\n"
       "2.  UG and PG placement of all the Universities\n"
       "3.  Placement percentage of each university\n"
       "4.  Number of males and females placed per college \n"
       "5.  Highest package obtained by a student of a particular university(in LPA) \n"
       "6.  Average package received per university (in LPA) \n"
       "7.  Count of the international and Domestic packages received by the college \n"
       "8.  Number of domains offered by a particular college \n"
       "9.  Location of the college\n"
       "10. Top companies that visited the college for recruitment \n\n")
Main_Table= pd.read_csv("C:\\Users\ADMIN\Desktop\IP\TRY_1.csv")
def Input(user,defined_range):
    try:
        user_input = int(user)
        if user_input in defined_range:
            return user_input
        else:
            print("Please enter a valid choice from the given options\n")
    except:
        print("Please enter a valid integer choice from the given options\n")
Choice_offered = ("Please make the choice for the columns from the below options:\n "
                       "1.  Highest Package (LPA)\n"
                       "2.  Domestic Package (LPA)\n"
                       "3.  International Package (LPA)\n"
                       "4.  No. Of Males Placed \n"
                       "5.  No. Of Females Placed\n"
                       "6.  Average Package Offered\n"
                       "7.  Job PLacement Percentage\n"
                       "8.  Location\n"
                       "9.  Companies Visited\n"
                       "10. No. Of Domains Offered\n"
                       "11. UG Placements\n"
                       "12. PG Placements\n")
# Tasks left to be done
# Ask for merging visual and tabular part
# Optimization and representation
while True:
    print("How do you want to see your report :\n"
          "1. Tabular format\n"
          "2. Visual Representation\n"
          "3. Mathematical calculations\n"
          "4. To find a college from its location\n"
          "5. To find the colleges visited by a particular company\n"
          "6. View full table \n"
          "7. Exit code \n")
    print("****** Please enter the number of the choice of your wish ****** ")
    command_1 = input("Please enter your choice : ")
    command_1 = Input(command_1,[1,2,3,4,5,6,7])
    if command_1==1:
        print("What do you want to see from the table :\n"
              "1. Details of a particular College\n"
              "2. Details of a Group of Columns\n\n")
        print("****** Please enter the number of the choice of your wish ******\n \n")
        command_2 = input("Please enter your choice : ")
        command_2 = Input(command_2,[1,2])
        if command_2 == 1 :
            Name_of_college = input("Please enter the name of the college : ")
            Name_of_college_renewed = Name_of_college.upper()
            if Name_of_college_renewed in Main_Table.loc[:,"Name of College"]:
                pass
            else:
                print("Please enter a valid name of the college\n")
            print("The details of the college ",Name_of_college," are as follows :-\n \n ")
            print(Main_Table.loc[Name_of_college_renewed])
        elif command_2 == 2:
            Number_of_columns = input("Please enter the number of columns you want to see : ")
            Number_of_columns = Input(Number_of_columns,[1,2,3,4,5,6,7,8,9,10,11,12])
            print(Choice_offered)
            list_columns = ["Name of College"]
            for i in range(Number_of_columns):
                column_input = input("Please enter your choice of column :")
                column_input = Input(column_input,[1,2,3,4,5,6,7,8,9,10,11,12])
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
        command_3 = Input(command_3,[1,2])
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
            Graph_command = Input(Graph_command,[1,2,3,4,5,6])
            print(Choice_offered)
            Column_command_2 = input("Please enter the column from the list for which you want to see the graph : ")
            Column_command_2 = Input(Column_command_2,[1,2,3,4,5,6,7,8,9,10,11,12])
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
            no_column_input = input("Please enter the number of columns you want to opt for : ")
            no_column_input = Input(no_column_input,[1,2,3,4,5,6,7,8,9,10,11,12])
            print(Choice_offered)
            print("****** Please enter the number of the choice of your wish ******\n\n")
            List_columns = ['Name of College',
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
            final_columns = ["Name of College"]
            for i in range(no_column_input):
                column_input_1 = input("Please enter the column number: \n")
                column_input_1 = Input(column_input_1,[1,2,3,4,5,6,7,8,9,10,11,12])
                final_columns.append(List_columns[column_input_1])
            print("The choosen columns are : \n\n")
            print(Main_Table[final_columns])
            print("Do you want see the graph of the selected: \n"
                          "1. Yes\n"
                          "2. No\n")
            print("****** Please enter the number of the choice of your wish ******\n\n ")
            graph_input = input("Please enter here :")
            graph_input = Input(graph_input, [1, 2])
            if graph_input == 1:
                print("Thanks for the confirmation ")
                print("Which type of graph do you want see : \n "
                      "1. Bar graph\n "
                      "2, Scattered plot\n "
                      "3. Line graph\n "
                      "4. Column graph\n "
                      "5. Histogram\n "
                      "6. Pie chart\n  ")
                print("****** Please enter the number of the choice of your wish ******\n \n ")
                graph_main = input("Which type of graph do you want to see : \n\n")
                graph_main = Input(graph_main,[1,2,3,4,5,6])
                if graph_main == 1:
                    for a in range(len(final_columns)):
                        print()
                elif graph_main == 2:
                    for a in range(len(final_columns)):
                        print()
                elif graph_main == 3:
                    for a in range(len(final_columns)):
                        print()
                elif graph_main == 4:
                    for a in range(len(final_columns)):
                        print()
                elif graph_main == 5:
                    for a in range(len(final_columns)):
                        print()
                elif graph_main == 6:
                    for a in range(len(final_columns)):
                        print()
            elif graph_input ==2:
                print("Okay!!!\n")
    elif command_1 == 3:
        print("Which mathematical function do you want to perform :\n "
              "1. Sum of values of a column\n"
              "2. Average of a column\n"
              "3. Maximum value of a column\n"
              "4. Minimum value of a column\n"
              "5. Median of a column\n"
              "6. Mode of a column \n\n")
        Maths_func_input = input("Please enter the number of the choice of your wish:")
        Maths_func_input = Input(Maths_func_input,[1,2,3,4,5,6])
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
        Column_input = Input(Column_input,[1,2,3,4,5,6,7,8,9,10])
        Column=List_columns[Column_input]
        if Maths_func_input == 1:
            print("The sum of the values of ",Column," is :\n")
            print(Main_Table[Column].sum())
        elif Maths_func_input == 2:
            print("The average of the values of ",Column," is :\n")
            print(Main_Table[Column].mean())
        elif Maths_func_input == 3 :
            print("The maximum of the values of ",Column," is :\n")
            print(Main_Table[Column].max())
        elif Maths_func_input == 4:
            print("The minimum of the values of ",Column," is :\n")
            print(Main_Table[Column].min())
        elif Maths_func_input == 5:
            print("The Median of the values of ",Column," is :\n")
            print(Main_Table[Column].median())
        elif Maths_func_input == 6:
            print("The Mode of the values of ",Column," is :\n")
            print(Main_Table[Column].mode())
        else:
            print("Please enter a valid choice\n")
    elif command_1 == 4:
        location_input = input("Please enter the location for which you want to search for a college : ")
        location_input_new = location_input.upper()
        location_list = []
        for i in range(len(Main_Table)):
            if location_input_new in Main_Table.loc[i, 'Location']:
                y = Main_Table.loc[i, 'Name of College']
                location_list.append(y)
        location_list_series = pd.Series(location_list)
        print("The college at the location ",location_input_new," are :-\n\n")
        print(location_list_series,"\n\n")
    elif command_1 == 5:
        Company_input = input("Please enter the company for which you want to check the colleges : ")
        Company_input = Company_input.upper()
        list_company = []
        for i in range(len(Main_Table)):
            if Company_input in Main_Table.loc[i, 'Companies Visited'].split(', '):
                x = Main_Table.loc[i, 'Name of College']
                list_company.append(x)
        list_company_series = pd.Series(list_company)
        print("The company ", Company_input, " visited the following colleges :-\n\n")
        print(list_company_series,"\n\n")
    elif command_1==6:
        print("The full table is : \n")
        print(Main_Table)
    elif command_1 == 7:
        print("\n")
        print("Hereby we have come to an end of the analysis of the job placement in various colleges")
        print("This Report is created by Aditi and Yanik Of Class XII A")
        break
