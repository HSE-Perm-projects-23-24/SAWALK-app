import time as t


async def get_greeting() -> str:
    """
    Функция для получения правильного текста приветствия
    :return: Текст приветствия
    """
    hours_now = t.localtime(t.time()).tm_hour
    if 21 < hours_now < 6:
        return "Здравствуйте"
    elif hours_now < 10:
        return "Доброе утро"
    elif hours_now < 17:
        return "Добрый день"
    else:
        return "Добрый вечер"
