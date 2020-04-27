#id [place id here]
#token [place your token here]
#perm. int 68672
#[perms link]
import discord
import random
from googletrans import Translator
translator = Translator()
client = discord.Client()
LANGUAGES = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co',
    'hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw',
    'hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt',
    'lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','pa','ro','ru','sm',
    'gd','sr','st','sn','sd','si','sk', 'sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur',
    'uz','vi', 'cy','xh','yi','yo','zu','fil','he']
@client.event # event dec/wrapper
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    strmess = str(message.content.lower())
    if "translate it:" in strmess:
        strmess=strmess.lstrip('translate it:')
        await message.channel.send('Working on it...')
        ind = 0
        while ind<5 :
            print(ind)
            rn = random.randint(0,105)
            print(LANGUAGES[rn])
            strmess = (translator.translate(strmess, dest=LANGUAGES[rn])).text

            ind=ind+1
        strmess = (translator.translate(strmess, dest='en')).text
        await message.channel.send(strmess)
client.run("NjkzODU1MzQ5OTI4ODg2MzMz.XoDKKw.2upB2uPQ8vgpR6h7a-KK2i8tuzw")
