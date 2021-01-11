## Translation
translation simply makes a request to the [deepl api](www.deepl.de).
Thus all credit goes to deepl.


### Default settings
By default the input is translated from auto detect to English. Feel free to
change the default in `translate.py`. 

### Setting up, to use from everywhere.
It as annoying to enter python each time you want to call the code. To omit this
enter: `chmod +x translate.py` while in the same directory as translate.py.

Next you may want to add "translate.py" to your Path variable. 

For this: 

either move "translate.py" to a directory, which is already in the
path variable. You can do this be executing:
`sudo make install`

Or add the translation folder to your path, by entering: 
`export PATH=$PATH:</path/to/file>` in the command line or adding it to your ~/.profile

### Basic usage

```
> translate.py "Was würde Hegel tun" EN   
['What would Hegel do', 'What Would Hegel Do']

> translate.py "How are you?"       
['Wie geht es Ihnen?', 'Wie geht es dir?', "Wie geht's Ihnen?", "Wie geht's?"]
```
