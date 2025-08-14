#这个文件和map.txt无关

input_file = "Pre-Process\frames.txt"
output_file = "Map-Generate\maps.csv"
DOT_LINE = ',"' + '.' * 60 + '",\n'

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("Map,Data,MetaData\nString,String,String\n")

    for line in f_in:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("frame") and ":" in line:
            frame_name, data = line.split(":", 1)
            frame_number = str(int(frame_name.replace("frame", "")))
            
            # 只取前 2700 个字符，防止溢出
            data = data[:2700]
            
            # 替换 0→w, 1→x
            converted = data.replace("0", "w").replace("1", "z")
            
            # 第一行单独处理（与帧名同一行）
            first_chunk = converted[0:60]
            f_out.write(f'"Survival_{frame_number}"' + f',"{first_chunk}",\n')
            
            # 余下 44 行
            for i in range(60, len(converted), 60):
                chunk = converted[i:i+60]
                f_out.write(f',"{chunk}",\n')

                        # 每帧结束后加 15 行点线
            for _ in range(15):
                f_out.write(DOT_LINE)