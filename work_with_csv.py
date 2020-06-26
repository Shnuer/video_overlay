import csv

### Opens the transferred file and gets the header and data from it ###
def get_data_from_csv(file_csv_name):

    with open(file_csv_name, encoding="utf-8") as csv_file:
            
        csv_read = csv.reader(csv_file, delimiter=';')

        _ = next(csv_read)

        for val in csv_read:
            yield val
        
def get_title_from_csv(file_csv_name):

    with open(file_csv_name, encoding="utf-8") as csv_file:
            
        csv_read = csv.reader(csv_file, delimiter=';')

        title = next(csv_read)

        return title 


if __name__ == "__main__":
    
    file_csv_name = 'Test_data.csv'
    title, data = get_title_from_csv(file_csv_name)
    print(title)
