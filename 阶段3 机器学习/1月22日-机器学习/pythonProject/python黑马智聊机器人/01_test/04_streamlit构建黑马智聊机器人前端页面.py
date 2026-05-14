# 1.导包
import streamlit as st
# 2.添加标题
st.title('黑马智聊机器人')
# 3.添加分割线
st.divider()
# 4.构建ai和用户的聊天窗口
# 4.1 AI的开场白
st.chat_message('assistant').write('你好,我是黑马智聊机器人,有什么可以帮助您的吗?')
# 4.2 获取用户的输入
prompt = st.chat_input('请输入您的问题:')
st.chat_message('user').write(prompt)
# 4.3 展示AI的答案
# 非空即为True
if prompt:
    # todo 后续此处要根据上述用户的问题,调用大模型获取答案
    # 此处先写一个固定的答案
    st.chat_message('assistant').write('很高兴为您服务!')