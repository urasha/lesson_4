from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    dct = {'surname': ('фамилия', 'Watny'),
           'name': ('Имя', 'Mark'),
           'education': ('Образование', 'выше среднего'),
           'profession': ('Профессия', 'инженер'),
           'sex': ('Пол', 'male'),
           'motivation': ('Мотивация', 'было бы круто застрять на Марсе!'),
           'ready': ('Готовы остаться?', 'true')}

    return render_template('auto_answer.html', dct=dct)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
