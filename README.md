# Counting Bot

## What is it?
This bot a is a simple bot coded in Python that will ensure that a counting channel is in proper order. It is highly preferred that you read the security section if you are using the code.

## How do I use it?
1. Clone or download the source code
2. CD into the source code directory.
3. Create a `config.json` file. Look at the `Config Example` section for the format.
4. Run `pip install -r requirements.txt`
5. Run `python main.py` or `python3 main.py` if you're running Linux.

## Config Example
Your config file should look like the following:
```json
{
  "token": "Your bot's token",
  "scope": "The server that your bot is in.",
  "target_channel": [The ID of the counting channel. Do not wrap it in quotes.]
}
```
Ensure that you replace **all** of the values with their appropriate value.

Here is an example:
```json
{
  "token": "token",
  "scope": "800399299397419078",
  "target_channel": 800401182392713267
}
```
If the config file does not follow the above format, then you will run into issues. Also, it should be noted that "token" should be the actual token of your bot and not just the word "token."

## Security
Due to the nature of the GNU public license, you will be required to make your fork of this bot's code open-source and available to the public. However, it should be noted that you should **never** include
your `config.json` file in the repository. Doing so poses a major security risk for both you and your Discord server. 
