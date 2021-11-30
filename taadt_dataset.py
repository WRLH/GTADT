import torch
import os
from PIL import Image
import numpy as np
from data.base_dataset import BaseDataset, get_transform
import random

class TaadtDataset(BaseDataset):
    def __init__(self, data_path_S, img_filename_S, data_path_T, img_filename_T, opt, isTrain):

        BaseDataset.__init__(self, opt)
        # initial file
        self.data_path_S = data_path_S
        self.data_path_T = data_path_T
        img_filepath_S = img_filename_S
        img_filepath_T = img_filename_T
        self.isTrain = isTrain


        self.img_filename_S = []
        self.img_filename_T = []

        self.labels_S = []
        self.labels_T = []

        self.lesions_S = []
        self.lesions_T = []

        self.flag_S = []
        self.flag_T = []

        fp_S = open(img_filepath_S, 'r')
        for line in fp_S.readlines():
            if self.isTrain:
                filename, label, lesion, flag = line.strip().split('  ')
                if flag == 'brown':
                    flag_num = 4
                elif flag == 'tanned':
                    flag_num = 5
                elif flag == 'intermediate':
                    flag_num = 6
                elif flag == 'light':
                    flag_num = 7
                self.flag_S.append(flag_num)
            else:
                filename, label, lesion = line.split()
            self.img_filename_S.append(filename)
            self.labels_S.append(int(label))
            self.lesions_S.append(int(lesion))
        fp_S.close()

        fp_T = open(img_filepath_T, 'r')
        for line in fp_T.readlines():
            if self.isTrain:
                filename, label, lesion, flag = line.strip().split('  ')
                if flag == 'brown':
                    flag_num = 4
                elif flag == 'tanned':
                    flag_num = 5
                elif flag == 'intermediate':
                    flag_num = 6
                elif flag == 'light' or flag == 'very_light':
                    flag_num = 7
                self.flag_T.append(flag_num)
            else:
                filename, label, lesion = line.split()
            self.img_filename_T.append(filename)
            self.labels_T.append(int(label))
            self.lesions_T.append(int(lesion))
        fp_T.close()

        self.img_filename_S = np.array(self.img_filename_S)
        self.img_filename_T = np.array(self.img_filename_T)
        self.labels_S = np.array(self.labels_S)
        self.labels_T = np.array(self.labels_T)
        self.lesions_S = np.array(self.lesions_S)
        self.lesions_T = np.array(self.lesions_T)
        self.flag_S = np.array(self.flag_S)
        self.flag_T = np.array(self.flag_T)



        self.A_size = len(self.img_filename_S)
        self.B_size = len(self.img_filename_T)

        btoA = self.opt.direction == 'BtoA'
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc  # get the number of channels of input image
        output_nc = self.opt.input_nc if btoA else self.opt.output_nc  # get the number of channels of output image

        self.transform_A = get_transform(self.opt, grayscale=(input_nc == 1))
        self.transform_B = get_transform(self.opt, grayscale=(output_nc == 1))

    def __getitem__(self, index):
        index_A = index % self.A_size
        A_name = self.img_filename_S[index_A]
        if self.opt.serial_batches:
            index_B = index % self.B_size
        else:
            index_B = random.randint(0, self.B_size - 1)
        B_name = self.img_filename_T[index_B]

        A_path = os.path.join(self.data_path_S, A_name)
        B_path = os.path.join(self.data_path_T, B_name)

        A_img = Image.open(A_path).convert('RGB')
        B_img = Image.open(B_path).convert('RGB')

        A_label = torch.from_numpy(np.array(self.labels_S[index_A]))
        B_label = torch.from_numpy(np.array(self.labels_T[index_B]))

        A_lesion = torch.from_numpy(np.array(self.lesions_S[index_A]))
        B_lesion = torch.from_numpy(np.array(self.lesions_T[index_B]))

        if self.isTrain:
            A_flag = torch.from_numpy(np.array(self.flag_S[index_A]))
            B_flag = torch.from_numpy(np.array(self.flag_T[index_B]))


        A = self.transform_A(A_img)
        B = self.transform_B(B_img)

        if self.isTrain:
            return {'A': A, 'B': B, 'A_paths': A_path, 'B_paths': B_path, 'A_labels': A_label, 'B_labels': B_label,
                    'A_lesions': A_lesion, 'B_lesions': B_lesion, 'A_flag': A_flag, 'B_flag': B_flag}
        else:
            return {'A': A, 'B': B, 'A_paths': A_path, 'B_paths': B_path, 'A_labels': A_label, 'B_labels': B_label, 'A_lesions':A_lesion, 'B_lesions': B_lesion}

    def __len__(self):
        if self.isTrain:
            return max(self.A_size, self.B_size)
        else:
            return self.B_size


