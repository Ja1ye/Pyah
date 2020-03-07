import tweepy
import discord
import random
import time
from discord.ext import commands
from funk import uwuify




auth = tweepy.OAuthHandler()
auth.set_access_token()
api = tweepy.API(auth)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

    async def on_message(self, message):
        if '!pyah' in message.content.lower()[:5]:
            await message.channel.send('```Twitter Account is @Pyahdoesthis``` Commands:')
            await message.channel.send('*!twit [message] - tweets a message*')
            await message.channel.send('```ex: !twit i love you @conqueringsog```')
            await message.channel.send('*!twituwu [message] - tweets an uwuified message*')
            await message.channel.send('```ex: !twituwu connor come back to me```')
            await message.channel.send('*!follow [user] - follows the user*')
            await message.channel.send('```ex: !follow conqueringsog```')
            await message.channel.send('*!unfollow [user] - unfollows the user*')
            await message.channel.send('```ex: !unfollow avahatesjava```')
            await message.channel.send('*!like [link to tweet] - likes tweet linked')
            await message.channel.send('```!like https://twitter.com/avahatesjava/status/1212614080285904896?s=20```')
            await message.channel.send('*!unlike [link to tweet] - unlikes tweet linked')
            await message.channel.send('```!unlike https://twitter.com/avahatesjava/status/1212614080285904896?s=20```')
            await message.channel.send('*!name [text] - changes the display name')
            await message.channel.send('```!name Pyah```')
            await message.channel.send('*!bio [text] - changes the bio')
            await message.channel.send('```!bio Community-run account and possible  train-wreck```')
            await message.channel.send('*!retweet [link to tweet] - retweets tweet linked')
            await message.channel.send('```!retweet https://twitter.com/avahatesjava/status/1212614080285904896?s=20```')
            await message.channel.send('*!unretweet [link to tweet] - unretweets tweet linked')
            await message.channel.send('```!unretweet https://twitter.com/avahatesjava/status/1212614080285904896?s=20```')
            await message.channel.send('*!deltwit [link to own tweet] - deletes own tweet linked')
            await message.channel.send('```!deltwit https://twitter.com/pyahdoesthis/status/1215429778301489154?s=20```')


        slurs = ['fag','faggot','i hate gays','i hate the gays','nigg','nigger','nigga','negro','trump','jew','blacks']
        bannedusers=[]
        for i in slurs:
            if i in message.content.lower():
                print(str(message.author) + " (" + str(message.author.id) + ") used a slur. their message was: " + str(message.content))
                bannedusers.append(message.author.id)
                print(bannedusers)
                break
        else:
            if '!twit' in message.content[0:5].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to say: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.update_status(message.content[6:])
                    print(str(message.content)+' -'+str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```"+str(message.author)+" tweeted: "+message.content[6:]+"```")
                    await message.delete()
            elif '!twituwu' in message.content[0:8].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to say: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.update_status(uwuify(message.content[9:]))
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " tweeted: " + message.content[9:] + "```")
                    await message.delete()
            elif '!follow' in message.content[0:7].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to delete tweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.create_friendship(message.content[8:])
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " followed: " + message.content[8:] + "```")
                    await message.delete()
            elif '!unfollow' in message.content[0:9].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to delete tweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.destroy_friendship(message.content[10:])
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " unfollowed: " + message.content[10:] + "```")
                    await message.delete()
            elif '!like' in message.content[0:5].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to delete tweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.create_favorite(message.content[message.content.find('status/')+7:message.content.find('?s=')])
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " liked: " + message.content[6:] + "```")
                    await message.delete()
            elif '!unlike' in message.content[0:7].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to delete tweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.destroy_favorite(message.content[message.content.find('status/')+7:message.content.find('?s=')])
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " unliked: " + message.content[8:] + "```")
                    await message.delete()
            elif '!name' in message.content[0:5].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to change the display name: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.update_profile(message.content[6:])
                    print(str(message.content) + ' -' + str(message.author)+" ("+str(message.author.id)+")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " updated the display name to: " + message.content[6:] + "```")
                    await message.delete()
            elif '!bio' in message.content[0:4].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to change the bio: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.update_profile(description=message.content[5:])
                    print(str(message.content) + ' -' + str(message.author) + " (" + str(message.author.id) + ")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " updated the bio to: " + message.content[5:] + "```")
                    await message.delete()
            elif '!retweet' in message.content[0:8].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to retweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.retweet(message.content[message.content.find('status/')+7:message.content.find('?s=')])
                    print(str(message.content) + ' -' + str(message.author) + " (" + str(message.author.id) + ")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " retweeted: " + message.content[9:] + "```")
                    await message.delete()
            elif '!unretweet' in message.content[0:10].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to unretweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.unretweet(message.content[message.content.find('status/')+7:message.content.find('?s=')])
                    print(str(message.content) + ' -' + str(message.author) + " (" + str(message.author.id) + ")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " unretweeted: " + message.content[11:] + "```")
                    await message.delete()
            elif '!deltwit' in message.content[0:8].lower():
                for i in bannedusers:
                    if message.author.id == i:
                        print('banned user ' + str(message.author) + '(' + str(message.author.id) + ') tried to delete tweet: ' + str(message.content) + 'but was blocked from doing do')
                        break
                else:
                    api.destroy_status(message.content[message.content.find('status/')+7:message.content.find('?s=')])
                    print(str(message.content) + ' -' + str(message.author) + " (" + str(message.author.id) + ")")
                    time.sleep(1)
                    await message.channel.send("```" + str(message.author) + " deleted tweet: " + message.content[9:] + "```")
                    await message.delete()

client = MyClient()

client.run()
bot.run()
