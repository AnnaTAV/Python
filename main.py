from os.path import exists
from HomeTask7.csv_creater import createre
from HomeTask7.write_creater import write_csv
from HomeTask7.write_creater import write_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    createre()

write_csv()
write_txt()
