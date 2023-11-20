import json


def upload(route: str) -> dict[str:str]:
    f = open(route, 'r')
    users = json.loads(f.readline())
    f.close()
    return users
