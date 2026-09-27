import pytest
import requests


@pytest.mark.xfail(
    reason="lesson05/bug-reports.md: заголовок вашего баг-репорта",
    strict=True,
)
def test_withdraw_over_balance_is_rejected(base_url, auth_headers):
    url = base_url + "/api/wallet/withdraw"
    response = requests.post(
        url,
        json={"amount": 999999},
        headers=auth_headers,
        timeout=10,
    )
    body = response.json()

    # ваши две строки: код ответа и код ошибки в теле
