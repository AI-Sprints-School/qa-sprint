import pytest
import requests


@pytest.mark.xfail(
    reason="заложенный дефект списания больше баланса, lesson05/bug-reports.md: заголовок вашего баг-репорта",
    strict=True,
)
def test_withdraw_over_balance_is_rejected(base_url, auth_headers):
    url = base_url + "/api/wallet/withdraw"
    response = requests.post(
        url,
        json={"amount": 50000},  # больше вашего баланса, но в лимите 100 000
        headers=auth_headers,
        timeout=10,
    )
    # тест убирает за собой: из-за дефекта сервер может списать деньги
    # и увести баланс в минус, поэтому при ответе 2xx возвращаем сумму
    if 200 <= response.status_code < 300:
        requests.post(
            base_url + "/api/wallet/topup",
            json={"amount": 50000},
            headers=auth_headers,
            timeout=10,
        )
    body = response.json()

    # ваши две строки: код ответа и код ошибки в теле
