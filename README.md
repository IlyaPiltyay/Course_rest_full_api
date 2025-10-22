# Course_rest_full_api

Курсовой проект Django_Rest

# Проект разработки сервиса трекера полезных привычек с помощью Django REST Framework

## В данном проекте реализован функционал backend части приложения для создания привычек и их интеграции с Телеграм Ботом, который реализует отправку напоминания пользователю о его привычке.

## Установка:

2. Клонируйте репозиторий через ssh:

```
git@github.com:IlyaPiltyay/Course_rest_full_api.git
```

3. Устанавливайте зависимости из файла **pyproject.toml** командой:

```
poetry install
```

## Использование:

python manage.py runserver
доступ по адресу http://127.0.0.1:8000/.

## Тестирование:

- Тесты можно запускать с помощью:
  poetry run pytest

## Документация:

- Документация проекта доступна по адресам swagger/ и redoc/.
- Используйте swagger/ для интерактивного тестирования API.
- redoc/ предоставляет более подробное представление документации.

## Основные команды Docker и Docker Compose

- **Остановить запущенный контейнер**:
    ```bash
    docker stop d5030b766bcc
    ```
- **Остановить и удалить все контейнеры, сети и тома**:
    ```bash
    docker-compose down
    ```
- **Удалить конкретный контейнер**:
    ```bash
    docker rm django-app
    ```
- **Просмотреть логи конкретного контейнера**:
    ```bash
    docker logs django-app
    ```
- **Построить образ Docker из `Dockerfile`**:
    ```bash
    docker build -t django-app .
    ```
- **Показать все запущенные контейнеры**:
    ```bash
    docker ps
    ```
- **Запустить контейнеры с пересборкой**:
    ```bash
    docker compose up --build
    ```
- **Получить доступ к контейнеру через оболочку**:
    ```bash
    docker exec -it <container_id> /bin/bash
    ```
- **Перейти в установленный рабочий каталог и просмотреть файлы**:
    ```bash
    ls -l
    ```

### 2. Настройка CI/CD с GitHub Actions

1. Создайте каталог для workflows:
   В вашем репозитории создайте папку .github/workflows, если она еще не существует.
   mkdir -p .github/workflows

2. Создайте файл workflow:
   Создайте новый файл с именем ci.yml в папке .github/workflows:
   nano .github/workflows/ci.yml

3. Заполните файл конфигурацией:
4. Добавьте SSH-ключи:

### 1. Настройка удаленного сервера

1. Подключитесь к вашему удаленному серверу:
   Используйте SSH для доступа к вашему серверу:
   ssh <user>@<server-ip>
2. Обновите пакеты системы:
   sudo apt update && sudo apt upgrade -y
3. Установите Docker:
   Для установки Docker выполните следующие команды:
   sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   sudo apt update
   sudo apt install docker-ce -y

4. Проверьте, что Docker установлен:
   sudo systemctl status docker
5. Клонируйте репозиторий на сервер:
   git clone <repository-url>
   cd <имя-репозитория>
6. Создайте файл Nginx со следующими конфигурациями
   events {
   worker_connections 1024;
   }
   http {
   upstream django
   {
   server web:8000;
   }
   server {
   listen 80;
   server_name _;
   location /static/ {
   alias /app/static/;
   }

        location / {
        proxy_pass http://django ;
        }
   }

}

7. Перейдите по адресу http://89.169.191.81:8000

http://89.169.191.81/habits/
