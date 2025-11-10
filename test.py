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
name = "张三"
path = r"D:\nus_ai_projects"
binary = b"data"
multiline = """第一行
第二行
第三行"""

print(f"姓名: {name}")
print(f"路径: {path}") 
print(f"二进制: {binary}")
print(f"多行文本:\n{multiline}")