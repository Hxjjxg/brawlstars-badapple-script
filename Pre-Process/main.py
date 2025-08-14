import cv2

# 参数设置
video_path = "Pre-Process/badapple.mp4"   # 输入视频路径
output_file = "Pre-Process/frames.txt"     # 输出文件名
target_width = 60
target_height = 45
extract_fps = 10               # 想要的帧率

# 打开视频
cap = cv2.VideoCapture(video_path)

original_fps = cap.get(cv2.CAP_PROP_FPS)

frame_interval = int(original_fps / extract_fps)  # 每几帧取一帧

frame_index = 0
saved_frame_count = 0

with open(output_file, "w") as f:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 每隔 frame_interval 帧取一次
        if frame_index % frame_interval == 0:
            # 灰度化并缩放
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (target_width, target_height), interpolation=cv2.INTER_NEAREST)

            # 二值化（黑白）
            _, binary = cv2.threshold(resized, 128, 1, cv2.THRESH_BINARY)

            # 展平成字符串（2700 个 0/1）
            flat = binary.flatten()
            binary_str = ''.join(str(x) for x in flat)

            # 写入文件
            f.write(f"frame{saved_frame_count:04d}:{binary_str}\n")
            saved_frame_count += 1

        frame_index += 1

cap.release()
print(f"每秒取 {extract_fps} 帧，已保存 {saved_frame_count} 帧到 {output_file}")
