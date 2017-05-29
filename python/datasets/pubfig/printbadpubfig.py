import csv
import hashlib
import os
import sys

path = './dev'
folders = os.listdir(path)
data_file_name = 'dev_urls.txt'

# for folder in folders:
#     sub_folder = path + folder + '/'
#     if os.path.isdir(sub_folder):
#         for info in os.listdir(sub_folder):
#             record = sub_folder + archive

description_list = []
with open(data_file_name,'rt') as file_handle:
    csv_reader = csv.reader(file_handle, delimiter='\t')
    hashing_lib = hashlib.md5()

    # Skip first two rows
    next(csv_reader)
    next(csv_reader)
    # Start row reading
    for row in csv_reader:
        person_name = row[0]
        image_num = row[1]
        image_url = row[2]
        image_box = row[3]
        md5sum = row[4]

        folder = person_name.replace(' ', '_')
        image = image_num + '.jpg'
        file_path = path + '/' + folder + '/' + image
        if os.path.isfile(file_path):
            hashing_lib.update(file_path)
            hashing = hashing_lib.hexdigest()
            if hashing != md5sum:
                bad_path = path + '_bad'
                if not os.path.exists(bad_path):
                    os.mkdir(bad_path)
                bad_folder = bad_path + '/' + folder
                if not os.path.exists(bad_folder):
                    os.mkdir(bad_folder)
                print(file_path, hashing, md5sum)
                # old_file_path = path + '/' + folder + '/' + image
                # new_file_path = bad_path + '/' + folder + '/' + image
                # os.rename(old_file_path, new_file_path)
        else:
            print(file_path + ' does not exist.')

