"""
变量 = input(提示语)
1.给用户展示提示语
2.input()把用户输入的内容接收到
3.把接收到的用户输入赋值给左边的变量
"""
# 需求: 获取用户的用户名,密码,年龄,性别,出生日期,身高
print('传智教育用户注册平台1')
user_name = input('请输入用户名:')
user_pwd = input('请输入密码:')
user_age = input('请输入年龄:')
user_gender = input('请输入性别:')
user_bir = input('请输入出生日期:')
user_height = input('请输入身高:')
print(f"""您输入的内容是
       用户名: {user_name}
       密码: {user_pwd}
       年龄: {user_age}
       性别: {user_gender}
       出生日期: {user_bir}
       身高: {user_height} 
      """)
