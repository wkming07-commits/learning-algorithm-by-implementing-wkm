"""
文件名: 02_pyramid_factory.py
所属章节: 第4章 - 基础语法综合  
题目: 数字金字塔工厂 - 嵌套循环深度练习
要求：
1. 生成4种金字塔：左对齐、居中、倒三角、数字递增
2. 用户选择模式并输入层数(1-9)
3. 实时显示生成的金字塔图案
4. 统计每行数字和总数字个数
5. 支持连续生成不同模式
"""
def pyramid_factory():
    while True:
        print("请选择金字塔模式：")
        print("1. 左对齐金字塔")
        print("2. 居中金字塔") 
        print("3. 倒三角金字塔")
        print("4. 数字递增金字塔")

        while True:
            try:
                choice = input("输入选项 (1-4): ").strip()
                choice = int(choice) 
                if choice not in [1, 2, 3, 4]:
                    raise ValueError("无效选项，请选择1到4之间的数字。")
                break
            except ValueError as e:
                print(f"错误: {e}")
                
            print(f"你选择了模式 {choice}")
        while True:
            try:
                levels = input("请输入金字塔层数 (1-9): ").strip()
                levels = int(levels)
                if levels < 1 or levels > 9:
                    raise ValueError("层数必须在1到9之间。")
                break
            except ValueError as e:
                    print(f"错误: {e}")
        print(f"你选择了 {levels} 层")
        if choice == 1:
            print("生成左对齐金字塔:")
            for i in range(1, levels + 1):
                for j in range(1, i + 1):
                    print(j, end=' ')
                print()
        elif choice == 2:
            print("生成居中金字塔:")
            for i in range(1, levels + 1):
                print(' ' * (levels - i), end='')
                for j in range(1, i + 1):
                    print(j, end=' ')
                print()
        elif choice == 3:
            print("生成倒三角金字塔:")
            for i in range(levels, 0, -1):
                for j in range(1, i + 1):
                    print(j, end=' ')
                print()
        elif choice == 4:
            print("生成数字递增金字塔:")
            num = 1
            for i in range(1, levels + 1):
                for j in range(1, i + 1):
                    print(num, end=' ')
                    num += 1
                print()

            

if __name__=="__main__":
    pyramid_factory()
