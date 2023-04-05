import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f = open(data)
   reader = csv.reader(f)
   for i in reader:
       print(i[1])
   
   return data

print(get_first_row("data.csv"))

# Read the csv file