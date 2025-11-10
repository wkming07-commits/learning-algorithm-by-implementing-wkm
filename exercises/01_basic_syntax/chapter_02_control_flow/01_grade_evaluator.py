"""
文件名: 01_grade_evaluator.py
所属章节: 第2章 - 流程控制结构  
题目: 成绩等级判断程序
技术要点: if-elif-else结构、Python缩进规则
完成日期: 2025-11-10
"""

def grade_evaluator():
    # 获取输入
    score = float(input("请输入成绩(0-100): "))
    
    # 成绩等级判断
    if score >= 90:
        grade = "优秀"
    elif score >= 80:  # 注意：Python使用elif，不是else if
        grade = "良好"
    elif score >= 70:
        grade = "中等" 
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    
    print(f"成绩 {score} 分，等级: {grade}")

if __name__ == "__main__":
    grade_evaluator()