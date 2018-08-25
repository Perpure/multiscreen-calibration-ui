1. Склонировать репозиторий и перейти в его папку

    ```
    git clone git@gitlab.com:multiscreen/calibration_ui.git
    cd calibration_ui
    ```

2. Создать виртуальное окружение и активировать его

    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Установить зависимости

    ```
    pip install -r requirements.txt
    ```

4. Установить необходимые пакеты
    ```
    apt-get install python3-tk
    ```

5. Поместить нужную фотографию по этому пути
    ```
    images/picture.jpeg
    ```

6. Запустить приложение
    ```
    python main.py
    ```
