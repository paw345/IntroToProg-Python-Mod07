# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: program demonstrating pickling and structured error handling
# ChangeLog (Who,When,What):
#   Patrick Woodard,8/23/2021,initial release
# ------------------------------------------------------------------------ #

# Pseudo Code:
# Movie/Rating List Program
# 1) Show user menu of choices: read/add/save/exit
# 2a) Read existing data from binary file (rb)
#       catch error if file doesn't exist
# 2b) Append the "Working List":
#       use list of dictionaries [{Movie:XX, Rating:YY}]
#       catch error if Rating is not numeric
# 2c) Save list to binary file (wb)

import pickle #this allows us to use binary file

# DATA -------------------------------------------- #
movie_file = 'movie_ratings.dat'
movie_list = []

# PROCESSING -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    f = open(file_name, 'wb')  #file will be created if it doesn't exist
    pickle.dump(list_of_data, f)
    f.close()

def read_data_from_file(file_name):
    f = open(file_name, "rb")
    f_data = pickle.load(f)  # load() only loads one row of data.
    f.close()
    return f_data

def presentation_pause():
    input('\npress enter to continue')

# PRESENTATION and MAIN ------------------------------------ #
print('*'*5,' Welcome to the Movie/Rating List Program ','*'*5)

while(True):
    print("\nMENU:\n1=read list from file\n2=add new items to working list\n3=save working list\n4=exit\n")
    #print("Working List =", movie_list)
    count=0
    print('Working List:')
    for item in movie_list:
        print(movie_list[count])
        count+=1
    choice=input('\nEnter choice: ')

    if choice=='1':
        # read the data from the file into a new list object and display the contents
        try:
            movie_list=read_data_from_file(movie_file)
        except FileNotFoundError as e:
            print('\n***ERROR*** file does not exist')
            presentation_pause()

    elif choice == '2':
        movie_name = input("Enter movie title: ").title()
        try:
            movie_rating = float(input("Enter movie rating: "))
            dict_item = {'Movie':movie_name,'Rating':movie_rating}
            movie_list.append(dict_item)
        except ValueError as e:
            print('\n***ERROR*** rating must be numeric')
            presentation_pause()
    elif choice=='3':
        save_data_to_file(movie_file,movie_list)

    else: break