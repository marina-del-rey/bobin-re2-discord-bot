# Re2 Discord Bot - Bobin Bot
My friend Bonin asked me to make him a Discord bot which uses Google's RE2 regular expressions library in order to check for banned phrases in text channels, as well as delete those messages. It allows admins to add and delete expressions, which are stored in a csv file. 

## Commands
- **?list** lists expressions
- **?addexp [args]** used to add expressions to csv file
- **?addexp [args]** used to remove expressions from csv file

## Setting it up

In order to get the bot running, make sure to first install the required Python packages by typing:
```
pip install -r requirements.txt
```

You will also need to download the [RE2 library](https://github.com/google/re2/wiki/Install), as well as its Python wrapper, [pyre2](https://github.com/axiak/pyre2#id3). For both, you will need a Unix shell. If you're using Windows, consider using the Windows Subsystems for Linux.
  
  
## To-do list
- Add an editexp command so users can edit expressions
- Fix remove by index success output

