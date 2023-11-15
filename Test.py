import requests
import config


api_url = config.API_URL + config.TELEGRAM_BOT_TOKEN + '/sendMessage?chat_id=' + config.CHAT_ID + '&text=' + config.TEXT
#api_url = 'https://api.telegram.org/bot' + config.TELEGRAM_BOT_TOKEN + '/getUpdates'
print(api_url)


response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код