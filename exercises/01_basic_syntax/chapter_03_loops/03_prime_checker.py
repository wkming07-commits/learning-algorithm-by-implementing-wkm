"""
文件名: 03_03_prime_checker.py
所属章节: 第3章 - 循环结构
题目: 质数判断器 - 掌握循环优化和性能对比
完成日期: 2025-11-10
学习总结:
  - 质数判断的核心算法：检查2到√n之间是否有因子
  - 循环优化的重要性：从O(n)到O(√n)的时间复杂度优化
  - time模块的使用：time.time()进行精确的性能测量
  - 边界情况处理：n=1和n=2的特殊情况考虑
  - 函数设计原则：单一职责，清晰的输入输出
  - 算法性能对比：通过实际数据验证理论优化效果
  - 代码复用技巧：prime_check函数被多个功能共用
  - 列表推导式的应用：快速生成质数列表
  - 格式化输出：f-string控制小数位数和输出对齐
"""




# def way_1(n):
#     answer = f"{n}是质数"
#     for i in range(1, n):
#         a = float(n % i)
#         if a == int(a):
#             answer = f"{n}不是质数"
#             break
#     return answer
# def way_2(n):
#     answer = f"{n}是质数"
#     for i in range(2, int(n**0.5) + 1):
#         a = float(n % i)
#         if a == int(a):
#             answer = f"{n}不是质数"
#             break
#     return answer
# if __name__ == "__main__":
#     n = int(input("请输入数字:"))
#     print(f"基础方法：{way_1(n)}")
#     print(f"优化方法：{way_2(n)}")

import time
import math

def is_prime_basic(n):
    """基础方法：从2遍历到n-1"""
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    """优化方法：从2遍历到√n"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    limit = int(math.isqrt(n)) + 1
    for i in range(3, limit, 2):  # 只检查奇数
        if n % i == 0:
            return False
    return True

def prime_check(n, method='optimized'):
    """统一的质数检查接口"""
    start_time = time.time()
    
    if method == 'basic':
        result = is_prime_basic(n)
    else:
        result = is_prime_optimized(n)
        
    end_time = time.time()
    return result, end_time - start_time

def find_primes_up_to(limit):
    """找出限定范围内的所有质数"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime_optimized(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        # 单个数字判断
        n = int(input("请输入要判断的数字: "))
        
        # 基础方法
        result_basic, time_basic = prime_check(n, 'basic')
        # 优化方法
        result_optimized, time_optimized = prime_check(n, 'optimized')
        
        print(f"\n=== 质数判断结果 ===")
        print(f"基础方法: {n}{'是' if result_basic else '不是'}质数 (耗时: {time_basic:.6f}秒)")
        print(f"优化方法: {n}{'是' if result_optimized else '不是'}质数 (耗时: {time_optimized:.6f}秒)")
        
        # 性能对比
        if time_basic > 0:
            improvement = (time_basic - time_optimized) / time_basic * 100
            print(f"性能提升: {improvement:.1f}%")
        
        # 输出100以内的质数
        print(f"\n=== 100以内的质数 ===")
        primes_100 = find_primes_up_to(100)
        print(f"质数列表: {primes_100}")
        print(f"共计: {len(primes_100)}个质数")
        
    except ValueError:
        print("错误：请输入有效的整数！")