# Pre-process

## 功能
- 将 Bad Apple 视频转换成帧数据。

- 由于bs的地图为60×60 而Bad Apple视频为4：3，故转化为60×45的分辨率。

## 主要文件
- main.py 主要处理视频，按每3帧取1帧的速度取帧，并缩放为60*45，二值化后提取0/1，按位存储在frames.txt中

- replaytest.py 仅验证是否正常提取帧数据