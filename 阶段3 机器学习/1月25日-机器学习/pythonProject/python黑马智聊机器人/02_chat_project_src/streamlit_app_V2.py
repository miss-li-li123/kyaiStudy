# 1.导包
import streamlit as st
import ollama_utils
# 2.添加标题
st.title('黑马智聊机器人')
# 3.添加分割线
st.divider()
# TODO 5.提前创建messages列表,用于添加和展示历史聊天记录
# st.session_state格式->{'messages':[{AI开场白},{用户问题1},{AI答案1},{用户问题2},{AI答案2},...]}
if "messages" not in st.session_state:
    # 首次没有历史列表,那就创建一个空列表
    st.session_state['messages'] = []
    # 提前添加一个AI开场白消息到messages列表中
    st.session_state['messages'].append(
        {'role': 'assistant', 'content': '你好,我是黑马智聊机器人,有什么可以帮助您的吗?'})
# TODO 4.构建AI和用户的聊天窗口
# todo 4.1 遍历历史消息列表,把每个消息依次展示到页面
for message in st.session_state['messages']:
    # todo 首次只拿到了AI开场白,后续拿到的是问答历史记录
    st.chat_message(message['role']).write(message['content'])
# 4.2 获取用户的输入
prompt = st.chat_input('请输入您的问题:')
# 4.3 展示AI的答案
# 非空即为True
if prompt:
    # TODO 如果用户输入了问题,再展示问题
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role': 'user', 'content': prompt})  # 存储用户问题历史

    # TODO 当问题回应比较慢的时候,可以添加spinner("正在思考...")
    with st.spinner('正在思考...'):
        # todo 此处要根据上述用户的问题,调用大模型获取答案
        # 'messages':[{AI开场白},{用户问题1},{AI答案1},{用户问题2},{AI答案2},...]
        llm_result = ollama_utils.get_ollama_chat_result(st.session_state['messages'][-20:]) # 建议把最近的20个问答记录发送给模型即可
    # todo 此处直接把ai生成的答案返回到页面中
    st.chat_message('assistant').write(llm_result)
    st.session_state['messages'].append({'role': 'assistant', 'content': llm_result})  # 存储ai历史
