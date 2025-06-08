from TeamSky.core.bot import TeamSky
from TeamSky.core.dir import dirr
from TeamSky.core.git import git
from TeamSky.core.userbot import Userbot
from TeamSky.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TeamSky()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
