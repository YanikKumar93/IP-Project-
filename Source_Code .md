import matplotlib.pyplot as mp
import pandas as pd
print("Welcome to The Survey Analysis on the topic\n"
      "\nJob placement in Various Colleges Around the World \n")
print ("The given report consists of the following dataset:\n"
       "\t\t1.  Around 200 Universities\n"
       "\t\t2.  UG and PG placement of all the Universities\n"
       "\t\t3.  Placement percentage of each university\n"
       "\t\t4.  Number of males and females placed per college \n"
       "\t\t5.  Highest package obtained by a student of a particular university(in LPA) \n"
       "\t\t6.  Average package received per university (in LPA) \n"
       "\t\t7.  Count of the international and Domestic packages received by the college \n"
       "\t\t8.  Number of domains offered by a particular college \n"
       "\t\t9.  Location of the college\n"
       "\t\t10. Top companies that visited the college for recruitment \n\n")
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
                       "\t\t1.  Highest Package (LPA)\n"
                       "\t\t2.  Domestic Package (LPA)\n"
                       "\t\t3.  International Package (LPA)\n"
                       "\t\t4.  No. Of Males Placed \n"
                       "\t\t5.  No. Of Females Placed\n"
                       "\t\t6.  Average Package Offered\n"
                       "\t\t7.  Job PLacement Percentage\n"
                       "\t\t8.  Location\n"
                       "\t\t9.  Companies Visited\n"
                       "\t\t10. No. Of Domains Offered\n"
                       "\t\t11. UG Placements\n"
                       "\t\t12. PG Placements\n")
while True:
    print("How do you want to see your report :\n"
          "\t\t1. Data of colleges\n"
          "\t\t2. Visual Representation\n"
          "\t\t3. Mathematical calculations\n"
          "\t\t4. To find a college from its location\n"
          "\t\t5. To find the colleges visited by a particular company\n"
          "\t\t6. View full table \n"
          "\t\t7. Exit code \n")
    print("****** Please enter the number of the choice of your wish ****** ")
    command_1 = input("Please enter your choice : ")
    command_1 = Input(command_1,[1,2,3,4,5,6,7])
    if command_1==1:
        print("What do you want to see from the table :\n"
              "\t\t1. Details of a particular College\n"
              "\t\t2. Details of a Group of Columns\n\n")
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
            print("The details of the college ",Name_of_college," are as follows :-\n\n")
            print(Main_Table[Main_Table["Name of College"]== Name_of_college_renewed].squeeze().drop("S. No."),"\n")
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
            print("The choosen group of columns are : \n\n")
            print(Main_Table[list_columns])
            if Number_of_columns == 1:
                print("Do you want see the graph of the selected: \n"
                    "\t\t1. Yes\n"
                    "\t\t2. No\n")
                print("****** Please enter the number of the choice of your wish ******\n\n")
                graph_input = input("Please enter here :")
                graph_input = Input(graph_input, [1, 2])
                if graph_input == 1:
                    if column_input != 8:
                        print("Thanks for the confirmation ")
                        print("For which colleges do you want to see the graph :\n"
                              "\t\t1.Top colleges\n"
                              "\t\t2.Bottom most colleges\n"
                              "\t\t3.Customised (You have to input the name of college\n")
                        print("****** The columns will be arranged in ascending order of your preferred row choice ******")
                        College_option = input("Please enter the number of your choice :")
                        College_option = Input(College_option,[1,2,3])
                        print("Which type of graph do you want see : \n"
                              "\t\t1. Bar graph\n"
                              "\t\t2, Scattered plot\n"
                              "\t\t3. Line graph\n")
                        print("****** Please enter the number of the choice of your wish ******\n\n")
                        graph_main = input("Which type of graph do you want to see : \n\n")
                        graph_main = Input(graph_main, [1, 2, 3, 4, 5, 6])
                        Main_Table_sorted = Main_Table.sort_values(by=list_columns[-1], ascending=True)
                        if College_option == 1:
                            top_rows = input("Please enter the rows from the top you want to opt for : ")
                            top_rows = Input(top_rows,range(1,203))
                            series = Main_Table["Name of College"].head(top_rows)
                            list_college_top_1 = series.tolist()
                            if graph_main == 1:
                                mp.bar(X = list_college_top_1,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 2:
                                mp.scatter(X = list_college_top_1,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 3:
                                mp.plot(X = list_college_top_1,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            else:
                                print("Invalid Choice")
                        elif College_option ==2 :
                            bottom_rows = input("Please enter the rows from the bottom you want to opt for :")
                            bottom_rows = Input(bottom_rows,range(1,203))
                            sries_tail = Main_Table["Name of College"].tail(bottom_rows)
                            list_college_bottom = sries_tail.tolist()
                            if graph_main == 1:
                                mp.bar(X = list_college_bottom,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 2:
                                mp.scatter(X = list_college_bottom,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 3:
                                mp.plot(X = list_college_bottom,Y = Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            else:
                                print("Invalid Choice")
                        elif College_option == 3:
                            custom_rows = input("Please enter the number of rows you want to opt for :")
                            custom_rows = Input(custom_rows,range(1,203))
                            list_custom_rows = []
                            for i in range(custom_rows):
                                name_college = input("Please enter the name of the college : ")
                                name_college_1 = name_college.upper()
                                for j in range(len(Main_Table)):
                                    if name_college_1 in Main_Table.loc[i, 'Name of College']:
                                        y = Main_Table.loc[j, 'Name of College']
                                        list_custom_rows.append(y)
                            if graph_main == 1:
                                mp.bar(X = list_custom_rows, Y =Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 2:
                                mp.scatter(X = list_custom_rows, Y =Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            elif graph_main == 3:
                                mp.plot(X = list_custom_rows, Y =Main_Table_sorted[list_columns[-1]])
                                mp.show()
                            else:
                                print("Invalid Choice")
                    else:
                        pass
                elif graph_input == 2:
                    print("Okay !!!!\n")
            else:
                pass
    elif command_1 == 2:
        print(Choice_offered,"\n\n")
        Column_command_2 = input("Please enter the column number from the list for which you want to see the graph : ")
        Column_command_2 = Input(Column_command_2,[1,2,3,4,5,6,7,8,9,10,11,12])
        List_columns_new = ["Highest Package (LPA)",
                            "Domestic Package (LPA)",
                            "International Package (LPA)",
                            "Number of Males Placed",
                            "Number of Females Placed",
                            "Average Package Offered",
                            "Job Placement Percentage",
                            "Location",
                            "Companies Visited",
                            "Number of Domains Offered",
                            "UG Placements",
                            "PG Placements"]
        List_columns_selected = []
        List_columns_selected = List_columns_selected.append(List_columns_new[Column_command_2 - 1])
        if Column_command_2 !=8:
            print("For which colleges do you want to see the graph :\n"
                  "\t\t1.Top colleges\n"
                  "\t\t2.Bottom most colleges\n"
                  "\t\t3.Customised\n"
                  "****** The columns will be arranged in ascending order of your preferred row choice ******")
            College_option_1 = input("Please enter the number of your choice :")
            College_option_1 = Input(College_option_1, [1, 2, 3])
            print("Which type of graph do you want see : \n"
                  "\t\t 1. Bar graph\n"
                  "\t\t 2. Scattered plot\n"
                  "\t\t 3. Line graph\n")
            print("****** Please enter the number of the choice of your wish ******\n\n")
            graph_main_1 = input("Which type of graph do you want to see : \n\n")
            graph_main_1 = Input(graph_main_1, [1, 2, 3])
            Main_Table_sorted_new_1 = Main_Table.sort_values(by = List_columns_new[Column_command_2] , ascending=True)
            if College_option_1 == 1:
                top_rows_new = input("Please enter the rows from the top you want to opt for : ")
                top_rows_new = Input(top_rows_new, range(1, 203))
                series = Main_Table["Name of College"].head(top_rows_new)
                list_college_top = series.tolist()
                if graph_main_1 == 1:
                    mp.bar(X = list_college_top,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                elif graph_main_1 == 2:
                    mp.scatter(X = list_college_top,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                elif graph_main_1 == 3:
                    mp.plot(X = list_college_top,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                else:
                    print("Invalid Choice")
            elif College_option_1 == 2:
                bottom_rows_new = input("Please enter the rows from the bottom you want to opt for :")
                bottom_rows_new = Input(bottom_rows_new, range(1, 203))
                sries_tail = Main_Table["Name of College"].tail(bottom_rows_new)
                list_college_bottom_1 = sries_tail.tolist()
                if graph_main_1 == 1:
                    mp.bar(X = list_college_bottom_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                elif graph_main_1 == 2:
                    mp.scatter()
                    mp.show(X = list_college_bottom_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                elif graph_main_1 == 3:
                    mp.plot(X = list_college_bottom_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                else:
                    print("Invalid Choice")
            elif College_option_1 == 3:
                custom_rows_1 = input("Please enter the number of rows you want to opt for :")
                custom_rows_1 = Input(custom_rows_1, range(1, 203))
                list_custom_rows_1 = []
                for i in range(custom_rows_1):
                    name_college_new = input("Please enter the name of the college : ")
                    name_college_1_new = name_college_new.upper()
                    for j in range(len(Main_Table)):
                        if name_college_1_new in Main_Table.loc[i, 'Name of College']:
                            y = Main_Table.loc[j, 'Name of College']
                            list_custom_rows_1.append(y)
                if graph_main_1 == 1:
                    mp.bar(X = list_custom_rows_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                elif graph_main_1 == 2:
                    mp.scatter(X = list_custom_rows_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                elif graph_main_1 == 3:
                    mp.plot(X = list_custom_rows_1,Y = Main_Table_sorted_new_1[List_columns_selected])
                    mp.show()
                else:
                    print("Invalid Choice")
    elif command_1 == 3:
        print("Which mathematical function do you want to perform :\n "
              "\t\t1. Sum of values of a column\n"
              "\t\t2. Average of a column\n"
              "\t\t3. Maximum value of a column\n"
              "\t\t4. Minimum value of a column\n"
              "\t\t5. Median of a column\n"
              "\t\t6. Mode of a column \n\n")
        Maths_func_input = input("Please enter the number of the choice of your wish:")
        Maths_func_input = Input(Maths_func_input,[1,2,3,4,5,6])
        print("Please make the choice for the columns from the below options:\n"
                  "\t\t1.  Highest Package (LPA)\n"
                  "\t\t2.  Domestic Package (LPA)\n"
                  "\t\t3.  International Offers (LPA)\n"
                  "\t\t4.  Number Of Males Placed\n"
                  "\t\t5.  Number Of Females Placed\n"
                  "\t\t6.  Average Package Offered\n"
                  "\t\t7. Job Placement Percentage\n"
                  "\t\t8. Number Of Domains Avaliable\n"
                  "\t\t9. UG Placements\n"
                  "\t\t10. PG Placements\n\n")
        print("****** Please enter the number of the choice of your wish ****** \n\n")
        Column_input=input("Please enter the number of the column you opt for:")
        Column_input = Input(Column_input,[1,2,3,4,5,6,7,8,9,10])
        List_columns = []
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
            if Company_input in Main_Table.loc[i,'Companies Visited'].split(', '):
                x = Main_Table.loc[i, 'Name of College']
                list_company.append(x)
        list_company_series = pd.Series(list_company)
        print("The company ", Company_input, " visited the following colleges :-\n\n")
        print(list_company_series,"\n\n")
    elif command_1==6:
        print("The full table is : \n")
        print(Main_Table)
    elif command_1 == 7:
        print("\n\n\n")
        print("Hereby we have come to an end of the analysis of the job placement in various colleges")
        print("This Report is created by Aditi and Yanik Of Class XII A")
        break
# Additional commands used :
#def()Function
#split() function
#squeeze() function
#tolist() function
