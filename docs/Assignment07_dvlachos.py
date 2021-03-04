# ------------------------------------------------- #
# Title: Assignment07
# Description: Store data in a binary file, then retrieve the binary file
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script Lab7-1_Starter.py code
# DVlachos, 2.27.2021, Added Input prompt for user, added code to save data to file, added code to read data from file.
# DVlachos, 2.28.2021, Added while loop to read all of data in file
# DVlachos, 3.2.2021, Changed menu selections to 1 and 0. Add second error exceptions to choice
# DVlachos, 3.3.2021, Add comments where needed
# ------------------------------------------------- #
import pickle  # Access the pickle module

# Data -------------------------------------------- #
file_name = 'script.dat'
list_script = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # pass  # TODO: Add code here
    file_obj = open(file_name, "ab")
    pickle.dump(list_of_data, file_obj) # Save data to binary file
    file_obj.close()

def read_data_from_file(file_name):
    # pass  # TODO: Add code here
    output = []
    file_obj = open(file_name, "rb")
    while True:
        try: # Loop through until end of data structure in binary file
            output.append(pickle.load(file_obj)) # Read data from binary file and append to a list
        except EOFError:  # When the end of the file is detected break from loop
            break
    file_obj.close()
    return output

# TODO: Get ID and NAME From user, then store it in a list object
def get_input_from_user(list):
    char_name = str(input("\nCharacter: ")) # Prompt for user to add a user name
    char_line = input("Enter " + char_name + "'s line: ") # Prompt for user to add a line to a script
    row_list = [char_name, char_line] # Add variables to list
    list.append(row_list) # Append the list to a table
    return list

def input_choice():
    choice = int(input("\nWould you like to add lines to the script? [1 = Yes, 0 = No] "))
    return choice

def print_loaded_data(read_loaded_data):
    print("\nHere's the amazing script you have saved!")
    for row in read_loaded_data: # Loop through list and display it in a script format
        for col in row:
            print(str(col[0]) + ": " + col[1])

# Presentation ------------------------------------ #

read_loaded_data = read_data_from_file(file_name)
print_loaded_data(read_loaded_data)

while True:
    try: # Loop through prompting user for choice until user no longer wants to add more data
        choice = input_choice()
        if choice == 1: # User wants to add more data
            list_script = get_input_from_user(list_script) # Appends data to table
        elif choice == 0: # User no longer chooses to add data
            break
        else:
            print("Please enter the number 1 or 0.")
            continue
    except ValueError: # Will display error if not an int and loop back to ask for another input
        print("Oops. You entered a letter. Please enter the number 1 or 0.")
        continue


# TODO: store the list object into a binary file
save_data_to_file(file_name, list_script) # Save data to binary file
# TODO: Read the data from the file into a new list object and display the contents
read_loaded_data = read_data_from_file(file_name)
print_loaded_data(read_loaded_data) # Prints data from binary file