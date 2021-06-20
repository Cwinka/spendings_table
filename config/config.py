import os

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#  путь до папки с базой данных пользователей
PATH_TO_ACCOUNTS: str = BASE_DIR + "\\databases\\accounts\\"
DB_FOR_ACCOUNTS: str = 'accounts.db'
TABLE_FOR_ACCOUNTS: str = DB_FOR_ACCOUNTS[:-3]

#   путь до папки с базой даннных изера
PATH_TO_EXPENS: str = BASE_DIR + '\\databases\\expenses\\'

#  Путь до папки с базой данных временных фалов юзера
PATH_TO_TEMP: str = BASE_DIR + '\\TEMP\\'
DB_FOR_TEMP: str = 'temp.db'
