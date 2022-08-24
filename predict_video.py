# 利用训练好的权重导入到网络中并测试视屏效果
# 而且能够在视屏中实时用绿线表示出显示后的效果
import cv2
import torch
import numpy as np
import net as N

def predict_video(video_path, result_video_path):
	"""
	功能：对视频进行预测并输出
	参数：
		video_path：要进行预测的视频路径
		result_video_path：预测结果的视频存放的路径
	"""

	# 设置批次数，为了能讲数据放入训练网络中
	batch_size = 1

	# 初始化文件名
	video = "first_video.mp4"
	result_video = "result_first_video_fast.mp4"

	# 加载权重
	net = torch.load("weight/weight.pkl")

	# 读取视屏
	cap = cv2.VideoCapture(video_path + video)

	# 获取视屏帧率
	fps_video = cap.get(cv2.CAP_PROP_FPS)
	print("fps_video={}".format(fps_video))

	# 设置写入视屏的编码格式
	fourcc = cv2.VideoWriter_fourcc(*"mp4v")
	print("fourcc={}".format(fourcc))

	# 获取视屏宽度和高度
	frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	print("frame_width={},frame_height{}".format(frame_width, frame_height))

	# 设置写视屏的对象
	videoWriter = cv2.VideoWriter(result_video_path + result_video, fourcc, fps_video, (frame_width, frame_height))

	while (cap.isOpened()):
		ret, frame = cap.read()

		# 如果视屏没有结束
		if ret == True:
			# 将图片进行剪切
			inputs = frame[420:670, 495:745]
			inputs = inputs.transpose(2, 1, 0)
			inputs = inputs / 255.0

			inputs = np.array([inputs])

			# 进行输入数据类型转换
			inputs = torch.from_numpy(inputs)
			inputs = inputs.float().cuda()

			# 得到预测数据
			predict = net(inputs)

			# 取最大值索引
			predict = torch.argmax(predict)

			# 判断预测的值并给文本变量赋予相应的状态
			if predict == 0:
				text = "The skip is not in position!"
			elif predict == 1:
				text = "The skip is discharging coal!"
			elif predict == 2:
				text = "The skip is in position!"

			# 在图片上显示红色文本
			cv2.putText(frame, text, (200, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (0, 0, 255), 5)

			# 在图片中显示出绿色的矩形框
			cv2.rectangle(frame, (495, 420), (745, 670), (0, 255, 0), 2, 4)

			# 显示视频
			cv2.imshow('Frame',frame)

			# 刷新视频
			cv2.waitKey(10)

			# 按q键退出
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break

			# 将图片写入视屏
			videoWriter.write(frame)
		else:
			# 写入视屏结束
			videoWriter.release()
			break