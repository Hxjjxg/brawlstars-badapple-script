# Map-generate

## Showmap.py
读取Map.txt并渲染，方便一眼判断地图是什么

Map.txt：使用官方.csv文件的格式
## .csv
maps_ori.csv  locations_ori.csv game_varitation.csv location_themes.csv安装包的原文件
- -ori是加的后缀 即original

## maps.py
先生成好2000张地图
（去掉了原本的官图，所以会出现奇怪的bug（比如点进选模式的界面会闪退））

## locations.py
友谊战界面（大概是）先去寻找game_varitation寻找显示哪些模式，每个模式（应该是）按照locations.csv的顺序渲染。

对于一行locations.csv,先看是否Disabled（false应该可省略（初始值为0））。TID去\assets\localization\cn.csv找对应的中文。LocationTheme应该是去location_themes.csv中找对应文件（不过我们不管，直接全改成DefaultShowdown就行了（））。GameModeVariation对应game_mode_variations.csv的模式名称。Map对应maps.csv的地图名。CommunityCredit对应作者名。TrainingGroundsEnabled这啥我不到啊，好像顺手给把true删掉了没太大问题。

