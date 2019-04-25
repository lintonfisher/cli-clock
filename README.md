# simple-shell-clock

## Description

The Simple Shell Clock is intended to be a simple and reliable digital clock for your Linux shell. The idea to create such a script came after trying to find a simple shell script or python script to do the same thing online. I couldn't find one that I actually liked, and that was easy to customise, so I created my own.

## Requirements

### [PyFiglet](https://pypi.org/project/pyfiglet/)

```bash
$ pip3 instal pyfiglet
```

## Usage

```bash
$ python3.7 ~/Downloads/simple-shell-clock/main.py
```

### Customisation

The variables at the start of the script can all be changed to modify the look and feel of the clock.

| Variable            | Default         | Description                                              | Useful Link(s)                                       |
| ------------------- | --------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| font_name           | ```python       | Changes the Figlet font which is rendered                | [Figlet Font DB](http://www.figlet.org/fontdb.cgi)   |
|                     | '3x5'           |                                                          |                                                      |
|                     | ```             |                                                          |                                                      |
| padding             | ```python       | Applies padding to the top/right/bottom/left of the text |                                                      |
|                     | [0, 0, 0, 0]    |                                                          |                                                      |
|                     | ```             |                                                          |                                                      |
| custom_char_replace | ```python       | Used to replace character(s) with another character(s)   | [Unicode Character Table](https://unicode-table.com) |
|                     | {'#': '\u2588'} |                                                          |                                                      |
|                     | ```             |                                                          |                                                      |
| time_format         | ```python       | Set the format of the time to be displayed               | [Time Formatting Parameters](http://strftime.org/)   |
|                     | '%H:%M:%S'      |                                                          |                                                      |
|                     | ```             |                                                          |                                                      |

## Planned Features

- Font customisation (figlet).
- Colour customisation.
- Padding & general tidiness.
