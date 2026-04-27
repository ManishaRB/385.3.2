import csv
# open the file in read mode
# encoding="utf8" ensures that the file is read using UTF-8 encoding, which supports a wider range of characters.
# update the file path as per our system
file_path = 'data/country.csv'
with open(file_path, encoding='utf8') as f:
    # create the csv reader object and delimiter is comma
     csv_reader = csv.reader(f, delimiter=',')
    # loop through the file object and read the content
     for line in csv_reader:
        print(line)


# Opening as a Dictionary but with custom field names
# field_names = ['Country Name', 'Area', 'Code2', 'Code3']
# with open(file_path, encoding='utf8') as f:
#     csv_reader = csv.DictReader(f, field_names)

#     for dict in csv_reader:
#         print(dict) 

    
# The country.csv has the first line as the header. To separate the header and data, you use the enumerate() function to get the index of each line:
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

# The following example uses the DictReader class to read the country.csv file:
# Open csv as a dictionary
# with open(file_path, encoding='utf8') as f:
#     csv_reader = csv.DictReader(f)
#     print(csv_reader)

#     next(csv_reader)

#     for dict in csv_reader:
#         print(f'The area of {dict['name']} is {dict['area']} km2')

    


