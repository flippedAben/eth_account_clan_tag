# Ethereum Clan-tag-based Account Generator

Instead of mining to put transactions on the blockchain, let's mine a clan tag.

This is completely for fun and an absolute waste of resources. While learning
about Ethereum, I happened to think about clan tags in games. Clan tags are the
dumbest things in this world, but YOLO.

This program will generate a seed, private key, public key, and account address
for you, such that the account address ends in a "clan tag".

Clan tags are only hex. Examples:

- fade
- dead
- beef

# Setup

Tested on Linux only. I use Arch btw. Also vegan. Crossfit, too.

```bash
python -m venv env
source env/bin/activate
pip install pycryptodome coincurve
python generate.py
# Type in your desired clan tag!
```

_Note: tags of size > 4 might take a while_

# Gratitude

Heavy thanks to this resource:

- (Generating Ethereum address in Python)[https://www.arthurkoziel.com/generating-ethereum-addresses-in-python/].
