import requests
import time
import config



offset = -2
counter = 0
cat_response: requests.Response
chat_id: int



while counter < config.MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{config.API_URL}{config.BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    print(updates)

    if updates['result']:
        for result in updates['result']:

            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(config.API_CATS_URL)

            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{config.API_URL}{config.BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{config.API_URL}{config.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={config.ERROR_TEXT}')

    time.sleep(5)
    counter += 1
