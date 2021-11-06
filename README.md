# What have I done?
Let you review things you have done on your computer.

## Why?
Computers are getting so addictive that we all have been entrained at some point. Destop recording let us see how our precious time has been spent. However, normal screen record methods are sometimes heavy on resources, and we can't afford to lose 1 hour reviewing things from the previous one - too unefficient, and hence this module.

## Examples

https://user-images.githubusercontent.com/87116762/140607481-9c0874ac-ef07-4d58-9ff2-7915d4b56e09.mp4

<br>

There is no sound (obviously), and the FPS is terrible. On the other hand, it is very light on CPU, memory and disk usage. The video quality is high enough to understand what was going on, thou.
<br>

## Installation
You can install from PyPi:
```bash
pip install whid
```

Don't forget to check the installation:
```bash
python -m whid -h
```
<br>

### About Linux...
You need to install `scrot` first for screenshot functions 
```bash
sudo apt install scrot
```

`scrot` is [acknowledged for not working on Wayland](https://githubmemory.com/repo/asweigart/pyautogui/issues/556). So please check your `scrot` installation beforehand:
```bash
cd /tmp
scrot test.png
firefox test.png
```

If you see a black screen, it's time to uninstall the packages.
<br>

## Usage
By default, the program records at 0.2 fps (5 secs/ 1 screenshot), for a duration of 1 hour (3600 seconds). To run default script:
```bash
python -m whid
```

For more optional arguments, check the `help` command.
```bash
python -m whid --help
```

## Development
- The module's supposed to work cross-platform, but due to the lack of access to Mac devices, I haven't tested it on OSX/MacOS. It would be deeply appreciated if you can test it on your Mac and report back issues (if any).
- If you have a fix for `scrot` problems on Wayland, please open a pull request.
- Every other issue, pull request or suggestions are also highly valuable.
