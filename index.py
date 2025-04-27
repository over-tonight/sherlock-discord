import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/",intents=discord.Intents.all())

TOKEN = ''

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.tree.sync()

@client.tree.command()
async def name(interaction: discord.Interaction, name: str):
    guild = interaction.guild
    channel = await guild.create_text_channel(name)
    urls = [
        f'[+] Archive.org: https://archive.org/details/@{name}\n[+] Chess: https://www.chess.com/member/{name}\n[+] Duolingo: https://www.duolingo.com/profile/{name}',
        f'[+] Fiverr: https://www.fiverr.com/{name}\n[+] G2G: https://www.g2g.com/{name}\n[+] GunsAndAmmo: https://forums.gunsandammo.com/profile/{name}',
        f'[+] IRL: https://www.irl.com/{name}\n[+] Quizlet: https://quizlet.com/{name}\n[+] Reddit: https://www.reddit.com/user/{name}',
        f'[+] Replit.com: https://replit.com/{name}\n[+] Roblox: https://www.roblox.com/user.aspx?username={name}\n[+] Speedrun.com: https://speedrun.com/user/{name}',
        f'[+] Tenor: https://tenor.com/users/{name}\n[+] TikTok: https://tiktok.com/@{name}\n[+] Twitch: https://www.twitch.tv/{name}',
        f'[+] SoundCloud: https://soundcloud.com/{name}\n[+] Vimeo: https://vimeo.com/{name}\n[+] Pinterest: https://www.pinterest.com/{name}/',
        f'[+] Behance: https://www.behance.net/{name}\n[+] Medium: https://medium.com/@{name}\n[+] Yelp: https://www.yelp.com/user_details?userid={name}',
        f'[+] TripAdvisor: https://www.tripadvisor.com/members/{name}\n[+] Imgur: https://imgur.com/user/{name}\n[+] GitHub: https://github.com/{name}',
        f'[+] Gravatar: http://en.gravatar.com/{name}\n[+] authorSTREAM: http://www.authorstream.com/{name}/\n[+] AskFM: https://ask.fm/{name}',
        f'[+] DeviantART: https://{name}.deviantart.com/\n[+] Dribbble: https://dribbble.com/{name}\n[+] Snapchat: https://www.snapchat.com/add/{name}',
        f'[+] Scratch: https://scratch.mit.edu/users/{name}\n[+] Facebook: https://www.facebook.com/{name}\n[+] Steam: https://steamcommunity.com/id/{name}',
        f'[+] Genius: https://genius.com/{name}\n[+] Flickr: https://www.flickr.com/people/{name}/\n[+] Goodreads: https://www.goodreads.com/user/show/{name}',
        f'[+] HackerRank: https://www.hackerrank.com/{name}\n[+] Keybase: https://keybase.io/{name}\n[+] Last.fm: https://www.last.fm/user/{name}',
        f'[+] MyAnimeList: https://myanimelist.net/profile/{name}\n[+] Spotify: https://open.spotify.com/user/{name}\n[+] Stack Exchange: https://stackexchange.com/users/{name}',
        f'[+] Wikipedia: https://en.wikipedia.org/wiki/User:{name}\n[+] YouTube: https://www.youtube.com/@{name}\n[+] Twitter: https://twitter.com/{name}',
        f'[+] Instagram: https://www.instagram.com/{name}\n[+] LinkedIn: https://www.linkedin.com/in/{name}\n[+] Blogger: https://{name}.blogspot.com/',
        f'[+] WordPress: https://{name}.wordpress.com/\n[+] Tumblr: https://{name}.tumblr.com/\n[+] VK: https://vk.com/{name}\nDone {interaction.user}!',
    ]
    for x in urls:
        await channel.send(x)

client.run(TOKEN)
