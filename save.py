import json


def save(route: str, users) -> None:
    f = open(route, 'w')
    temp = json.dumps(users)
    f.write(temp)
    f.close()
