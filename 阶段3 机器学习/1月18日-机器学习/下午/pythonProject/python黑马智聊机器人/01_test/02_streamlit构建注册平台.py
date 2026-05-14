# 1.导包
# 先安装: pip install streamlit
import streamlit as st

# todo 注意: streamlit的文件不能右键直接运行,需要用streamlit运行命令: streamlit run 文件
# 2.设置标题
st.title('传智教育用户注册平台')
# 3.添加分隔线
st.divider()
# 4.获取用户名
user_name = st.text_input('请输入用户名:',value='binzi')
# 5.获取密码
user_pwd = st.text_input('请输入密码:', type='password',value='123')
# 6.获取年龄
user_age = st.number_input('请输入年龄:', value=18, min_value=0, max_value=150)
# 7.获取性别
user_gender = st.radio('请选择性别:', options=("男", "女", "保密"), horizontal=True)
# 8.获取生日
user_bir = st.date_input('请选择生日:')
# 9.获取身高
user_height = st.slider('请选择身高:', value=188, min_value=0, max_value=300)
# 10.提交按钮
# 非空即为True
if st.button('确认'):
    st.write('恭喜您,信息录入成功!')
    # 写到页面
    st.write(f"""您输入的内容是
           用户名: {user_name}
           密码: {user_pwd}
           年龄: {user_age}
           性别: {user_gender}
           出生日期: {user_bir}
           身高: {user_height} 
          """)
    # 写到本地文件
    with open('user_info.txt', "w", encoding='utf8') as f:
        f.write(f"""您输入的内容是
           用户名: {user_name}
           密码: {user_pwd}
           年龄: {user_age}
           性别: {user_gender}
           出生日期: {user_bir}
           身高: {user_height} 
          """)

