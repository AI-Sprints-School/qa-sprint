"""Фикстуры для API-тестов урока 9.

Править этот файл не нужно. Он один раз забирает адрес «Кошелька»
и доступы из настроек окружения, один раз логинится и отдаёт готовый
заголовок авторизации. Логина, пароля и токена в коде тестов при этом
нет ни одного, и в публичный репозиторий они не попадают.

Если переменных окружения нет — без секретов репозитория их нет, — тесты
честно печатаются пропущенными, а не роняют прогон.

Переменные окружения:
    WALLET_BASE_URL   адрес «Кошелька», например https://wallet.aisprints.ru
    WALLET_LOGIN      ваш логин вида student-07
    WALLET_PASSWORD   пароль из письма «Доступ к учебному приложению «Кошелёк»»
"""
import os

import pytest
import requests

SKIP_REASON = (
    "нет доступов к «Кошельку» в переменных окружения "
    "(WALLET_BASE_URL, WALLET_LOGIN, WALLET_PASSWORD) — API-тест пропущен"
)


@pytest.fixture(scope="session")
def base_url():
    """Адрес «Кошелька» без завершающего слэша."""
    url = os.environ.get("WALLET_BASE_URL", "").strip()
    if not url:
        pytest.skip(SKIP_REASON)
    return url.rstrip("/")


@pytest.fixture(scope="session")
def token(base_url):
    """Живой токен: один вход на весь прогон."""
    login = os.environ.get("WALLET_LOGIN", "").strip()
    password = os.environ.get("WALLET_PASSWORD", "").strip()
    if not login or not password:
        pytest.skip(SKIP_REASON)

    response = requests.post(
        base_url + "/api/auth/login",
        json={"login": login, "password": password},
        timeout=10,
    )
    if response.status_code != 200:
        pytest.skip(
            "вход не удался: сервер ответил "
            + str(response.status_code)
            + " — проверьте логин и пароль в переменных окружения"
        )
    return response.json()["token"]


@pytest.fixture(scope="session")
def auth_headers(token):
    """Готовый заголовок авторизации для всех запросов."""
    return {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }
