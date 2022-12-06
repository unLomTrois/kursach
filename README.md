# Скачаем проект:
```sh
git clone https://github.com/unLomTrois/kursach.git
```

# Установим зависимости
Для работы с ботом
```sh
pip install -r requirements.txt
```
# Как запускать:
Весь код находится в папке src

```sh
python src/main.py
```

main.py импортирует код бота, запускает бота из bot.py
bot.py содержит код с ботом, и импортирует для своей работы калькулятор из calc.py
calc.py содержит класс с калькулятором
