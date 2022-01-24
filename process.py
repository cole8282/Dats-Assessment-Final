# opening access to the data in the txt file
log_file = open("um-server-01.txt")
# creating a function that takes in one parameter for the data in the .txt file
def sales_reports(log_file):
 # itterating over each line in the .txt file
    for line in log_file:
        # deleting blank space at the end of each line of string
        line = line.rstrip()
        # assigning a variable a string of each line starting at index zero and ending at index 3, which will be each lines day of the week
        day = line[0:3]
        # checking if the day is monday and will print the entire line if so
        if day == "Mon":
            print(line)

# invokes the function sales_reports
sales_reports(log_file)
