class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6710268098"
    sudo_users = "7080925947 6959003848"
    GROUP_ID = -1002079755812
    TOKEN = "6782667556:AAGImAWRJbss9BXEpALCjisaxYVMC7sKUt0"
    mongo_url = "mongodb+srv://Shadizinho:Ggae4304,,@animehw.kdajkvp.mongodb.net/"
    PHOTO_URL = ["https://telegra.ph/file/e799d64db218df244d187.jpg", "https://telegra.ph/file/9bfd5dfc5633040cd8b8f.jpg"]
    SUPPORT_CHAT = "AnimeHW_sup"
    UPDATE_CHAT = "AnimeHW_sup"
    BOT_USERNAME = "AnimeHW_bot"
    CHARA_CHANNEL_ID = "-1002028837181"
    api_id = 21732614
    api_hash = "ff91cccbb310e68d0b93320abb2d229d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
