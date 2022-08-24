def image_tag(labels_path, start_number, end_number, skip_state):
	"""
	功能：对图片进行数据标定
	参数：
		labels_path：存放标签数据的路径
		start_number：开始标记数据号码
		end_number：结束标记号码
		skip_state：箕斗状态（有1、2、3）三种状态
	"""

	# 开始检索标定
	for i in range(end_number - start_number + 1):
		with open(labels_path + '%s.txt' % str(start_number + i), 'w') as out_file:
			if skip_state == 1:
				out_file.write(" ".join(['1', '0', '0']))
			elif skip_state == 2:
				out_file.write(" ".join(['0', '1', '0']))
			elif skip_state == 3:
				out_file.write(" ".join(['0', '0', '1']))

if __name__ == '__main__':
	labels_path = 'labels/'
	start_number = 1501
	end_number = 1675
	skip_state = 1
	image_tag(labels_path, start_number, end_number, skip_state)