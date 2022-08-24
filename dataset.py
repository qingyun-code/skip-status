import cv2
import numpy as np
from torch.utils.data import Dataset

class dataset(Dataset):
	def __init__(self, is_train = True):
		# 设置存储着文件名的列表
		self.file_names = []

		# 如果是要进行训练读取训练数据文档，否则读取验证数据文档
		if is_train:

			# 将训练数据的文档名存储到文件列表中,.strip()去除字符串前后的空格或换行符
			with open("ImageSets/Main/train.txt", 'r') as f:
				self.file_names = [x.strip() for x in f]
		else:

			# 将验证数据的文档名存储到文件列表中
			with open("ImageSets/Main/val.txt", 'r') as f:
				self.file_names = [x.strip() for x in f]

		# 图片存储路径
		self.img_path = "image/"

		# label数据文档存储数据
		self.label_path = "labels/"

	def __len__(self):
		'''
		功能：返回文件名的个数
		'''
		# 返回文件名的个数
		return len(self.file_names)

	def __getitem__(self, item):
		'''
		功能：对图像数据进行规范化处理
		参数：
		——picture_index：图片在文件名当中的索引
		'''
		img = cv2.imread(self.img_path + self.file_names[item] + '.jpg')

		# 将图片进行裁剪，h(420~670)，w(495~745)
		img = img[420:670, 495:745]

		# 将原图片中的(h,w,c)转换成(c,w,h)
		img = img.transpose(2, 1, 0)

		# 将图片进行归一化
		img = img / 255.

		with open(self.label_path + self.file_names[item] + ".txt") as f:

			# 将.txt文档中的内容放入列表中
			line = [x.split() for x in f]
			label = [float(x) for y in line for x in y]

		labels = np.zeros((3))

		labels[0:3] = np.array([label[0], label[1], label[2]])

		return img, labels