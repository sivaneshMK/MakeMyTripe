import requests


class TestCalculator:

    def test_sum_api(self):

        response = requests.get("https://fastapi-calculadora.onrender.com/calculo-basico/sumar/?num1=504&num2=340")
        print(response.content)
        print(response.status_code)