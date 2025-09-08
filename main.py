# 在这个文件下编写代码，题目具体要求见README.md文件
# WeightConvert.py
WeightStr = input("请输入带有单位的重量值：")
if WeightStr[-2:] in ["kg"]:
    kg = eval(WeightStr[0:-2])
    pd = kg * 2.2046
    print("对应的英制重量是 {:.3f} 磅".format(pd))
elif WeightStr[-2:] in ["pd"]:
    pd = eval(WeightStr[0:-2])
    kg = pd / 2.2046
    print("对应的公制重量是 {:.3f} 千克".format(kg))
else:
    print("输入格式错误")
