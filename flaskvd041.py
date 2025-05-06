from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем текущие дату и время
    current_time = datetime.now()

    # Форматируем дату и время для отображения
    formatted_date = current_time.strftime("%d.%m.%Y")
    formatted_time = current_time.strftime("%H:%M:%S")

    return render_template('index.html',
                           date=formatted_date,
                           time=formatted_time)

#
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Отключить автоматическую перезагрузку
