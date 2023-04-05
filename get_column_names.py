import csv
#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    lst = []
    f = open(data)
    reader = csv.reader(f)
    for i in reader:
        lst.append(i)
    return lst[0]
    
print(get_column_names("data.csv"))
# Read the csv file