# PyQT Sampler

## About
This is my first foray into PyQt6 Initial set up code comes from [PyQt6 Tutorial Series | Python GUI Programming](https://coderslegacy.com/python/pyqt6-create-basic-window/).

My goal is to see if I can do what I've had such a hard time doing with other Py GUI frameworks. Some of the items I want to test out are:
* ease of use (some take forever to make seemingly simple modifications)
* Can I change the fonts? 
* Can I add Google Fonts?
* How easy is it to display images?

## Getting Started
These instructions are focused on using [poetry](https://python-poetry.org/) for project management and [VSCode](https://code.visualstudio.com/) for my IDE.

I typically use GitBash to get started (for some odd reason), but you can use whatever CLI (Terminal, Command Prompt, PowerShell, or even the VSCode Terminal) and project manager (poetry, pip, pipenv) you like.

### From Scratch
I prefer to run these commands in Git Bach
1. Use poetry to create your project `poetry new project-name`
2. CD into the project: `cd project-name`
3. Add your dependencies:
`poetry add pyqt6`
`poetry add requests` (if you want to make API calls)

### From repo clone
In Git Bash:
1. `git clone <URL>`
2. `cd project_folder`
3. Spawn the virtual environment shell: `poetry shell`

### In VSCode 
Select Python interpreter using the link to the poetry shell in VS
Code:

 * View > Command Palette (or just `Ctrl` + `Shift` + `P`)
 * Type: `Python: Select Interpreter`
 * Choose the link from the terminal that you saw when running
   `poetry shell`
   - If you do not see the path
   - copy the path from the terminal
   - Click the `+` sign
   - Paste the path




## Credits/Shout outs!
Thanks so much [TeachingCS](https://www.youtube.com/@teachingcs)'s YouTube video for the video [PyQt6 Tutorial - Making Your First GUI #04 - Adding Images](https://youtu.be/-aYqBBnSeuc)
Bookshelf and Search icons from [Maria & Guillem](https://icon-icons.com/pack/Miscellany-Web-icons/692)

Python Logo Icon by [icon 54]"(https://iconscout.com/contributors/icon-54)