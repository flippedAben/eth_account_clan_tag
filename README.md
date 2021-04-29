# Ethereum Clan Tagged Account Generator

Imagine being the absolute unit whose Ethereum account address is:

> 36f1ec004e9cb05bd12fa23a079786261ae5**beef**

Instead of mining to put transactions on the blockchain and do useful work,
let's mine clan tags. This is completely for fun and an absolute waste of
resources. While learning about Ethereum, I happened to think about clan tags
in games. Clan tags are the dumbest things in this world.

This program will generate a seed, private key, public key, and account address
for you, such that the account address ends in a "clan tag".

Clan tags are only hex. Examples:

- fade
- dead
- beef
- 0000

# Setup

Tested on Linux only. I use Arch btw. Also vegan. Crossfit, too. (It's a joke.
I'm none of these things.)

```bash
python -m venv env
source env/bin/activate
pip install pycryptodome coincurve
python main.py <a tag>
```

_Note: tags of size > 4 might take a while_

# Example output

```
Seed       : <removed>
Private key: <removed>
Public key : b338ecaf6c5a13fc436345dfbde58a29a0d05a74a6f89a89b4061c8f7840617fd705720188e41c32c019bb962c6fb2b11330314aa8351a3975a0daf87982841a
Address    : 36f1ec004e9cb05bd12fa23a079786261ae5beef
Never share the seed or private key with anyone!
Never share the seed or private key with anyone!
Never share the seed or private key with anyone!
```

# Gratitude

Heavy thanks to these resources:

- [Generating Ethereum addresses in Python](https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/)
- [Hexspeak](https://en.wikipedia.org/wiki/Hexspeak)
