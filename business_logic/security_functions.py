import hashlib
def get_password(login: str, password: str) -> str:
    """
    Формирование пароля для пользователя, возвращает строку с паролем

    """
    proper = ''
    lengns = [len(login), len(password)]
    for idx in range(max(lengns)):
        try:
            proper += login[idx]
        except:
            pass
        try:
            proper += password[idx]
        except:
            pass
    h = hashlib.sha1(proper.encode())
    return h.hexdigest()

def get_login(login: str) -> str:
    """
    Формирование логина пользователя, возвращает строку с логином

    """
    h = hashlib.sha1(login.encode())
    return h.hexdigest()
