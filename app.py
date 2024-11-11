import streamlit as st
import random
#streamlit run app.py

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
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# 选择模式
mode = st.radio("Choose mode:", ("Mode A: Fixed Numbers (1-20,25,35,45,55,65,75)", "Mode B: Random Numbers (1-500)"))

# 根据选择的模式生成问题
if st.button("Start Quiz"):
    if mode == "Mode A: Fixed Numbers (1-20,25,35,45,55,65,75)":
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
    st.session_state.feedback = ""

# 显示当前问题
if st.session_state.problems and st.session_state.current_problem_index < len(st.session_state.problems):
    # 获取当前问题和答案
    current_problem = st.session_state.problems[st.session_state.current_problem_index]
    correct_answer = st.session_state.correct_answers[st.session_state.current_problem_index]

    # 显示问题并接受用户输入答案
    #st.write(current_problem)
    #user_answer = st.number_input("Your answer:", step=0.1, key="answer_input")
    
    st.write(current_problem)
    user_answer = st.text_input("Your answer:", value="", key="answer_input")  # 使用text_input，默认值为空

    # 尝试将输入转换为浮点数
    try:
        user_answer_float = float(user_answer) if user_answer else None
    except ValueError:
        user_answer_float = None
        st.warning("Please enter a valid number.")

    # 提交答案按钮
    if st.button("Submit Answer"):
        if user_answer == correct_answer:
            st.session_state.score += 1
            st.session_state.feedback = "Correct!"
        else:
            st.session_state.feedback = f"Wrong! The correct answer was {correct_answer}."

    # 显示答案反馈
    st.write(st.session_state.feedback)

    # “Next Question”按钮，允许用户手动进入下一题
    if st.session_state.feedback and st.button("Next Question"):
        st.session_state.current_problem_index += 1
        st.session_state.feedback = ""  # 清除反馈
        st.rerun()  # 刷新页面以显示下一题

# 检查是否完成所有问题
if st.session_state.current_problem_index >= len(st.session_state.problems):
    st.write("Quiz completed!")
    st.write(f"You got {st.session_state.score} out of {len(st.session_state.problems)} correct.")
    # 清空题目和状态，以便下次重新开始
    del st.session_state.problems
    del st.session_state.correct_answers
    st.session_state.current_problem_index = 0
    st.session_state.score = 0

# 在页面底部添加作者信息和 PayPal 捐赠链接
st.markdown("---")  # 分割线
st.markdown("### Created by Willa Q.")

st.markdown("If you enjoyed this quiz and would like to support further development, feel free to donate!")

# PayPal.Me 捐赠链接
#donate_url = "https://paypal.me/WillaQu?country.x=CA&locale.x=en_US"  # 替换成你的 PayPal.Me 链接
#st.markdown(f"[Donate to my PayPal]( {donate_url} )")  # 超链接显示

# 或者使用按钮样式
st.write("###")
if st.button("Donate via PayPal"):
    st.markdown(f"[Click here to donate via PayPal]({"https://paypal.me/WillaQu?country.x=CA&locale.x=en_US"})")

