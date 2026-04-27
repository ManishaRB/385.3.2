import csv

file_path = 'data/country.csv'
with open(file_path, encoding='utf8') as f:
    csv_reader = csv.reader(f, delimiter=',')

    # Opening as a Dictionary but with custom field names
    field_names = ['Country Name', 'Area', 'Code2', 'Code3']
    with open(file_path, encoding='utf8') as f:
        csv_reader = csv.DictReader(f, field_names)

        for dict in csv_reader:
            print(dict)

    # for line in csv_reader:
    #     print(line)

    # for line_no, line in enumerate(csv_reader, 1):
    #     if line_no == 1:
    #         print("Header:")
    #         print(line) # This will print header
    #         print('Data:')
    #     else: # This will print the darn line
    #         print(line)

    # next() skips the first line and goes to next
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line)

    # Open csv as a dictionary
    # with open(file_path, encoding='utf8') as f:
    #     csv_reader = csv.DictReader(f)
    #     print(csv_reader)

    #     next(csv_reader)

    #     for dict in csv_reader:
    #         print(f'The area of {dict['name']} is {dict['area']} km2')

    


