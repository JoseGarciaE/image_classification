import numpy as np

import os
import cv2

import torch
from torch.utils.data import Dataset, DataLoader, random_split

from sklearn.model_selection import train_test_split


class createData(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __get__item(self, index):
        return self.data[index], self.labels[index]

if __name__ == '__main__':
    
    photos_path = './photos/'

    # lists to hold each data value and their respective label
    data, labels = [], []

    # re-sizing images and extracting RGB
    for dir in os.listdir(photos_path):
        for file in os.listdir(os.path.join(photos_path, dir)):
            img = cv2.imread(os.path.join(photos_path, dir, file))
            img = cv2.resize(img, dsize=(50,100))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            data.append(img)
            labels.append(dir)

    # split data 
    data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size= 1/3, random_state=0)
    
    
    



