import requests
from time import sleep


class IikoToken:

    def __init__(self, login: str, password: str):
        self.Login = login
        self.Password = password
        self.Token = ""
        self.isErorr = False
        self.ErrorCode = ""

    def get_token(self):
        """Получить токен"""

        def setstatus(token: str, iserror: bool, errorcode: str):
            self.Token = token
            self.isErorr = iserror
            self.ErrorCode = errorcode

        try:
            url = 'https://iiko.biz:9900/api/0/auth/access_token?user_id=' + \
                  self.Login + "&user_secret=" + self.Password
            response = requests.get(url, timeout=5)
            if response.ok:
                # logger.info('Получение токена. Токен получен ')
                setstatus(response.json(), False, "")
            else:
                # logger.error('Получение токена. Response <> 200')
                # return response.json()
                setstatus("", True, response.json())
        except Exception as error:
            setstatus("", True, repr(error))
            # logger.error('Получение токена. Ошибка соединения с сервером.' + repr(error))


def main():
    while True:
        token = IikoToken('ipgaranin@gmail.com', 'BambooK2020')
        token.get_token()
        print(token.Token)
        print(token.isErorr)
        print(token.ErrorCode)
        sleep(2)

main()