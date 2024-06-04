import interactions
import json
from interactions import Intents, Message

with open("config.json", "r") as config_file:
    config_json = json.loads(config_file.read())

    bot_token = config_json['token']
    bot_scope = config_json['scope']
    target_channel = config_json['target_channel']

bot = interactions.Client(token=bot_token, debug_scope=bot_scope, intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT)


@interactions.listen()
async def on_startup():
    print("Bot is ready.")


@interactions.listen()
async def on_message_create(event):
    message: Message = event.message
    channel: interactions.GuildText = message.channel

    if int(channel.id) != target_channel:
        return

    message_word_list = message.content.split(" ")
    previous_channel_message = (await channel.fetch_messages(limit=1, before=message.id))[0]
    split_previous_message = previous_channel_message.content.split(" ")

    try:
        value = int(message_word_list[0])
        last_value = int(split_previous_message[0])
    except ValueError:
        await message.delete()
        return

    if (
            ((value - 1) != last_value) or
            (message.author.id == previous_channel_message.author.id)
    ):
        await message.delete()

bot.start()
