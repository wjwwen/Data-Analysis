import csv

def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email
            })
        
append_data("data.csv", "Justin", "testing@gmail.com")