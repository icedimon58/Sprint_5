import random
class AdditionalFunctions:
    MAILS = ('@yandex.ru', '@bk.ru', '@mail.ru')

    def generate_password(self):
        return random.randint(100000, 999999)

    def generate_wrong_password(self):
        return random.randint(1, 99999)

    def generate_email(self):
        return f'{self.generate_password()}{random.choice(self.MAILS)}'

