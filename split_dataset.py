import os
from sklearn.model_selection import train_test_split


def write_list(data_list, data_path, train=True):
    file_name = 'train.txt' if train else 'val.txt'
    with open(file_name, 'w') as f:
        for data_file in data_list:
            f.write(f'{data_path}/{data_file}\n')


image_list = list(filter(lambda x: 'jpg' in x, os.listdir('../data/A')))
train_list, test_list = train_test_split(image_list, test_size=0.2, random_state=2022)
write_list(train_list, '../data/A')
write_list(test_list, '../data/A', False)
