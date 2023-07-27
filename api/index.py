from flask import Flask,request
import openai
import os
import json
import traceback

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat',methods=["POST"])
def chat():
    try:
        print(request.method)
        if request.method == "GET":
            content = request.args.get("content")
            # comment = request.values.get("content")
            res = int(content) + 10
            print(res, type(content))

        elif request.method == "POST":
            print("========", request.headers)
            content_type = request.headers.get('Content-Type')
            if "multipart/form-data" in content_type:
                form_data = dict(request.form)
                # files_data = dict(request.files)
                # print(form_data)

                res = int(form_data.get('content')) + 14

            elif "application/json" in content_type:
                # request.get_data() # 原始的数据
                input_dict = request.get_json()
                res = input_dict.get('content')
                print(res)
            elif "application/x-www-form-urlencoded" in content_type:
                input_dict = request.form
                # request.values.get("content")
            else:
                print(request.get_data())

            # 调用 API 生成文本
            outContent = generate_text(res)
            print(outContent)
        print('url: %s , script_root: %s , path: %s , base_url: %s , url_root : %s' % (
            request.url, request.script_root, request.path, request.base_url, request.url_root))
        return json.dumps({"code": 0, "msg": "success", "data": outContent},ensure_ascii=False)
    except:
        err_msg = 'url: %s, err_msg: %s' % (request.url, (str(traceback.format_exc())))
        print(err_msg)
        return json.dumps({"code": -1, "msg": "failed", "data": 0})

# 调用 GPT-3.5-turbo API 来生成文本
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用 GPT-3.5-turbo 引擎
        prompt=prompt,
        max_tokens=240,  # 生成的最大文本长度
        stop=None,  # 可选：在此停止生成文本的标记列表
        temperature=0.7,  # 控制生成文本的创造性。较低的值会使输出更加保守，较高的值会使输出更加随机。
    )
    return response.choices[0].text.strip()

@app.route('/test',methods=["POST"])
def test():
    data = request.get_json(force=True)
    data2 = request.get_data()
    data3 = request.form.get('data')
    return data +"---"+data2+"---"+data3

@app.route('/')
def home():
    return 'Hello, opengan!'
    
@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run("127.0.0.1", debug=True, port=6006)
