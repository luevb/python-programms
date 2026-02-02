valid_value = (".com", ".ru", ".net")
not_valid_value = ("@@", "@.", "..", "com.", "ru.", "net.")


def check(recipient, sender):
    if "@" in recipient and "@" in sender:
        if recipient.endswith(valid_value) and sender.endswith(valid_value):
            for x in not_valid_value:
                if x in recipient or x in sender:
                    return False
            return True


def send_emails(message, recipient, *, sender="university.help@gmail.com"):
    if check(recipient, sender) == True:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено "
                  f"с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса "
              f"{sender} на адрес {recipient}")


send_emails('hello', "123@asd.net.com")
send_emails("Это сообщение для проверки связи", "vasya1338@gmail.com")
send_emails("wtf", "apple@id.com", sender="1332gmgmg@maill.ru")
send_emails('pepeshne', 'poppepe@mail.ru', sender="apa@example.uk")
send_emails("brother", "university.help@gmail.com")