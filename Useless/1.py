import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import re

# 读取文件
with open('1.txt', encoding='utf-8') as f:
    lines = f.readlines()

# 解析ob为true的坐标
# 解析ob为true的坐标
ob_line = lines[0]
ob_json_str = re.search(r'(\{.*\})', ob_line).group(1)
ob_json_str = ob_json_str.replace('""', '"')  # ← 这里是新增的
ob_data = json.loads(ob_json_str)
ob_coords = set((d['x'], d['y']) for d in ob_data['data'] if d.get('ob'))
# 解析地图字符矩阵
# 解析地图字符矩阵
map_lines = [line.split(',')[1].strip().replace('"', '') for line in lines[1:61]]
map_lines = [line.ljust(60) for line in map_lines]  # 补齐到60字符
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(0, 60)
ax.set_ylim(0, 60)
ax.set_xticks(range(61))
ax.set_yticks(range(61))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)

# 绘制格子
for y in range(60):
    for x in range(60):
        try:
            char = map_lines[y][x]
        except IndexError:
            char = ' '
        if (x, y) in ob_coords:
            rect = patches.Rectangle((x, 59-y), 1, 1, linewidth=0, edgecolor=None, facecolor='yellow')
            ax.add_patch(rect)
        ax.text(x+0.5, 59-y+0.5, char, va='center', ha='center', fontsize=8, color='black')
        
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()