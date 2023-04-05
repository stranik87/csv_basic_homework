import csv

def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    cnt = []
    f = open(data)
    reader = csv.reader(f)
    for row in reader:
        cnt.append(row[0])
        # print(row[0])
    return cnt[-1]
print(find_number_of_columns("data.csv"))


# Read the csv file