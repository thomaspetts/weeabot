import discord
from discord.ext.commands import Bot
from discord.ext import commands

weeabot = Bot(command_prefix='!')

@weeabot.event
async def on_ready():
    print('{} online'.format(weeabot.user.name))
    await weeabot.change_presence(game=discord.Game(name='v0.5 !help'))


#reaction
@weeabot.command()
async def shame():
    await weeabot.say('Shame on you all, especially Dai')

@weeabot.command()
async def thot():
    await weeabot.say('https://www.youtube.com/watch?v=AFCxHmtHTGU')

@weeabot.command()
async def normie():
    await weeabot.say('https://www.youtube.com/watch?v=rVqSneiRAVc')

@weeabot.command()
async def snussy():
    await weeabot.say('ALL HAIL THE ALMIGHTY SNUSSY :snail:')

@weeabot.command()
async def smite():
    await weeabot.say('There is no god because this post killed it')

@weeabot.command()
async def weeb():
    await weeabot.say('Weeabot is here to escort you to weeb prison')

@weeabot.command()
async def clap():
    await weeabot.say('https://www.youtube.com/watch?v=1Bix44C1EzY')

#people
@weeabot.command()
async def bees():
    await weeabot.say('Degeneracy? In MY Christian server?')

@weeabot.command()
async def donna():
    await weeabot.say('Hide your children')

@weeabot.command()
async def natasha():
    await weeabot.say('SLSPPSLPSLPSLSPLSPLSPLSPSLPS')

@weeabot.command()
async def dai():
    await weeabot.say('EuroCuck spotted')

@weeabot.command()
async def thomas():
    await weeabot.say('Keep refridgerated and away from Donna')

@weeabot.command()
async def jojo():
    await weeabot.say('Show us that bloccy boi')

@weeabot.command()
async def monster():
    await weeabot.say('The meatiest of bois')

@weeabot.command()
async def joss():
    await weeabot.say('The moon is **h o l l o w**')

@weeabot.command()
async def kenah():
    await weeabot.say("Paging satan to Dr. McKenah's office")

@weeabot.command()
async def scoot():
    await weeabot.say("Today I will once more be a prophet: "
                      "If the international Weeb messages in and outside "
                      "Discord should succeed in plunging the nations once more "
                      "into a world war, then the result will not be the "
                      "Bolshevization of the earth, and thus the victory "
                      "of Weebs, but the annihilation of the messages in Discord!")
 


#sins
@weeabot.command()
async def sin_bees():
    with open('sin_bees.txt') as a:
            num = int(a.read())
            num = num + 1
            num2 = str(num)
    with open('sin_bees.txt', 'w') as a1:
            a1.write(num2)
    await weeabot.say('Bees has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_dai():
    with open('sin_dai.txt') as b:
            num = int(b.read())
            num = num + 1
            num2 = str(num)
    with open('sin_dai.txt', 'w') as b1:
            b1.write(num2)
    await weeabot.say('Dai has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_donna():
    with open('sin_donna.txt') as c:
            num = int(c.read())
            num = num + 1
            num2 = str(num)
    with open('sin_donna.txt', 'w') as c1:
            c1.write(num2)
    await weeabot.say('Donna has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_jojo():
    with open('sin_jojo.txt') as d:
            num = int(d.read())
            num = num + 1
            num2 = str(num)
    with open('sin_jojo.txt', 'w') as d1:
            d1.write(num2)
    await weeabot.say('Jojo has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_joss():
    with open('sin_joss.txt') as e:
            num = int(e.read())
            num = num + 1
            num2 = str(num)
    with open('sin_joss.txt', 'w') as e1:
            e1.write(num2)
    await weeabot.say('Joss has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_kenah():
    with open('sin_kenah.txt') as f:
            num = int(f.read())
            num = num + 1
            num2 = str(num)
    with open('sin_kenah.txt', 'w') as f1:
            f1.write(num2)
    await weeabot.say('Kenah has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_natasha():
    with open('sin_natasha.txt') as g:
            num = int(g.read())
            num = num + 1
            num2 = str(num)
    with open('sin_natasha.txt', 'w') as g1:
            g1.write(num2)
    await weeabot.say('Natasha has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_scoot():
    with open('sin_scoot.txt') as h:
            num = int(h.read())
            num = num + 1
            num2 = str(num)
    with open('sin_scoot.txt', 'w') as h1:
            h1.write(num2)
    await weeabot.say('Scoot has now sinned ' + num2 + ' times')


@weeabot.command()
async def sin_thomas():
    with open('sin_thomas.txt') as i:
            num = int(i.read())
            num = num + 1
            num2 = str(num)
    with open('sin_thomas.txt', 'w') as i1:
            i1.write(num2)
    await weeabot.say('Thomas has now sinned ' + num2 + ' times')

@weeabot.command()
async def repent():
    with open('sin_bees.txt') as a:
            acount = 'Bees has ' + a.read() + ' sins to repent'
    with open('sin_dai.txt') as b:
            bcount = 'Dai has ' + b.read() + ' sins to repent'
    with open('sin_donna.txt') as c:
            ccount = 'Donna has ' + c.read() + ' sins to repent'
    with open('sin_jojo.txt') as d:
            dcount = 'Jojo has ' + d.read() + ' sins to repent'
    with open('sin_joss.txt') as e:
            ecount = 'Joss has ' + e.read() + ' sins to repent'
    with open('sin_kenah.txt') as f:
            fcount = 'Kenah has ' + f.read() + ' sins to repent'
    with open('sin_natasha.txt') as g:
            gcount = 'Natasha has ' + g.read() + ' sins to repent'
    with open('sin_scoot.txt') as h:
            hcount = 'Scoot has ' + h.read() + ' sins to repent'
    with open('sin_thomas.txt') as i:
            icount = 'Thomas has ' + i.read() + ' sins to repent'

    await weeabot.say(acount + '\n' + bcount + '\n' + ccount + '\n' +
                      dcount + '\n' + ecount + '\n' + fcount + '\n' +
                      gcount + '\n' + hcount + '\n' + icount + '\n')






















weeabot.run('MzQyNzAyNTU0MTU0NTMyODg0.DGTeIw.ByqdaBju_XxATEMuRAVX9J9wrAU')
