# 打开文件（w 表示写入模式，encoding 保证中文正常）
with open("Map-Generate\locations.csv", "w", encoding="utf-8") as f:
    # 写表头
    f.write("""Name,Disabled,TID,LocationTheme,SupportingCampaignGround,BannerOverrideSWF,BannerOverrideExportName,GameModeVariation,Map,CommunityCredit,TrainingGroundsEnabled,RecommendedBrawler0,RecommendedBrawler1,RecommendedBrawler2,RecommendedBrawler3,RecommendedBrawler4,RecommendedBrawler5,RecommendedBrawler6,RecommendedBrawler7,RecommendedBrawler8,RecommendedBrawler9
string,boolean,string,string,boolean,string,string,string,string,string,boolean,string,string,string,string,string,string,string,string,string,string\n""")

    # 写循环生成的行
    for n in range(200,500):
        f.write(f"Survival{n},,TID_BADAPPLE_{n},DefaultShowdown,,,,Showdown,Survival_{n},胡须局锦绣谷Hxjjxg,,,,,,,,,,,\n")
#请自行更改生成地图数量以及起始位置，渲染太多会卡。