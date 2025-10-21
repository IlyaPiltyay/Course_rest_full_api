import requests

from config.settings import API_TOKEN_TELEGRAM, TELEGRAM_URL


def send_message(chat_id, message):
    """Функция отправки сообщения пользователю о привычке в телеграм"""
    params = {"text": message, "chat_id": chat_id}
    requests.get(f"{TELEGRAM_URL}{API_TOKEN_TELEGRAM}/sendMessage", params=params)
