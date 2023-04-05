import csv

def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    cnt = 0
    x = 0
    lst = []
    
    f = open(data)
    reader = csv.reader(f)
    for i in reader:
        lst.append(i[0])
    while x < len(lst):
        x += 1
    return data, x
print(find_number_of_rows("data.csv"))
# Read the csv file
