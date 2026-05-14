# 1.导包
# 先安装: pip install ollama
import ollama
# 2.ollama调用本地私有大模型
# 创建对象
client = ollama.Client("http://127.0.0.1:11434/")
# 发送请求
result = client.chat(
    model='qwen2.5:7b',
    messages=[
        {'role':'user','content':'你是谁'},
    ],
    stream=False
)
# 3.打印结果
print(result.message.content)
