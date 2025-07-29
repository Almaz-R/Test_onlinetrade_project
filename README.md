# 🛠 Проект автотестов для onlinetrade.ru

## 📌 Описание
Этот проект содержит автоматизированные UI-тесты для сайта [onlinetrade.ru](https://www.onlinetrade.ru/), написанные с использованием:
- **Python 3.11**
- **Pytest**
- **Selenium WebDriver**
- **undetected-chromedriver** (для обхода антибот-защиты)
- **Page Object Model (POM)**

---

## ⚙️ Установка
1. Клонировать репозиторий:
```bash
git clone https://github.com/ТВОЙ_ЛОГИН/ТВОЙ_РЕПОЗИТОРИЙ.git
```
2. Перейти в директорию проекта:
```bash
cd Test_onlinetrade_project
```
3. Создать и активировать виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```
4. Установить зависимости:
```bash
pip install -r requirements.txt
```

---

## ▶️ Запуск тестов
```bash
pytest -v
```
или с формированием отчёта:
```bash
pytest --html=report.html
```

---

## 📂 Структура проекта
```
Test_onlinetrade_project/
│── conftest.py          # Фикстуры для тестов
│── tests/               # Тестовые сценарии
│── pages/               # Page Object Model классы
│── requirements.txt     # Зависимости проекта
│── README.md            # Описание проекта
```

---

## ✅ Особенности
- Авторизация выполняется через UI во всех тестах (фикстура `authorized_driver`).
- Используется случайная задержка, чтобы имитировать действия реального пользователя.
- Реализована обработка cookie-баннера.
