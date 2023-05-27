from environs import Env

# environs kitapxanasınan paydalanıw
env = Env()
env.read_env()

# .env fayl ishinen tómendegilerdi oqıymız
BOT_TOKEN = env.str("BOT_TOKEN")  # bot token
ADMINS = env.list("ADMINS")  # adminler listi
IP = env.str("ip")  # xosting ip adress
