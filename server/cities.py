MIN_ID_LEN = 1
NAME = 'name'


cities = {}
current_id = 1


def is_valid_id(_id: str) -> bool:
    if not isinstance(_id, str):
        return False
    if len(_id) < MIN_ID_LEN:
        return False
    return True


def length():
    return len(cities)


def create(fields: dict) -> str:
    if not isinstance(fields, dict):
        raise ValueError(f'Bad type for fields: {type(fields)}')
    if not fields.get(NAME):
        raise ValueError(f'Name missing in fields: {fields.get(NAME)}')

    _id = str(len(cities) + 1)
    cities[_id] = fields
    return _id
