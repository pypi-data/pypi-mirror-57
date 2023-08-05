# BenBot
Python wrapper for BenBot.

[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/AsyncBenBot.svg)](https://pypi.org/project/AsyncBenBot/)
[![BenBot Version: 0.0.3](https://img.shields.io/pypi/v/AsyncBenBot.svg)](https://pypi.org/project/AsyncBenBot/)

## Installing:
### Synchronous:
Windows: ``py -3 -m pip install BenBot``<br>
Linux/macOS: ``python3 -m pip install BenBot``

### Asynchronous:
Windows: ``py -3 -m pip install BenBotAsync``<br>
Linux/macOS: ``python3 -m pip install BenBotAsync``

## Example:
```
import BenBotAsync

async def get_ghoul_trooper():
    BenSearch = await BenBotAsync.get_cosmetic('Ghoul Trooper', parameter='displayName', sorter='type', filter='Outfit')
    print(BenSearch.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_ghoul_trooper())
loop.close()
```

fortnite.py example:

```
import fortnitepy
import BenBotAsync

client = fortnitepy.Client(
    email='example@email.com',
    password='password123'
)

@client.event
async def event_friend_message(message):
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!skin':
        skinId = await BenBotAsync.get_cosmetic(content, parameter='displayName', sorter='type', filter='Outfit')
        await client.user.party.me.set_outfit(asset=skinId)

client.run()
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

The list of functions is on the Wiki.