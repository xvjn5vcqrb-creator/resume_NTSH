

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

#改成互動 3/17
@app.route('/activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        # 2. 讀取學生的問題
        question = request.form.get('question', '').strip()
        # 3. 查詢題庫的對應答案
        answer = "我喜歡打羽球、打LOL、寫作、聽音樂"
        # 4. 回傳答案給學生
        return render_template('activities.html', question=question, answer=answer)
    # GET 時給空白欄位
    return render_template('activities.html', question="", answer="")

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
