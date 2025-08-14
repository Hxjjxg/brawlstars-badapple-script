import time

# === 参数 ===
frame_file = "Pre-Process/frames.txt"
frame_width = 60
frame_height = 45
fps = 10
frame_delay = 1.0 / fps

char_black = "#"
char_white = "."

# === 读取帧文件 ===
with open(frame_file, "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line or ":" not in line:
        continue

    label, data = line.split(":", 1)
    if len(data) != frame_width * frame_height:
        print(f"[跳过] {label} 长度不是 2700：{len(data)}")
        continue

    # 输出帧编号
    #print(f"\n{label}")
    print(f"\n")

    # 输出图像（60列 × 45行）
    for i in range(0, len(data), frame_width):
        row = data[i:i+frame_width]
        print(''.join(char_black if c == '1' else char_white for c in row))

    # 控制帧率
    #time.sleep(frame_delay)127.0.0.1:12346154.37.221.68:12346
