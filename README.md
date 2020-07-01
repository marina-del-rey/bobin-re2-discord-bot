# Re2 Discord Bot - Bobin Bot
My friend Bonin asked me to make him a Discord bot which uses Google's RE2 engine in order to check for banned phrases in text channels, as well as delete those messages.

## Setting it up

In order to get the bot running, make sure to first install the required Python packages by typing:
```
pip install -r requirements.txt
```

You will also need to download the re2 engine, as well as the python wrapper for it, pyre2. For this, you will need a Unix shell. If you're using Windows, consider using the Windows Subsystems for Linux.

### RE2
The re2 engine is pretty straight forward to install, you can find the instructions on their [git repository wiki](https://github.com/google/re2/wiki/Install).

### PyRE2
