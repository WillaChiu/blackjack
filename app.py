import streamlit as st
import random

def generate_problems(numbers):
    """生成问题和答案列表"""
    problems = []
    answers = []
    for num in numbers:
        problem = f"${num}?"
        answer = num * 1.5
        problems.append(problem)
        answers.append(answer)
    return problems, answers

# 设置页面标题
st.title("Math Quiz")

# 全局变量，用于追踪分数和当前题目索引
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

# 根据选择的模式生成问题
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
    user_answer = st.number_input("Your answer:", step=0.1, key="answer_input")
    
    # 提交答案按钮
    if st.button("Submit Answer"):
        if user_answer == correct_answer:
            st.session_state.score += 1
            st.write("Correct!")
        else:
            st.write(f"Wrong! The correct answer was {correct_answer}.")

        # 更新题目索引
        st.session_state.current_problem_index += 1

# 检查是否完成所有问题
if st.session_state.current_problem_index >= len(st.session_state.problems):
    st.write("Quiz completed!")
    st.write(f"You got {st.session_state.score} out of {len(st.session_state.problems)} correct.")
    st.session_state.problems = []  # 清空题目，等待下次开始


