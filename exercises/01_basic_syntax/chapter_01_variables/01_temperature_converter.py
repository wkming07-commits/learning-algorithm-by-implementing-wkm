"""
文件: 01_temperature_converter.py
功能: 摄氏温度转华氏温度
要点: input()返回字符串需显式转换、f-string格式化
日期: 2025-11-10
状态: 完成
"""



c = float(input("请输入摄氏温度："))
f = (c*9/5)+32
print(f"摄氏{c:.2f} = 华氏{f:.2f}")