import streamlit as st
import random

def generate_problems(numbers):
    """生成问题和答案列表"""
    problems = []
    answers = []
    for num in numbers:
        problem = f"What is 1.5 times ${num}?"
        answer = num * 1.5
        problems.append(problem)
        answers.append(answer)
    return problems, answers

# 设置页面标题
st.title("Math Quiz")

# 初始化 session_state 变量
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_problem_index" not in st.session_state:
    st.session_state.current_problem_index = 0
if "problems" not in st.session_state:
    st.session_state.problems = []
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = []

# 选择模式
mode = st.radio("Choose mode:", ("Mode A: Fixed Numbers", "Mode B: Random Numbers (1-500)"))

# 开始测验按钮
if st.button("Start Quiz"):
    if mode == "Mode A: Fixed Numbers":
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 35, 45, 55, 65, 75]
    else:
        numbers = [random.randint(1, 500) for _ in range(20)]  # 生成20个随机数

    # 生成问题和答案，并打乱问题顺序
    st.session_state.problems, st.session_state.correct_answers = generate_problems(numbers)
    combined = list(zip(st.session_state.problems, st.session_state.correct_answers))
    random.shuffle(combined)
    st.session_state.problems, st.session_state.correct_answers = zip(*combined)

    # 重置分数和题目索引
    st.session_state.score = 0
    st.session_state.current_problem_index = 0

# 显示当前问题
if st.session_state.problems:
    # 获取当前问题和答案
    current_problem = st.session_state.problems[st.session_state.current_problem_index]
    correct_answer = st.session_state.correct_answers[st.session_state.current_problem_index]

    # 显示问题并接受用户输入答案
    st.write(current_problem)
    user_answer = st.text_input("Your answer:", value="", key="answer_input")
    
    # 提交答案按钮，模拟回车效果
    if st.button("Submit Answer"):
        try:
            user_answer_float = float(user_answer)
            if user_answer_float == correct_answer:
                st.session_state.score += 1
                st.write("Correct!")
            else:
                st.write(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            st.write("Please enter a valid number.")

        # 清空输入框并更新题目索引
        st.session_state.current_problem_index += 1
        st.experimental_rerun()  # 重新运行以清空输入框

# 检查是否完成所有问题
if st.session_state.current_problem_index >= len(st.session_state.problems):
    st.write("Quiz completed!")
    st.write(f"You got {st.session_state.score} out of {len(st.session_state.problems)} correct.")
    st.session_state.problems = []  # 清空题目，等待下次开始

