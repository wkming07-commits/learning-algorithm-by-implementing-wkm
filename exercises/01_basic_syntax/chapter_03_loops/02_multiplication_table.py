"""
文件名: 03_02_multiplication_table.py
所属章节: 第3章 - 循环结构
题目: 乘法口诀表 - 掌握循环控制与格式化输出
完成日期: [请填写实际完成日期]
学习总结:
  - 嵌套循环的实践应用：外层控制行，内层控制列
  - 循环变量关系理解：内层循环范围依赖外层循环变量(i+1)
  - 制表符\t的使用：实现简单的列对齐效果
  - f-string格式化输出：在字符串中嵌入变量和表达式
  - print(end="")的使用：控制单行内多内容输出
  - 循环边界处理：range(1,10)和range(1,i+1)的配合
  - 异常处理机制：try-except保护程序稳定性
  - 代码调试技巧：通过观察输出格式发现问题
"""




def print_multiplication_table():
    for i in range (1,10):
        for j in range (1,i+1):
            print(f"{j}X{i}={i*j}", end="\t")
        print()
if __name__ == "__main__":
    try:
        print_multiplication_table()
    except Exception as e:
        print(f"发生错误: {e}")  # 显示具体的错误信息