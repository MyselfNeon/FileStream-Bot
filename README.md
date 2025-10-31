<h2 align="center"><i>FileStream-Bot</i></h1>
<p align="center">
  <a href="https://github.com/MyselfNeon/FileStream-Bot">
    <img src="https://files.catbox.moe/6x59s2.jpg" alt="Cover Image" width="550">
  </a>
</p>  
  <p align="center">
   </strong></a>
    <br><b>
    <a href="https://github.com/MyselfNeon/FileStream-Bot/issues"><i>Report a Bug or Request Feature</i></a></b>
  </p>

#### *About ➠*

<p align="center">
    <a href="https://github.com/MyselfNeon/FileStream-Bot">
        <img src="https://files.catbox.moe/rayjpl.png" height="100" width="100" alt="FileStreamBot Logo">
    </a>
</p>
<p align='center'>
  <i>This Bot instantly Generates Streaming Links for Telegram Files no need to wait for the Download to Finish. It also offers convenient File Storage for easy Access anytime.</i>
</p>


#### *How To Deploy ➠*

<details><summary><b><i>Deploy on Multiple Servers</i></summary></b></summary>
<br>
<details>
  <summary><b><i>Deploy on Heroku (Paid)</i></b></summary>

- Fork This Repo
- Click on Deploy Easily
- Press the below Button to Fast Deploy on Heroku


   [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- Go to <a href="#mandatory-vars">variables tab</a> for more info on Setting up Environmental Variables. </details>

<details>
  <summary><b><i>Deploy Using Docker</i></b></summary>
<br>
* Clone the Repository:
```sh
git clone https://github.com/myselfneon/FileStream-Bot
cd FileStreamBot
```
* Build own Docker Umage:
```sh
docker build -t file-stream .
```

* Create ENV and Start Container:
```sh
docker run -d --restart unless-stopped --name fsb \
-v /PATH/TO/.env:/app/.env \
-p 8000:8000 \
file-stream
```
- If you Need to Change the Variables in .env File after your Bot was Already Started, all you need to do is Restart the container for the Bot Settings to get Updated:
```sh
docker restart fsb
```

  </details>

<details>
  <summary><b><i>Deploy Locally</i></b></summary>
<br>

```sh
git clone https://github.com/myselfneon/FileStream-Bot
cd FileStreamBot
python3 -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m FileStream
```

- To stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

- If you want to run this bot 24/7 on the VPS, follow these steps.
```sh
sudo apt install tmux -y
tmux
python3 -m FileStream
```
- now you can close the VPS and the bot will run on it.

  </details>

</details>

#### *Config Variables ➠*

<details><summary><b><i>ENV Variables</i></summary></b></summary>

#### *Mandatory Variables ➠*

* [`API_ID`]: ***From [My Telegram](https://my.telegram.org).***
* [`API_HASH`]: ***From [My Telegram](https://my.telegram.org).***
* [`OWNER_ID`]: ***Your Telegram User ID. Get From [@MissRose_Bot](https://t.me/MissRose_Bot)***
* [`BOT_TOKEN`]: ***Telegram API Bot Token, Get it from [@BotFather](https://t.me/BotFather).***
* [`FLOG_CHANNEL`]: ***ID of the Channel where Bot will Store all Files from Users `int`***
* [`ULOG_CHANNEL`]: ***ID of the Channel where Bot will send Logs of New Users`int`***
* [`BOT_WORKERS`]: ***Number of updates Bot should process from Telegram at once, by Default to 10 Updates. `int`***
* [`DATABASE_URL`]: ***[MongoDB URI](https://cloud.mongodb.com) for Saving User Data and Files List created by User. `str`***
* [`FQDN`]: ***A Fully Qualified Domain Name if present without https. Defaults `BIND_ADDRESS`.***

#### 🗼 *MultiClient Variables* :
* [`MULTI_TOKEN1`]: ***Add your 1st Bot Token or Session Strings.***
* [`MULTI_TOKEN2`]: ***Add your 2nd Bot Token or Session Strings.***

#### 🪐 *Optional Variables* :

* [`UPDATES_CHANNEL`]: ***Channel Username without `@`. `str`***
* [`FORCE_SUB_ID`]: ***Force Sub Channel ID, if you want to use Force Sub with `-100` `int`***
* [`FORCE_SUB`]: ***Set to True, so every User have to Join Update Channel to use the Bot. `bool`***
* [`AUTH_USERS`]: ***Authorized User IDs, Separated by Space. `int`***
* [`SLEEP_THRESHOLD`]: ***Set Global Flood wait threshold, Auto-Retry Requests under 60s. `int`***
* [`SESSION_NAME`]: ***Name for the Database Created on [MongoDB](https://cloud.mongodb.com). Defaults `FileStream`. `str`***
* [`FILE_PIC`]: ***To set Image at `/files` Command. Defaults to Pre-Set image. `str`***
* [`START_PIC`]: ***To set Image at `/start` Command. Defaults to Pre-Set image. `str`***
* [`VERIFY_PIC`]: ***To set Image at Force Sub Verification. Defaults to Pre-Set image. `str`***
* [`WORKERS`]: ***Number of Max Workers for handling Incoming Updates. Defaults to `6`. `int`***
* [`PORT`]: ***The Port that you want your Webapp to be listened to. Defaults to `8080`. `int`***
* [`BIND_ADDRESS`]: ***Your Server Bind Address. Defauls to `0.0.0.0`. `int`***
* [`MODE`]: ***Set to `secondary` if you Only want to use the Server for serving Files. `str`***
* [`NO_PORT`]: ***Set (`True`/`False`) PORT to 80 or 443 Hide Port Display; Ignore if on Heroku. Defaults to `False`.***
* [`HAS_SSL`]: ***(`True` or `False`) If you want the Generated Links in https format. Default is `False`.***

</details>
 
#### *Bot Commands ➠* 

<details><summary><b><i>Bot Commands</i></b></summary>
  
```
start - Check if Bot is Alive
help - Get Help Message
about - Check About the Bot
files - Get All Files List of User
del - Delete Files from DB with File ID [ADMIN]
ban - Ban any Channel or User from using Bot [ADMIN]
unban - Unban any Channel or User from using Bot [ADMIN]
status - To Get Bot Status and Total Users [ADMIN]
broadcast - To Broadcast any Message to all Users of Bot [ADMIN]
```
<b><i>⪼ Copy all Commands and paste it in <a href='https://t.me/botfather'>BotFather</a> to apply Commands.

</details>

#### *Channel Support ➠*

***The Bot also Supports Telegram Channels, Just add it as an Admin. Whenever a new File is posted in the Channel, the Bot will Automatically edit the Message and add a “Get Download Link” Button.***

#### Contact Developer 👨‍💻

[![Contact Developer](https://img.shields.io/badge/Contact-Developer-blue?logo=telegram)](https://t.me/MyselfNeon)    
[![Telegram Channel](https://img.shields.io/badge/Telegram-Main%20Channel-blue?logo=telegram)](https://t.me/neonfiles)  
Join My <a href='https://t.me/neonfiles'>Update Channel</a> For More Update Regarding Repo.

</details>

#### *Thanks To ➠* ❤️
 - <b>Thanks To [Neon An](https://t.me/MyselfNeon) To Modify And Add Amazing Features
 - Thanks To Everyone who have Contributed In This Repo ❤️</b>

---
<h4 align="center">➠ © <a href="https://myselfneon.github.io/neon/" target="_blank" rel="noopener noreferrer">MyselfNeon 🍟</a></h4>
