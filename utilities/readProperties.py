from configparser import ConfigParser

config = ConfigParser()
config.read("D://python//HybridFramework//Configurations//config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('COMMON', 'baseurl')
        return url

    @staticmethod
    def get_username():
        username = config.get('COMMON', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('COMMON', 'password')
        return password
