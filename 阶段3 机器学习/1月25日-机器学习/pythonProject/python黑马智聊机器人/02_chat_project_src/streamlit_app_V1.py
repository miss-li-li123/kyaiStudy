# 1.导包
import streamlit as st
import ollama_utils

# 2.添加标题
st.title('黑马智聊机器人')
# 3.添加分割线
st.divider()
# 4.构建ai和用户的聊天窗口
# 4.1 AI的开场白
st.chat_message('assistant').write('你好,我是黑马智聊机器人,有什么可以帮助您的吗?')
# 4.2 获取用户的输入
prompt = st.chat_input('请输入您的问题:')

# 4.3 展示AI的答案
# 非空即为True
if prompt:
    # 如果用户输入了问题,再展示问题
    st.chat_message('user').write(prompt)
    # TODO 提前封装messages消息列表
    messages = [{'role': 'user', 'content': prompt}]
    # TODO 当问题回应比较慢的时候,可以添加spinner("正在思考...")
    with st.spinner('正在思考...'):
        # todo 此处要根据上述用户的问题,调用大模型获取答案
        llm_result = ollama_utils.get_ollama_chat_result(messages)
    # todo 此处直接把ai生成的答案返回到页面中
    st.chat_message('assistant').write(llm_result)
