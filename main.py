# Copyright 2018 Slowly/slowlygoingon

import discord
import random
import datetime
from discord.ext import commands
import os
import sys

bot = commands.Bot(
    description='Official bot for The Campfire Discord server! Memes, fun and wholesomeness.',
    command_prefix='vb!')
timenow = datetime.datetime.utcnow()
bot.remove_command('help')


@bot.event
async def on_ready():
    game = discord.Game(name="a ball of yarn | vb!help")
    await bot.change_presence(status=discord.Status.online, activity=game)
    readymessage = "Hi, I'm going out for a hike! It is " + str(timenow) + "\n" + "System version: " + (sys.version)
    uptimedict['timeuptime'] = timenow
    print(readymessage)


uptimedict = {
    'timeuptime': 0,
}


class Moderating():

    @commands.command(aliases=['prune', 'purge', 'delete'])
    @commands.has_role('Staff')
    async def clear(self, ctx, amount):
        errormessage = discord.Embed(title="Error!", description="You can delete min 1 / max 100 messages at once.", color=0xd90000)
        channel = ctx.channel
        for amount in range(int(amount), 0, (-100)):
            if 101 > amount > 0:
                await channel.purge(limit=int(amount))
            else:
                await ctx.send(embed=errormessage)


    @commands.command()
    @commands.has_role('Staff')
    async def kick(self, ctx, user: discord.Member):
        await ctx.guild.kick(user)
        await ctx.send(f'{user.name} has been kicked.')


class Info():
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! Did you call me?")

    @commands.command(aliases=['git', 'github', 'src'])
    async def source(self, ctx):
        link = "https://github.com/slowlygoingon/VenturerBot/"
        await ctx.send(link)

    @commands.command(aliases=['about'])
    async def info(self, ctx):
        uptimemessage = ("I've been online since " + str(uptimedict['timeuptime'])) + ' UTC.'
        em = discord.Embed(
            title='About this bot', description='All about Venturer Bot.', colour=0x082E6F)
        em.add_field(name='Developer', value='Slowly#1846', inline=False)
        em.add_field(
            name='Thank-yous',
            value="Special thanks to Sebi's Bot Tutorial, this bot wouldn't have been possible without your help.",
            inline=False)
        em.add_field(name='Uptime', value=uptimemessage, inline=False)
        em.add_field(name='Version', value='Still in development.', inline=False)
        await ctx.send(embed=em)

    @commands.command(aliases=['help', 'cmds', 'commandlist', 'commandslist'])
    async def commands(self, ctx):
        em = discord.Embed(
            description=
            'These are all the commands of Venturer Bot.\nThe words in [] are aliases.\n\n•  •  •  •  •  •  •  •  •', colour=0x082E6F)
        em.add_field(
            name='INFO',
            value=
            "**info**   -   Shows basic info about the bot. [about]\n**commands**   -   Shows this message. [help, commandslist]\n**ping**   -   Hey Venturer Bot, you there?\n**source**   -   Shows bot's source code. [src, git, github]",
            inline=False)
        em.add_field(
            name='FUN AND MISC.',
            value=
            '**positivity**   -   Sends a nice gif!\n**say**   -   Bot repeats what you say. [echo]\n**compliment**   -   Displays a random compliment or says something reassuring. [randomcompliment, reassuring]\n**dice**   -   Throws a dice. [dicethrow, throwdice]\n**coinflip**   -   Flips a coin. [coin, flipcoin]\n**question**   -   Ask the bot a yes or no question. [ask]\n**dog**   -   Displays a random dog.\n**cat**   -   Displays a random cat.\n**cornyjoke**   -   Makes a corny joke. [joke, pun, randomjoke, randompun]\n**givecookie**   -   Give someone a cookie. [cookie]\n**hug**   -   Give someone a hug. [givehug, hugs, givehugs]',
            inline=False)
        em.add_field(
            name='MODERATING (Staff only)',
            value=
            '**clear**   -   Delete messages. [prune, purge, delete]\n**kick**   -   Kicks a user.',
            inline=False)
        await ctx.send(embed=em)


class Fun():
    @commands.command(aliases=['coin', 'flip', 'flipcoin'])
    async def coinflip(self, ctx):
        choices = random.choice(['Heads!', 'Tails!'])
        await ctx.send(choices)

    @commands.command(aliases=['say', 'talk'])
    async def echo(self, ctx, *, something):
        error = discord.Embed(
            title='Error!', description="Don't ping with bot commands, thank you.", colour=discord.Colour.red())
        errorm = discord.Embed(
            title='Error!', description='Did you seriously just try to mass-ping?', colour=discord.Colour.red())
        messagetosend = '{0.author} just tried to mass-ping.'.format(ctx.message)
        if ('@' in ctx.message.content) and ('@someone' not in ctx.message.content):
            await ctx.send(embed=error)
        if '@everyone' in ctx.message.content:
            await ctx.send(embed=errorm)
            await (await bot.get_user_info(345307151989997568)).send(messagetosend)
        if ('@' not in ctx.message.content) or ('@someone' in ctx.message.content):
            await ctx.send(something)

    @commands.command()
    async def cat(self, ctx):
        catlist = random.choice([
            "Here's a random cat from our selection of cute pics.\nhttps://pixnio.com/free-images/2017/09/26/2017-09-26-10-10-28-1100x728.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://cdn.pixabay.com/photo/2017/09/16/01/38/sleeping-cat-2754329_960_720.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/160000/velka/mignon-petit-chaton.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/240000/velka/little-kitten-1515265224ojM.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/240000/velka/little-kitten-1515269648ppg.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/220000/velka/chat-chatte-femelle.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/80000/velka/resting-cat.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/90000/velka/kitten-looking-up.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/270000/velka/gray-kitten-with-pink-bow.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://images.pexels.com/photos/256632/pexels-photo-256632.jpeg",
            "Here's a random cat from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/220000/velka/kitten-1494854108zz6.jpg",
            "Here's a random cat from our selection of cute pics.\nhttps://images.pexels.com/photos/127028/pexels-photo-127028.jpeg"])
        await ctx.send(catlist)

    @commands.command()
    async def dog(self, ctx):
        doglist = random.choice([
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/264206/pexels-photo-264206.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/374898/pexels-photo-374898.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/230784/pexels-photo-230784.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/356378/pexels-photo-356378.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/1009922/pexels-photo-1009922.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/110000/velka/cute-little-puppy-eyes.jpg",
            "Here's a random dog from our selection of cute pics.\nhttps://www.publicdomainpictures.net/pictures/240000/velka/french-bulldog-puppy-portrait-1509041878usp.jpg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/977281/pexels-photo-977281.jpeg",
            "Here's a random dog from our selection of cute pics.\nhttps://images.pexels.com/photos/9080/night-garden-yellow-animal.jpg",
            "Here's a random dog from our selection of cute pics.\nhttps://c.pxhere.com/photos/c4/8f/weimaraner_puppy_dog_snout_animal_portrait-626898.jpg",
            "Here's a random dog from our selection of cute pics.\n\n(source: <https://liveoncelivewild.com/>)\n\nhttps://c1.staticflickr.com/1/269/32683801096_5b7598b75c_b.jpg"])
        await ctx.send(doglist)

    @commands.command(aliases=['positive'])
    async def positivity(self, ctx):
        pos = random.choice([
            "Hey there, here's your daily nice gif.\n        https://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4",
            "Hey there, here's your daily nice gif. (source: teenypinkbunny)\n        https://78.media.tumblr.com/8b468c1f9c20ca5f9483da6753460ec2/tumblr_onfpirBibx1tyggbco1_1280.gif",
            "Hey there, here's your daily nice gif.\n        https://giphy.com/gifs/chuber-turtle-hang-in-there-l1J3zw3sgJ6Ye6I4E",
            "Hey there, here's your daily nice gif.\n        https://78.media.tumblr.com/c0a1ffdef8c5b710769595cdf1119356/tumblr_on4s1k5Gru1w7ymkuo1_500.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\n        https://78.media.tumblr.com/8317376ec2f138b962d7dec63d479c46/tumblr_os6c25dzp21w4zse0o1_r1_500.gif",
            "Hey there, here's your daily nice gif. (source: gogh-save-the-bees)\n        https://78.media.tumblr.com/a92282dfc57d01e2e29184e3ed12fa5d/tumblr_otngozhihv1ut0lfho1_400.gif",
            "Hey there, here's your daily nice gif.\n        https://78.media.tumblr.com/7ba86c4cbc0b0f8fc981ca780fe8bb61/tumblr_osdkc2EJZL1w4zse0o1_1280.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\n        https://78.media.tumblr.com/3914e99610371d427989d5146c42b85e/tumblr_p0981oKsrJ1vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\n        https://78.media.tumblr.com/2bbe256eba6d07ea6df9698dd20dfa65/tumblr_ot4afrYG181w4zse0o1_500.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\n        https://78.media.tumblr.com/6acf4ed92328f675ae8890df51b23794/tumblr_os27xwOzXz1w4zse0o1_500.gif",
            "Hey there, here's your daily nice gif. (source: vanish)\n        https://78.media.tumblr.com/ca9372839569a8406c0709bcc50a15ec/tumblr_p2iebnGUZr1sga7ujo1_500.gif",
            "Hey there, here's your daily nice gif.\n        https://78.media.tumblr.com/e0e093271b5657b75000f693bb48d877/tumblr_opy7xzfkJS1tssyz8o1_500.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\n        https://78.media.tumblr.com/91fbd29211a1c7b06e7a16adf2deae50/tumblr_ozl7ooyZxQ1vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\n        https://78.media.tumblr.com/dd5e45b3690ac2e979bc694ea473cf0b/tumblr_oyo1zfEii61vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: gogh-save-the-bees)\n        https://78.media.tumblr.com/4b8c9b079cd3da2d74275d3063d83b72/tumblr_oxidf7tQjz1ut0lfho1_500.gif",
            "Hey there, here's your daily nice gif. (source: magical-latte)\n        https://78.media.tumblr.com/d2fa0d7d4ca67af23750bb79a674d5c2/tumblr_p67f6ugJp91x69labo1_500.gif",
            "Hey there, here's your daily nice gif.\n        https://78.media.tumblr.com/85efdd7380284bd7279a0839e9674f96/tumblr_oqish5aNqX1ufccs2o1_500.gif",
            "Hey there, here's your daily nice gif. (source: faiemagick)\n        https://78.media.tumblr.com/bf7cad140e3e113cd4062b0377842ca3/tumblr_otogrpArAo1wo3hpco1_1280.gif"
        ])
        await ctx.send(pos)

    @commands.command(aliases=['hug', 'hugs', 'givehugs'])
    async def givehug(self, ctx):
        botmention = discord.Embed(description="T-thank you! I feel so loved now...", colour=0x082E6F)
        botmention.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")
        normalmention = discord.Embed(description="Aw, you just gave them a cookie. How sweet of you!", colour=0x082E6F)
        normalmention.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")
        me = discord.Embed(description="There you go. Enjoy your cookie!", colour=0x082E6F)
        me.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")

        if ctx.me.mention in ctx.message.content:
            await ctx.send(embed=botmention)
        elif '@' in ctx.message.content:
            await ctx.send(embed=normalmention)
        elif 'me' in ctx.message.content:
            await ctx.send(embed=me)

    @commands.command(aliases=['reassuring', 'randomcompliment', 'comfort', 'comforting'])
    async def compliment(self, ctx):
        randomcomp = random.choice([
            "You're so resourceful.", "You're such a strong person.", 'Your light shines so brightly.',
            'You matter, and a lot.', 'You are so brave.', "You have an incredible talent even if you don't see it.",
            'You are deserving of a hug right now.', "You're more helpful than you realize.", 'You can inspire people.',
            'I bet you do the crossword puzzle in ink.',
            "You're someone's reason to smile, even if you don't realize it.",
            "It's so great to see you're doing your best.", "Your smile can make someone's day.",
            "You've always ben able to always figure out how to pick yourself up.", 'Your ideas matter.',
            'Your feelings matter.', 'Your emotions matter.', 'Your opinions matter.', 'Your needs matter.',
            'Your own vision of the world is unique and interesting.',
            "Even if you were cloned, you'd still be one of a kind. (And the better one between the two.)",
            'You are more unique and wonderful than the smell of a new book.',
            "You're great at being you! No one can replace you - so keep it up.", 'You can get through this.',
            "If you're going through something, remember: this too shall pass.",
            'You deserve to get help if you need it.', 'You - yes you - are valid.', 'You are more than enough.',
            'Your presence is appreciated.', 'You can become whoever you want to be.', 'You deserve to be listened to.',
            'You deserve to be heard.', 'You deserve to be respected.', "You're an absolute bean.",
            'You’re trying your best and everyone sees that.',
            "Even if you feel like you're getting nowhere you're still one step ahead of yesterday - and that's still progress.",
            "You're growing so much, and if you can't see it now, you certainly will in a few months.",
            "You're strong for going on even when it's so hard."
        ])
        await ctx.send(randomcomp)

    @commands.command(aliases=['throwdice', 'dicethrow', 'throw'])
    async def dice(self, ctx):
        throw = random.choice(['1.', '2.', '3.', '4.', '5.', '6.'])
        await ctx.send(throw)

    @commands.command(aliases=['cookie'])
    async def givecookie(self, ctx):
        botmention = discord.Embed(description="Wow, thanks! I love cookies >///<", colour=0x082E6F)
        botmention.set_thumbnail(url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")
        normalmention = discord.Embed(description="Aw, you just gave them a cookie. How sweet of you!", colour=0x082E6F)
        normalmention.set_thumbnail(url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")
        me = discord.Embed(description="There you go. Enjoy your cookie!", colour=0x082E6F)
        me.set_thumbnail(url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")

        if ctx.me.mention in ctx.message.content:
            await ctx.send(embed=botmention)
        elif '@' in ctx.message.content:
            await ctx.send(embed=normalmention)
        elif ('me' in ctx.message.content) or ('Me' in ctx.message.content):
            await ctx.send(embed=me)

    @commands.command(
        aliases=['joke', 'jokes', 'cheesyjoke', 'randomjoke', 'pun', 'randompun', 'cheesypun', 'cornypun', 'puns'])
    async def cornyjoke(self, ctx):
        randomjoke = random.choice([
            'What do you call a thieving alligator? A crookodile.',
            "What did the watermelon say to the cantaloupe? You're one in a melon.",
            'How do you put a baby alien to sleep? You rocket.', 'How do you throw a space party? You planet.',
            'What do you call a bear with no teeth? A gummy-bear.', 'What does a house wear? Address.',
            'Why is it hard to be in a relationship with a thief? Because they always take things... literally.',
            "Why can't a bycycle stand on its own? Because it's two tired.", 'Do french people play videogames? Wii.',
            "Did you hear about the joke about German sausages? It's the wurst.",
            'What does a falling star say to start a fight? Comet me bro.',
            "What did E.T.'s mother say to him when he got home? 'Where on Earth have you been?!'",
            "Why are calendars so popular? They have lots of dates.",
            'Why do musicians always get good grades? They have lots of notes.',
            'What did the traffic light say to the car? Don’t look! I’m about to change.',
            'Why was the little strawberry crying? Its mom was in a jam.',
            'Why are frogs so happy? They eat whatever bugs them.',
            'What do you call a guy with a rubber toe? Roberto.',
            'What do you call a bee that’s having a bad hair day? A frisbee.',
            "Why wouldn't the shrimp share his treasure? Because it was a little shellfish.",
            'If a seagull flies over the sea, what flies over the bay? A bagel.',
            'What happens to deposed kings? They get throne away.',
            'What kind of tree do fingers grow on? A palm tree.', 'What do you call a rabbit with fleas? Bugs Bunny.',
            'What happens to illegally parked frogs? They get toad away.',
            'What do you call a fish with no eyes? A fsh.', 'What do prisoners use to call each other? Cell phones.',
            "What happens when a clock's hungry? It goes back four seconds.",
            'How was Rome split in two? With a pair of Ceasars.',
            'What did the corn say in response to a compliment? Aw, shucks.',
            'What do you tell maize on graduation day? Corn-gratulations.',
            'What do you call a beautiful pumpkin? GOURDgeous.', 'What did the buffalo say to his son? Bison.',
            'What do you call a fake noodle? An impasta.', 'How do trees access the internet? They log on.',
            'What do you call a pirate who sells corn? A buccaneer.',
            'Want to hear a pizza joke? Actually never mind, it’s too cheesy.',
            "Why shouldn't you trust atoms? They make up everything.",
            "What do you call a pile of cats? A meow-ntain.",
            "An Italian chef has died. He pasta way.",
            "What kind of cup can't you drink out of? A cup-cake.",
            """Two antennas met on a roof, fell in love and got married. The ceremony wasn't much, but the reception was excellent.""",
            "An Irishman walks out of a bar.",
            "I was diagnosed with clinical depression the other day... Which made me sad.",
            "I spent five minutes fixing a broken clock yesterday. At least, I *think* it was five minutes...",
            "I once made a belt out of clocks. It was a waist of time.",
            "Learning how to collect trash wasn't hard. I just picked it up as I went along.",
            "What's red and bad for your teeth? A brick.",
            "I'd tell you my construction joke but I'm still working on it.",
            "Why do Norwegians build their own tables? No Ikea!",
            "There's been an explosion at a cheese factory in Paris. There's nothing left but de Brie.",
            "No matter how kind you are, German children are kinder.",
            """I've fallen in love with a pencil and we're getting married. I can't wait to introduce my parents to my bride 2B.""",
            "What did the baby corn say to the mama corn? 'Where is my pop corn?'",
            "Not all math puns are bad. Just sum.",
            "I went to the zoo the other day, there was only one dog in it. It was a shitzu...",
            "RIP boiled water. You will be mist.",
            """- Knock knock.
- Who's there?
- To.
- To who?
- To ***whom***.""",
            "Working in a bank must be awful. I bet it gets loanly in there sometimes."

        ])
        await ctx.send(randomjoke)

    @commands.command(aliases=['ask'])
    async def question(self, ctx):
        quest = random.choice([
            'Yes.', 'No.', 'Yes!', 'No!', 'What? No!', 'Probably not.', 'Maybe...', 'Always.', 'Never.', 'Sometimes...',
            'Almost certainly.', 'I hope not!', "I hope so!", 'Yep!', 'Yes...?', 'No...?', 'Always!', 'Never!', 'Not sure...',
            'Of course!', 'Of course not!', 'Of course.', 'DUH!', 'Why not?', 'Why though?', "Absolutely not!", "Absolutely not.", "Perhaps.", "Who knows..."
        ])
        await ctx.send(quest)


bot.add_cog(Info())
bot.add_cog(Fun())
bot.add_cog(Moderating())
bot.run(os.getenv('discord_client_key'))
