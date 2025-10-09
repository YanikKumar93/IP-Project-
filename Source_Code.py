import matplotlib.pyplot as mp
import pandas as pd
pd.set_option('display.max_rows', 20)  # Show a maximum of 20 rows
pd.set_option('display.max_columns', 15)  # Show all columns (assuming max 15)
pd.set_option('display.width', 1000)  # Set console width for better alignment
pd.set_option('display.float_format', '{:.2f}'.format)  # Show floats with 2 decimal places
print("=" * 70)
print("             📊 Welcome to The College Placement Analysis Report 🎓")
print("=" * 70)
print("\nThe given report consists of the following dataset features:\n"
      "\t1.  University Name (approx. 200)\n"
      "\t2.  UG and PG placement counts\n"
      "\t3.  Job Placement percentage\n"
      "\t4.  Number of males and females placed\n"
      "\t5.  Highest package obtained (in LPA)\n"
      "\t6.  Average package received (in LPA)\n"
      "\t7.  Count of international and domestic packages\n"
      "\t8.  Number of domains offered\n"
      "\t9.  College Location\n"
      "\t10. Top companies that visited\n")
print("-" * 70)
Main_Table = pd.read_csv(r"C:\Users\USER-9\Desktop\List_colleges.csv")
Main_Table = Main_Table.drop("S. No.", axis=1)
def Input(user, defined_range):
    try:
        user_input = int(user)
        if user_input in defined_range:
            return user_input
        else:
            print(f"⚠️ Please enter a valid choice from the given options,\n")
    except:
        print("⚠️ Please enter a valid integer choice.\n")
Choice_offered = ("Please make the choice for the columns from the below options:\n "
                  "\t\t1.  Highest Package (LPA)\n"
                  "\t\t2.  Domestic Package (LPA)\n"
                  "\t\t3.  International Package (LPA)\n"
                  "\t\t4.  No. Of Males Placed \n"
                  "\t\t5.  No. Of Females Placed\n"
                  "\t\t6.  Average Package Offered\n"
                  "\t\t7.  Job Placement Percentage\n"
                  "\t\t8.  Location\n"
                  "\t\t9.  Companies Visited\n"
                  "\t\t10. No. Of Domains Offered\n"
                  "\t\t11. UG Placements\n"
                  "\t\t12. PG Placements\n")
while True:
    print("\n" + "=" * 30 + " MAIN MENU " + "=" * 30)
    print("How do you want to see your report:\n"
          "\t1. Data of colleges\n"
          "\t2. Visual Representation\n"
          "\t3. Mathematical calculations\n"
          "\t4. Find a college from its location\n"
          "\t5. Find the colleges visited by a particular company\n"
          "\t6. View full table\n"
          "\t7. Exit\n")
    command_1 = input("Please enter your choice : ")
    command_1 = Input(command_1, [1, 2, 3, 4, 5, 6, 7])
    if command_1 == 1:
        while True:
            print("\n" + "-" * 25 + "🏢🏤 DATA OPTIONS 🏢🏤" + "-" * 25)
            print("Options:\n"
                  "\t1. Details of a particular College\n"
                  "\t2. Details of a Group of Columns\n"
                  "\t3. Back\n")
            command_2 = input("Please enter your choice : ")
            command_2 = Input(command_2, [1, 2, 3])
            if isinstance(command_2, int):
                if command_2 == 1:
                    Name_of_college = input("Please enter the name of the college : ")
                    Name_of_college_renewed = Name_of_college.upper()
                    if Name_of_college_renewed in Main_Table["Name of College"].values:
                        print("\n" + "*" * 20 + "The details of the college ", Name_of_college + "*" * 20)
                        pd.set_option('display.max_columns', None)
                        print(Main_Table[Main_Table["Name of College"] == Name_of_college_renewed], "\n")
                        print("*" * 55 + "\n")
                        print("Do you want see the graph of the selected: \n"
                              "\t\t1. Yes ✅\n"
                              "\t\t2. No  ❌ \n")
                        print("****** Please enter the number of the choice of your wish ******\n\n")
                        graph_input = input("Please enter here :")
                        graph_input = Input(graph_input, [1, 2])
                        if isinstance(graph_input, int):
                            if graph_input == 1:
                                print("\nThanks for the confirmation !!!!\n")
                                print(Choice_offered)
                                Number_of_columns = (input("No. of columns you want to see (Range 1-12):"))
                                if isinstance(Number_of_columns, int):
                                    list_columns = []
                                    limit_1 = 0
                                    while limit_1 < Number_of_columns:
                                        column_input = input(f"Please enter your choice of column {limit_1 + 1} :")
                                        column_input = Input(column_input, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                                        if isinstance(column_input, int):
                                            if Main_Table.columns[column_input + 1] not in list_columns:
                                                list_columns.append(Main_Table.columns[column_input + 1])
                                                limit_1 += 1
                                            else:
                                                print(f"⚠️'{Main_Table.columns[column_input + 1]}'already selected.Please choose a different column.")
                                                continue
                                        else:
                                            print("⚠️ Please enter a valid integer choice ⚠️\n")
                                            continue
                                        values = []
                                        for i in list_columns:
                                            values.append(Main_Table.loc[Main_Table["Name of College"] == Name_of_college_renewed, i].values.squeeze())
                                        mp.bar(list_columns,values,
                                               color='k', edgecolor='w', alpha=0.5, linewidth=2)
                                        mp.title(Name_of_college)
                                        mp.xlabel("Data")
                                        mp.xticks(rotation=90)
                                        mp.ylabel("Values")
                                        mp.show()
                                elif graph_input == 2:
                                    print("Thanks for the confirmation !!!")
                                    break
                                else:
                                    print("\n ⚠️ Please enter a valid integer choice ⚠️\n")
                                    continue
                        else:
                            print("\n ⚠️ Please enter a valid integer choice ⚠️\n")
                    else:
                        print(f"❌ College '{Name_of_college}' not found.\n")
                elif command_2 == 2:
                    Number_of_columns = input("Please enter the number of columns you want to see(in range 1-12) : ")
                    Number_of_columns_1 = Input(Number_of_columns, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                    if isinstance(Number_of_columns_1, int):
                        print(Choice_offered)
                        list_columns_1 = ["Name of College"]
                        limit = 0
                        while limit < Number_of_columns_1:
                            column_input = input(f"Please enter your choice of column {limit + 1} :")
                            column_input = Input(column_input, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                            if isinstance(column_input,int):
                                if Main_Table.columns[column_input + 1] not in list_columns_1:
                                    list_columns_1.append(Main_Table.columns[column_input + 1])
                                    limit += 1
                                else:
                                    print(f"⚠️ '{Main_Table.columns[column_input + 1]}' already selected. Please choose a different column.")
                                    continue
                            else:
                                continue
                        pd.set_option('display.max_columns', None)
                        print("\n" + "=" * 20 + "✅ SELECTED COLUMNS DATA ✅" + "=" * 20)
                        print(Main_Table[list_columns_1])
                        print("=" * 63 + "\n")
                        if Number_of_columns_1 == 1:
                            if column_input in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
                                print("Do you want see the graph of the selected: \n"
                                      "\t\t1. Yes ✅\n"
                                      "\t\t2. No  ❌ \n")
                                print("****** Please enter the number of the choice of your wish ******\n\n")
                                graph_input = input("Please enter here :")
                                graph_input = Input(graph_input, [1, 2])
                                if isinstance(graph_input, int):
                                    if graph_input == 1:
                                        print("🙂 Thanks for the confirmation !!!! 🙂\n")
                                        print("For which colleges do you want to see the graph :\n"
                                              "\t\t1.Top colleges\n"
                                              "\t\t2.Bottom most colleges\n"
                                              "\t\t3.Customised (You have to input the name of college)\n")
                                        print("****** The columns will be arranged in ascending order of your preferred row choice ******")
                                        College_option = input("Please enter the number of your choice :")
                                        College_option = Input(College_option, [1, 2, 3])
                                        print("Which type of graph do you want see : \n"
                                              "\t\t1. Bar graph 📊\n"
                                              "\t\t2. Scattered plot\n"
                                              "\t\t3. Line graph 📈\n")
                                        print("****** Please enter the number of the choice of your wish ******\n\n")
                                        graph_main = input("Which type of graph do you want to see : ")
                                        graph_main = Input(graph_main, [1, 2, 3, 4, 5, 6])
                                        Main_Table_sorted = Main_Table.sort_values(by=list_columns_1[-1],ascending=True)
                                        if isinstance(graph_main,int):
                                            if College_option == 1:
                                                top_rows = input("Please enter the no. of rows from the top you want to opt for : ")
                                                top_rows = Input(top_rows, range(1, 203))
                                                series = Main_Table_sorted["Name of College"].head(top_rows)
                                                list_college_top_1 = series.tolist()
                                                if graph_main == 1:
                                                    mp.bar(list_college_top_1,
                                                           Main_Table_sorted[list_columns_1[-1]].head(top_rows),
                                                           color = 'k',edgecolor ='w' ,alpha =0.5 ,linewidth =2)
                                                    mp.title(f"{list_columns_1[-1]} of top {top_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.xticks(rotation=90)
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.show()
                                                elif graph_main == 2:
                                                    mp.scatter(list_college_top_1,
                                                               Main_Table_sorted[list_columns_1[-1]].head(top_rows),
                                                               color ='y' ,alpha =0.5 ,marker ='p')
                                                    mp.title(f"{list_columns_1[-1]} of top {top_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.xticks(rotation=90)
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.show()
                                                elif graph_main == 3:
                                                    mp.plot(list_college_top_1,
                                                            Main_Table_sorted[list_columns_1[-1]].head(top_rows),
                                                            color = 'g',linestyle = ':',marker = "X",linewidth =2 )
                                                    mp.title(f"{list_columns_1[-1]} of top {top_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.xticks(rotation=90)
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.show()
                                                else:
                                                    print("⚠️ Invalid Choice ⚠️")
                                            elif College_option == 2:
                                                bottom_rows = input(
                                                    "Please enter the no. of rows from the bottom you want to opt for :")
                                                bottom_rows = Input(bottom_rows, range(1, 203))
                                                series_tail = Main_Table_sorted["Name of College"].tail(bottom_rows)
                                                list_college_bottom = series_tail.tolist()
                                                if graph_main == 1:
                                                    mp.bar(list_college_bottom,
                                                           Main_Table_sorted[list_columns_1[-1]].tail(bottom_rows),
                                                           color = 'c',edgecolor ="k" ,alpha =0.5 ,linewidth =2 )
                                                    mp.title(f"{list_columns_1[-1]} of bottom {bottom_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.xticks(rotation=90)
                                                    mp.show()
                                                elif graph_main == 2:
                                                    mp.scatter(list_college_bottom,
                                                               Main_Table_sorted[list_columns_1[-1]].tail(bottom_rows),
                                                               color = 'b',alpha =0.5 ,marker ="D")
                                                    mp.title(f"{list_columns_1[-1]} of bottom {bottom_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.xticks(rotation=90)
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.show()
                                                elif graph_main == 3:
                                                    mp.plot(list_college_bottom,
                                                            Main_Table_sorted[list_columns_1[-1]].tail(bottom_rows),
                                                            color ='g' ,linestyle =":" ,marker ="d" ,linewidth = 2)
                                                    mp.title(f"{list_columns_1[-1]} of bottom {bottom_rows} Colleges")
                                                    mp.xlabel("Colleges")
                                                    mp.xticks(rotation=90)
                                                    mp.ylabel(list_columns_1[-1])
                                                    mp.show()
                                                else:
                                                    print("⚠️ Invalid Choice ⚠️")
                                            elif College_option == 3:
                                                x_labels = []
                                                x = input("Please enter the number of rows you want to opt for (in range 1-203) :")
                                                custom_rows = Input(x, range(1, 203))
                                                if isinstance(custom_rows,int):
                                                    college = 0
                                                    while college < custom_rows :
                                                        x_n = input(f"Please enter the name of the college{college + 1} : ")
                                                        x_n_1 = x_n.upper()
                                                        if x_n_1 in Main_Table["Name of College"].values:
                                                            x_labels.append(x_n_1)
                                                            college += 1
                                                        else:
                                                            print("⚠️ Please enter a valid college name ⚠️\n")
                                                            continue
                                                    y_values = []
                                                    for j in x_labels:
                                                        row = Main_Table.loc[Main_Table['Name of College'] == j,list_columns_1[-1]].values[0]
                                                        y_values.append(row)
                                                    if graph_main == 1:
                                                        mp.bar(x_labels,
                                                               y_values,
                                                               color = 'r',edgecolor ="y" ,alpha =0.5,linewidth =2 )
                                                        mp.title(f"{list_columns_1[-1]} of {custom_rows} Colleges")
                                                        mp.xlabel("Colleges")
                                                        mp.ylabel(list_columns_1[-1])
                                                        mp.xticks(rotation=90)
                                                        mp.show()
                                                    elif graph_main == 2:
                                                        mp.scatter(x_labels,
                                                                   y_values,
                                                                   color ='k' ,alpha =0.5 ,marker ="^")
                                                        mp.title(f"{list_columns_1[-1]} of {custom_rows} Colleges")
                                                        mp.xlabel("Colleges")
                                                        mp.xticks(rotation=90)
                                                        mp.ylabel(list_columns_1[-1])
                                                        mp.show()
                                                    elif graph_main == 3:
                                                        mp.plot(x_labels,
                                                                y_values,
                                                                color ='p' ,linestyle = "--",marker ="v" ,linewidth = 2)
                                                        mp.title(f"{list_columns_1[-1]} of {custom_rows} Colleges")
                                                        mp.xlabel("Colleges")
                                                        mp.xticks(rotation=90)
                                                        mp.ylabel(list_columns_1[-1])
                                                        mp.show()
                                                    else:
                                                        print("⚠️ Invalid Choice ⚠️")
                                                else:
                                                    print("⚠️ Invalid choice ⚠️")
                                        else:
                                            pass
                                    elif graph_input == 2:
                                        print("🙂 Okay !!!! 🙂\n")
                elif command_2 == 3:
                    break
                else:
                    pass
    elif command_1 == 2:
        while True:
            print("\n" + "-" * 25 + "🎨 VISUALIZATION OPTIONS 🎨" + "-" * 25)
            print(Choice_offered, "\t\t13. Back\n\n")
            Column_command_2 = input("Please enter the column number from the list for which you want to see the graph : ")
            Column_command_2 = Input(Column_command_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
            if isinstance(Column_command_2, int):
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
                if Column_command_2 == 13:
                    break
                List_columns_selected.append(List_columns_new[Column_command_2 - 1])
                print(List_columns_selected)
                if Column_command_2 != 8 or Column_command_2 != 9:
                    print("For which colleges do you want to see the graph :\n"
                          "\t\t1.Top colleges\n"
                          "\t\t2.Bottom most colleges\n"
                          "\t\t3.Customised\n"
                          "****** The columns will be arranged in ascending order of your preferred row choice ******")
                    College_option_1 = input("Please enter the number of your choice :")
                    College_option_1 = Input(College_option_1, [1, 2, 3])
                    if isinstance(College_option_1,int):
                        print("Which type of graph do you want see : \n"
                              "\t\t 1. Bar graph 📊 \n"
                              "\t\t 2. Scattered plot\n"
                              "\t\t 3. Line graph 📈\n")
                        print("****** Please enter the number of the choice of your wish ******\n\n")
                        graph_main_1 = input("Which type of graph do you want to see : ")
                        graph_main_1 = Input(graph_main_1, [1, 2, 3])
                        Main_Table_sorted_new_1 = Main_Table.sort_values(by=List_columns_selected[-1],ascending=True)
                        if isinstance(graph_main_1,int):
                            if College_option_1 == 1:
                                top_rows_new = input("Please enter the rows from the top you want to opt for (in range 1-200) : ")
                                top_rows_new = Input(top_rows_new, range(1, 203))
                                series = Main_Table["Name of College"].head(top_rows_new)
                                list_college_top = series.tolist()
                                if isinstance(top_rows_new,int):
                                    if graph_main_1 == 1:
                                        mp.bar(list_college_top,
                                               Main_Table_sorted_new_1[List_columns_selected[-1]].head(top_rows_new),
                                               color ='b' ,edgecolor ='w',alpha = 0.5 ,linewidth = 2 )
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 2:
                                        mp.scatter(list_college_top,
                                                   Main_Table_sorted_new_1[List_columns_selected[-1]].head(top_rows_new),
                                                   color = 'm',alpha = 0.5 ,marker ="o")
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 3:
                                        mp.plot(list_college_top,
                                                Main_Table_sorted_new_1[List_columns_selected[-1]].head(top_rows_new)
                                                ,color ='g' ,linestyle = ':',marker = '*',linewidth = 2)
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    else:
                                        print("⚠️ Invalid Choice ⚠️")
                            elif College_option_1 == 2:
                                bottom_rows_new = input("Please enter the rows from the bottom you want to opt for (in range 1-200) :")
                                bottom_rows_new = Input(bottom_rows_new, range(1, 203))
                                series_tail = Main_Table["Name of College"].tail(bottom_rows_new)
                                list_college_bottom_1 = series_tail.tolist()
                                if isinstance(bottom_rows_new,int):
                                    if graph_main_1 == 1:
                                        mp.bar(list_college_bottom_1,
                                               Main_Table_sorted_new_1[List_columns_selected[-1]].tail(bottom_rows_new),
                                               color ='b' ,edgecolor = 'm',alpha = 0.5,linewidth =2)
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 2:
                                        mp.scatter(list_college_bottom_1,
                                                   Main_Table_sorted_new_1[List_columns_selected[-1]].tail(bottom_rows_new),
                                                   color = 'b',alpha = 0.5,marker ='H')
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 3:
                                        mp.plot(list_college_bottom_1,
                                                Main_Table_sorted_new_1[List_columns_selected[-1]].tail(bottom_rows_new),
                                                color = 'r',linestyle = '-.',marker ='h' ,linewidth = 2)
                                        mp.title(f"Graph of : Top colleges vs {List_columns_new[Column_command_2 - 1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    else:
                                        print("⚠️ Invalid Choice ⚠️")
                            elif College_option_1 == 3:
                                x_labels_1 = []
                                x = input("Please enter the number of rows you want to opt for (in range 1-200) :")
                                custom_rows_1 = Input(x, range(1, 203))
                                if isinstance(custom_rows_1,int):
                                    college_1 = 0
                                    while college_1 < custom_rows_1:
                                        x_n = input(f"Please enter the name of the college {college_1 + 1} : ")
                                        x_n_1 = x_n.upper()
                                        if x_n_1 in Main_Table["Name of College"].values:
                                            x_labels_1.append(x_n_1)
                                            college_1 += 1
                                        else:
                                            print("⚠️ Please enter a valid college name ⚠️\n")
                                            continue
                                    y_values_1 = []
                                    for j in x_labels_1:
                                        row = Main_Table.loc[Main_Table['Name of College'] == j,List_columns_selected[-1]].values[0]
                                        y_values_1.append(row)
                                    if graph_main_1 == 1:
                                        mp.bar(x_labels_1,
                                               y_values_1,
                                               color = 'k',edgecolor ='b' ,alpha =0.5,linewidth = 2)
                                        mp.title(f"Graph of :College vs {List_columns_selected[-1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 2:
                                        mp.scatter(x_labels_1,y_values_1,color = 'c',alpha =0.5 ,marker =2)
                                        mp.title(f"Graph of : College vs {List_columns_selected[-1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    elif graph_main_1 == 3:
                                        mp.plot(x_labels_1,
                                                y_values_1,
                                                color = 'y',linestyle ='--' ,marker =3 ,linewidth =2 )
                                        mp.title(f"Graph of : College vs {List_columns_selected[-1]}")
                                        mp.xlabel("Colleges")
                                        mp.xticks(rotation=90)
                                        mp.ylabel(List_columns_selected[-1])
                                        mp.show()
                                    else:
                                        print("⚠️ Invalid Choice ⚠️")
                                else:
                                    print("⚠️ Invalid choice ⚠️")
                    else:
                        print("Sorry !! But we are unable to form the graph of the following dataset 😔")
    elif command_1 == 3:
        while True:
            print("\n" + "-" * 25 + "➗✖️ MATHEMATICAL OPTIONS ➕➖" + "-" * 25)
            print("\t\t1. Sum of values of a column\n"
                  "\t\t2. Average of a column\n"
                  "\t\t3. Maximum value of a column\n"
                  "\t\t4. Minimum value of a column\n"
                  "\t\t5. Median of a column\n"
                  "\t\t6. Mode of a column \n"
                  "\t\t7. Back\n\n")
            Maths_func_input = input("Please enter the number of the choice of your wish:")
            Maths_func_input = Input(Maths_func_input, [1, 2, 3, 4, 5, 6, 7])
            if isinstance(Maths_func_input, int):
                if Maths_func_input == 7:
                    break
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
                Column_input = input("Please enter the number of the column you opt for:")
                Column_input = Input(Column_input, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                if isinstance(Column_input,int):
                    List_columns = ["Highest Package (LPA)",
                                    "Domestic Package (LPA)",
                                    "International Package (LPA)",
                                    "Number of Males Placed",
                                    "Number of Females Placed",
                                    "Average Package Offered",
                                    "Job Placement Percentage",
                                    "Number of Domains Offered",
                                    "UG Placements",
                                    "PG Placements"]
                    Column = List_columns[Column_input - 1]
                    if Maths_func_input == 1:
                        print("-" * 25 + "The sum of the values of ", Column, " is :" + "-" * 25+ "\n")
                        print(Main_Table[Column].sum(), "\n\n")
                    elif Maths_func_input == 2:
                        print("-" * 25 + "The average of the values of ", Column, " is :"+"-" * 25 + "\n")
                        print(Main_Table[Column].mean(), "\n\n")
                    elif Maths_func_input == 3:
                        print("-" * 25 + "The maximum of the values of ", Column, " is :"+ "-" * 25 + "\n")
                        print(Main_Table[Column].max(), "\n\n")
                    elif Maths_func_input == 4:
                        print("-" * 25 + "The minimum of the values of ", Column, " is :" + "-" * 25+"\n")
                        print(Main_Table[Column].min(), "\n\n")
                    elif Maths_func_input == 5:
                        print("-" * 25 + "The Median of the values of ", Column, " is :" + "-" * 25 + "\n")
                        print(Main_Table[Column].median(), "\n\n")
                    elif Maths_func_input == 6:
                        print("-" * 25+"The Mode of the values of ", Column, " is :"+"-" * 25+"\n")
                        print(Main_Table[Column].mode(), "\n\n")
                    else:
                        print("⚠️ Please enter a valid choice ⚠️\n")
    elif command_1 == 4:
        print("\n" + "-" * 25 + "📍 SEARCHING COLLEGE WITH LOCATION 📍" + "-" * 25)
        location_list = []
        location_input = input("\nPlease enter the location for which you want to search for a college : ")
        location_input_new = location_input.upper()
        if isinstance(location_input,str):
            for i in range(len(Main_Table)):
                if location_input_new in Main_Table.loc[i, 'Location']:
                    y = Main_Table.loc[i, 'Name of College']
                    location_list.append(y)
            location_list_series = pd.Series(location_list)
            print(f"✅ Found {len(location_list)} College(s) at or near '{location_input_new}':")
            print(location_list_series, "\n\n")
    elif command_1 == 5:
        print("\n" + "-" * 25 + "💼 SEARCHING COLLEGE WITH COMPANY 💼" + "-" * 25)
        Company_input = input("Please enter the company for which you want to check the colleges : ")
        Company_input = Company_input.upper()
        list_company = []
        if isinstance(Company_input,str):
            for i in range(len(Main_Table)):
                if Company_input in Main_Table.loc[i, 'Companies Visited'].split(', '):
                    x = Main_Table.loc[i, 'Name of College']
                    list_company.append(x)
            list_company_series = pd.Series(list_company)
            print(f"✅ Company '{Company_input}' visited {len(list_company)} College(s):")
            print("-" * 75)
            print(list_company_series, "\n\n")
    elif command_1 == 6:
        print("\n" + "=" * 25 + "🙂 FULL TABLE DATA 🙂 " + "=" * 25)
        print(Main_Table)
        print("=" * 65 + "\n")
    elif command_1 == 7:
        print("\n" + "=" * 70)
        print(" "*10 + "🙏" * 20)
        print("End of analysis. Thank you for using the report analysis programme!")
        print("This report is created by Aditi and Yanik, Class XII A.")
        print(" "*10 + "🙏" * 20)
        print("=" * 70)
        break
# Additional commands used :
# def()Function
# isinstance() function
# split() function
# squeeze() function
# tolist() function
