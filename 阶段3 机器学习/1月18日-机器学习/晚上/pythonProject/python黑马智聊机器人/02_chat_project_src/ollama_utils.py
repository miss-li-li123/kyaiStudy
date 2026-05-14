# 1.导包
# 先安装: pip install ollama
import ollama

# 2.ollama调用本地私有大模型
# 创建对象
client = ollama.Client("http://127.0.0.1:11434/")


# 定义api函数
def get_ollama_chat_result(messages):
    # 发送请求
    result = client.chat(
        model='qwen2.5:7b',
        messages=messages,
        stream=False
    )
    # 返回结果
    return result.message.content


if __name__ == '__main__':
    messages = [{'role': 'user', 'content': '给我讲一个笑话'}]
    data = get_ollama_chat_result(messages)
    print(data)
    print('=======================================================')
    messages = [{'role': 'user', 'content': '给我生成一个100字的小故事'}]
    data = get_ollama_chat_result(messages)
    print(data)