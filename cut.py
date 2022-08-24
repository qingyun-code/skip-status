import cv2

def capture_video(video_path, result_video_path, video, result_video, start_time, end_time):
    """
    功能：截取短视频
    参数：
        video_path：需要截取的视频路径
        result_video_path：截取后的视频存放的路径
        video：需要截取的视频的名称（不带后缀）
        result_video：截取了的视频的名称（不带后缀）
        start_time：截取开始时间（单位s）
        end_time：截取结束时间（单位s）
    """

    # 打印出起始和结束时间
    print("The path of the video to be processed is:{}".format(video_path))
    print("start_time={}".format(start_time))
    print("end_time={}".format(end_time))

    # 读取视屏
    cap = cv2.VideoCapture(video_path + video)
    print("The video load was successful!")

    # 读取视屏帧率
    fps_video = cap.get(cv2.CAP_PROP_FPS)
    print("fps_video={}".format(fps_video))

    # 设置写入视屏的编码格式
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    print("fourcc={}".format(fourcc))

    # 获取视屏宽度和高度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("frame_width={},frame_height={}".format(frame_width, frame_height))

    # 设置写视屏的对象
    videoWriter = cv2.VideoWriter(result_video_path + result_video, fourcc, fps_video, (frame_width, frame_height))
    print("The object for writing video is set.")
    print("Will enter a loop to read frame images!")

    # 初始化一个计数器
    acount = 0

    print("It goes into the cycle!")

    while (cap.isOpened()):

        # 读取视屏里的图片
        ret, frame = cap.read()

        # 如果视屏没有读取结束
        if ret == True:

            # 计数器加一
            acount += 1

            # 截取相应时间内的视频信息
            if(acount > (start_time * fps_video) and acount <= (end_time * fps_video)):
                # 将图片写入视屏
                videoWriter.write(frame)

            if(acount == (end_time * fps_video)):
                print("The video was captured successfully!")
                print("The processed video is stored:{}".format(result_video_path))
                break

        else:
            # 写入视屏结束
            videoWriter.release()
            print("Start time or end time exceeds the video time!")
            print("Video capture failed!")
            break

if __name__ == '__main__':
    video_path = "jidou_video/"
    result_video_path = "video/"
    video = "wskip2020-12-03-20.mp4"
    result_video = "first_video.mp4"
    start_time = 5 * 60 + 30
    end_time = 6 * 60 + 30
    capture_video(video_path, result_video_path, video, result_video, start_time, end_time)