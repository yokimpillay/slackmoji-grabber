# slackmoji-grabber
A simple Python script to download all emojis from the Slackmoji website (or any url for that matter).

## How to use

Make sure you have the following installed:
- Python 3 (I created & used this script on 3.7.0)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (Python Package for parsing and pulling data out of HTML/XML documents)

1. Clone the repo
```bash 
git clone https://github.com/yokimpillay/slackmoji-grabber.git
```

2. Open up your terminal and navigate to the Python script
```bash
cd slackmoji-grabber
```

3. Install the packages using [pipenv](https://github.com/pypa/pipenv/). Pipenv will take care of environment isolation with virtualenv and installing the required packages.
```bash
pipenv install
```

4. Grab Them all

4.1. Activate the virtual enviroment and watch the numbers fly!
```bash
pipenv shell
slackmoji-grabber.py https://slackmojis.com/
```

4.2. Run the script using pipenv
```bash
pipenv run grab_emojis
```

5. The files will be downloaded to a folder called 'slackmojis' created where the script is located.

If you're using this to get all the emojis from Slackmoji, I suggest using Neutral Face Emoji Tools to upload all of them to your Slack workspace. You can find the extension [here](https://chrome.google.com/webstore/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej?hl=en) 

I'm open to suggestions & contributions on how to make this better to use!
