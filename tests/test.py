import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from .config.config import *
    from .business_logic.ac_functions import try_sign_in
    from .business_logic.get_functions import *
    from .business_logic.get_functions import _put_user, _del_user
    from .business_logic.securiry_functions import *
except ImportError:
    from business_logic.ac_functions import try_sign_in, check_login_on_existing
    from config.config import *
    from business_logic.get_functions import *
    from business_logic.get_functions import _put_user, _del_user
    from business_logic.security_functions import *


class TestConfig(unittest.TestCase):
    def test_ac_path(self):
        """
        Проверка наличия пути до папки с базами от аккаунтов

        """
        result = os.path.exists(PATH_TO_ACCOUNTS)
        self.assertEqual(result, True)

    def test_xp_path(self):
        """
        Проверка наличия пути до папки с базами от расходов

        """
        result = os.path.exists(PATH_TO_EXPENS)
        self.assertEqual(result, True)

    def test_tp_path(self):
        """
        Проверка наличия пути до Temp папки

        """
        result = os.path.exists(PATH_TO_TEMP)
        self.assertEqual(result, True)

class TestAcFunctions(unittest.TestCase):
    def test_sign_in(self):
        """
        Проверка входа

        """
        result = try_sign_in("812hg387213", "asdqw11212")
        self.assertEqual(result, False)

    def test_check_login_on_existing(self):
        """
        Проверка на существование логина в базе

        """
        resust = check_login_on_existing("jjjwefi1ir2942")
        with self.assertRaises(AttributeError):
            result2 = check_login_on_existing(11213)

        self.assertEqual(resust, False)

class TestGetFunctions(unittest.TestCase):
    def test_get_base_dir(self):
        """
        Проверка корректного возврата базовой дирректории

        """
        result = get_base_dir()
        self.assertEqual(isinstance(result, str), True)
        self.assertEqual(result, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def test_get_path_ac(self):
        """
        Проверка корректного возврата пути до базы данных с аккаунтами str

        """
        result = get_path_ac()
        self.assertEqual(isinstance(result, str), True)
        self.assertEqual(result, PATH_TO_ACCOUNTS + DB_FOR_ACCOUNTS)

    def test_get_tb_ac(self):
        """
        Проверка корректного возврата имени таблицы для аккаунтов str

        """
        result = get_tb_ac()
        self.assertEqual(isinstance(result, str), True)
        self.assertEqual(result, TABLE_FOR_ACCOUNTS)

    def test_get_path_xp(self):
        """
        Проверка корректного возврата пути до базы данных с расходами

        """
        result = get_path_xp()
        self.assertEqual(isinstance(result, str), True)
        self.assertEqual(result, PATH_TO_EXPENS)

    def test_get_path_temp(self):
        """
        Проверка корректного возврата пути до Temp базы

        """
        result = get_path_temp()
        self.assertEqual(isinstance(result, str), True)
        self.assertEqual(result, PATH_TO_TEMP + DB_FOR_TEMP)

    def test_put_user(self):
        """
        Проверка корректной установки пользователя

        """
        result = _put_user('zaraza')
        self.assertEqual(result, 'zaraza')

    def test_del_user(self):
        """
        Проверка корректного удаления пользователя

        """
        result = _del_user()
        self.assertEqual(result, '')

    def test_get_user(self):
        """
        Проверка корректного получения пользователя

        """
        _put_user('7YT6214u!#$89j7h234h')
        result = get_user()
        _del_user()
        self.assertEqual(result, '7YT6214u!#$89j7h234h')

    def test_get_path_to_database(self):
        """
        Проверка корректного получения пути до базы данных пользователя

        """
        _put_user('7YT6214u!#$89j7h234h')
        result = get_path_to_database()
        _del_user()
        self.assertEqual(result, PATH_TO_EXPENS + '7YT6214u!#$89j7h234h.db')

class TestSecurityFunctions(unittest.TestCase):

    def test_get_password(self):
        """ Проверка корректности возвращаемого пароля """

        result2 = get_password('qwef!!3r0dawd7', '2143ereg4345')

        with self.assertRaises(TypeError):
            result3 = get_password(12424525, 435347614)
            result = get_password('qwef!!3r0dawd7', 1390984374)

        self.assertEqual(result2, 'f1a4723eab99adb5cf24b279971fea4a6d40b335')


    def test_get_login(self):
        """ Проверка корректности возвращаемого логина """
        result = get_login('asdqwrыфайца')


        with self.assertRaises(AttributeError):
            result2 = get_login(124123)

        self.assertEqual(result, '30ae4db95b1101811f6989ee3eb00d841e7f49c8')




if __name__ == '__main__':
    unittest.main()
