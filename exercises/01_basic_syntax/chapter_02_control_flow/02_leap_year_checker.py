"""
文件名: 02_leap_year_checker.py
所属章节: 第2章 - 流程控制结构
题目: 闰年判断程
完成日期: 2025-11-10
学习总结:
  - 掌握了复杂的闰年判断逻辑：(能被4整除且不能被100整除)或能被400整除
  - 学会了使用try-except处理用户输入错误，提升程序健壮性
  - 理解了逻辑运算符的优先级和括号的正确使用
"""




# year = float(input("请输入年份："))
# if (year %4 == 0 and year %100 != 0) or year %400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")
    

try:
    year = int(input("请输入年份: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
        
except ValueError:
    print("错误：请输入有效的年份")