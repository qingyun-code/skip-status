def write_data(file_path, file_type, number):
	"""
	功能：将需要训练的数据的文件名写入文档中
	参数：
		file_path：训练文件名集存放的路径
		file_type：文件类型，主要有训练和测试两种
		number：需要用到的文件个数
	"""
	with open(file_path + '%s.txt' % (file_type), 'w') as out_file:
		for i in range(number):
			out_file.write(str(i + 1) + '\n')

if __name__ == '__main__':
	file_path = 'ImageSets/Main/'
	file_type = 'train'
	number = 1675
	write_data(file_path, file_type, number)