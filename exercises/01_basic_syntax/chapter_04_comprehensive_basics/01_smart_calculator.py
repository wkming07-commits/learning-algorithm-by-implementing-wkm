"""
文件名: 01_smart_calculator.py
所属章节: 第4章 - 基础语法综合
题目: 智能计算器 - 变量、流程控制、循环综合应用
完成日期:2025/11/13
学习总结:
  - 连续计算功能的循环实现
  - 多级菜单的流程控制
  - 变量在计算过程中的状态管理
  - 完整的数据验证和异常处理
"""


def smart_calculator():
    print("欢迎使用智能计算器！")
    result = 0
    while True:
        print("\n当前结果:", result)
        print("请选择操作:")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 重置结果")
        print("6. 退出")

        choice = input("输入选项 (1-6): ")

        if choice == '6':
            print("感谢使用智能计算器！再见！")
            break

        if choice == '5':
            result = 0
            print("结果已重置为0。")
            continue

        try:
            number = float(input("请输入一个数字: "))
        except ValueError:
            print("无效输入，请输入一个数字。")
            continue

        if choice == '1':
            result += number
        elif choice == '2':
            result -= number
        elif choice == '3':
            result *= number
        elif choice == '4':
            if number == 0:
                print("错误：除数不能为零。")
                continue
            result /= number
        else:
            print("无效选项，请选择1到6之间的数字。")

if __name__ == "__main__":
    smart_calculator()
