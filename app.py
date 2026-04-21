from flask import Flask, request, render_template

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "안녕하세요" : "你好",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "家人": "가족",
    "愛": "사랑"
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

# 使用 dict 作為中韓翻譯的題庫
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # 2. 讀取學生的問題###^#@#Q%#@
        question1 = request.form.get('question', '').strip()
        # 3. 查詢題庫的對應答案
        # answer1 = zh_ko_dict.get(question, "抱歉，我目前沒有這個詞的韓文對應。")

        answer1 = zh_ko_dict[question1]
        # 4. 回傳答案給學生
        return render_template('ask.html', question=question1, answer=answer1)
    # GET 時給空白欄位
    return render_template('ask.html', question="", answer="")



#改成互動 3/17
@app.route('/activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        # 2. 讀取學生的問題
        question = request.form.get('question', '').strip()
        # 3. 查詢題庫的對應答案
        answer = "抱歉，我目前沒有這個詞的韓文對應。"
        # 4. 回傳答案給學生
        return render_template('activities.html', question=question, answer=answer)
    # GET 時給空白欄位
    return render_template('activities.html', question="", answer="")

#改成互動 4/14
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        # 2. 讀取股票號碼
        question = request.form.get('question', '').strip()
        # 3. 查詢股票號碼的對應股價
        answer = "抱歉，我目前沒有這個股票號碼。"
        # 4. 回傳答案給使用者
        return render_template('stock.html', question=question, answer=answer)
    # GET 時給空白欄位
    return render_template('stock.html', question="", answer="")


@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')


if __name__ == '__main__':
    app.run(debug=True)
