"""
文件名: 03_01_number_pyramid.py
所属章节: 第3章 - 循环结构
题目: 数字金字塔 - 掌握嵌套循环模式
完成日期: 2025-11-10
学习总结:
  - 嵌套循环的层次关系：外层控制行数，内层控制每行内容
  - 字符串乘法生成重复字符：" " * (n-i) 生成前导空格
  - 循环变量关系：利用i,j控制数字的递增和递减序列
  - print(end="")控制不换行输出，实现单行多内容
  - 对称数字序列生成：先递增(1→i)再递减(i-1→1)
  - 主程序保护模式：if __name__ == "__main__" 的实践应用
  - 用户输入验证：try-except处理非数字输入，if判断范围限制
"""



def number_pyramid(n):
    """生成对称数字金字塔"""
    for i in range(1, n + 1):
        # 打印前导空格
        print(" " * (n - i), end="")
        
        # 打印左半部分递增数字
        for j in range(1, i + 1):
            print(j, end="")
        
        # 打印右半部分递减数字
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        # 换行
        print()

if __name__ == "__main__":
    try:
        n = int(input("请输入金字塔层数 (1-9): "))
        if 1 <= n <= 9:
            number_pyramid(n)
        else:
            print("请输入1-9之间的数字！")
    except ValueError:
        print("输入错误，请输入整数！")