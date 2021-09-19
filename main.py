from instabot import Bot

def upload(uname, paswd):
    bot = Bot()

    bot.login(username=uname, password=paswd)
    bot.upload_photo("PathOfPicInMachine", caption="Caption")


if __name__ == '__main__':
    try:
        upload(input("Enter username: "), input("Enter Password"))
    except:
        print("Invalid ID or Password: ")
