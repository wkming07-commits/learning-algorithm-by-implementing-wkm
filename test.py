# import sys
# print(f"Python路径: {sys.executable}")

# # 测试所有库
# try:
#     import numpy as np
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     from sklearn.datasets import load_iris
#     import jupyter
    
#     print("✅ 所有AI库导入成功！")
    
#     # 功能测试
#     iris = load_iris()
#     print(f"✅ 数据集: {iris.data.shape}")
    
#     arr = np.array([1, 2, 3])
#     print(f"✅ NumPy: {arr.sum()}")
    
#     print("🎉 环境配置完全成功！")
    
# except ImportError as e:
#     print(f"❌ 错误: {e}")


# 实验不同类型的字符串
# name = "张三"
# path = r"D:\nus_ai_projects"
# binary = b"data"
# multiline = """第一行
# 第二行
# 第三行"""

# print(f"姓名: {name}")
# print(f"路径: {path}") 
# print(f"二进制: {binary}")
# print(f"多行文本:\n{multiline}")


# try:
#     num = int(input("请输入数字: "))
# except ValueError as e:
#     print(f"发生错误: {e}")  # 显示具体的错误信息

# for i in range (1,2):
#     print("i =", i)
    
# def validate_age(age):
#     if age < 0 or age > 150:
#         raise ValueError("年龄必须在0到150之间")
#     return True

# # 测试
# try:
#     validate_age(200)  # 这里会抛出 ValueError
# except ValueError as e:
#     print(f"捕获到错误: {e}")  # 输出: 捕获到错误: 年龄必须在0到150之间

# def pyramid_factory():
#     while True:
#         print("请选择金字塔模式：")
#         print("1. 左对齐金字塔")
#         print("2. 居中金字塔") 
#         print("3. 倒三角金字塔")
#         print("4. 数字递增金字塔")

#         while True:
#             try:
#                 choice = input("输入选项 (1-4): ").strip()
#                 choice = int(choice) 
#                 if choice not in [1, 2, 3, 4]:
#                     raise ValueError("无效选项，请选择1到4之间的数字。")
#                 break
#             except ValueError as e:
#                 print(f"错误: {e}")
                
#             print(f"你选择了模式 {choice}")
#         while True:
#             try:
#                 levels = input("请输入金字塔层数 (1-9): ").strip()
#                 levels = int(levels)
#                 if levels < 1 or levels > 9:
#                     raise ValueError("层数必须在1到9之间。")
#                 break
#             except ValueError as e:
#                     print(f"错误: {e}")
#         print(f"你选择了 {levels} 层")
#         if choice == 1:
#             print("生成左对齐金字塔:")
#             for i in range(1, levels + 1):
#                 for j in range(1, i + 1):
#                     print(j, end=' ')
#                 print()
#         elif choice == 2:
#             print("生成居中金字塔:")
#             for i in range(1, levels + 1):
#                 print(' ' * (levels - i), end='')
#                 for j in range(1, i + 1):
#                     print(j, end=' ')
#                 print()
#         elif choice == 3:
#             print("生成倒三角金字塔:")
#             for i in range(levels, 0, -1):
#                 for j in range(1, i + 1):
#                     print(j, end=' ')
#                 print()
#         elif choice == 4:
#             print("生成数字递增金字塔:")
#             num = 1
#             for i in range(1, levels + 1):
#                 for j in range(1, i + 1):
#                     print(num, end=' ')
#                     num += 1
#                 print()

            

# if __name__=="__main__":
#     pyramid_factory()