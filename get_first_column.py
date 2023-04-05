import csv

def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f = open(data)
    reader = csv.reader(f)
    for i in reader:
        print(i[0])
    return data
    
print(get_first_column("data.csv"))
# Read the csv file