import requests
import time
import config




offset = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{config.API_URL}{config.BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={config.POLLING_TIME}').json()

    if updates['result']:
        for result in updates['result']:

            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
