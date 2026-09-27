import requests


def test_balance_has_currency(base_url, auth_headers):
    url = base_url + "/api/wallet/balance"
    response = requests.get(url, headers=auth_headers, timeout=10)
    body = response.json()

    # ваши две строки: код ответа и конкретное поле тела
