import psutil
import requests
import time

# Установим пороговое значение потребления памяти в процентах
threshold_percentage = 90

# Укажем URL API, на который будем отправлять запрос в случае превышения порога
api_url = 'http://localhost:8080/api/alert'

while True:
    # Получим текущее значение использования памяти
    memory_usage = psutil.virtual_memory().percent

    # Если потребление памяти превышает порог, отправим HTTP запрос на API
    if memory_usage > threshold_percentage:
        data = {'message': f'Memory usage is {memory_usage}%'}
        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                print(f'Alert sent: {data}')
            else:
                print(f'Failed to send alert. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error sending alert: {e}')

    # Пауза на 5 минут перед следующей проверкой
    time.sleep(300)