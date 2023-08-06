# Colord


## Executive summary

- Python package which allows you to print colored text & colored words.
- You need to setup lists with colored words & all words in lists will be printed in color of that list.

## Installation

- pip3 install colord


## Usage

- in printc function can be used argumets: delay, skipline.
- delay : delay between next letter will be printed
- skipline = True : will skip line after text is printed

## Example

```
import colord

colord.setlist.magenta(['test'])
colord.setlist.green(['test2','test3'])
colord.setlist.red(['test4'])

colord.printc('testtest2test4test3')

colord.printc('testtest2test4test3',delay=0.03)

colord.printc('testtest2test4test3',delay=0.03,skipline=True)
```
