# MK8DX Time Trials & leaderboard discord bot
the discord bot made for Silent Lightning team discord server

---
> **Warning**
>
> #### 2023-11-10 Lounge command is not supported
> #### 2023-11-10 General, Leaderboard, TTupdate, context is supported

### Apps commands for updating people's Time Trials
![image](https://cdn.discordapp.com/attachments/1172493621732327495/1172495134395474020/updating.gif?ex=6560862f&is=654e112f&hm=6ba1a9b10920fa311a1ab44a18d794e0e8c7b1d74dac400931c0205edddb7a2a&)

### Show track's leaderboard 
![image](https://cdn.discordapp.com/attachments/1172493621732327495/1172495675930447903/show_track.gif?ex=656086b1&is=654e11b1&hm=39670465510eacec7b523fb60a4a7899052a968c397224e4e1baccb867f9cc98&)

#setup
## Critical prerequisites to install
* run ```pip3 install -r requirements.txt```
**make `secret.py` for `discord token`**
* Recommended python version `3.10` only because `mk8dx` api
## Step 1: Create Cred.json
1. for project folder you must create `creds.json` for your own googlesheet to sync with bot
2. go to `https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com` to enable google sheet api and get credential file
3. `https://www.youtube.com/shorts/BBgrgA96n-Q` you follow this video and you will get creds file
## Step 2: add player infomation data
1. go to file > make a copy `https://docs.google.com/spreadsheets/d/1Fkv82LtjbdIHnl22ZEFZanG8iSW-QE_K4FxpxMkZkD0/edit#gid=0` and rename for your own sheet files
2. go to `player` tab inside googlesheet and add your own player in here and after you done make sure you sort a-z
![image](https://cdn.discordapp.com/attachments/1172493621732327495/1172502188279472218/player_tab.PNG?ex=65608cc1&is=654e17c1&hm=acca34a9edba8a27e5542bbbbb37931eebeb63509282c522745942c22d87fa76&)
---
## Commands
* `.show [track abbra]` to show track leaderboard in googlesheet files!
* `/submit` to submitting people's Time Trials (recommended Apps > updating time trials) is better for this command and much easier
* `.tl` to translate any message
* `Apps > Translate ` this command just right click on any massage you want to translate and click on `Apps` tab and click `translate`
* `Apps > Submit TimeTrials` this command just right click on any tt post and click on `Apps` and go to `Submit TimeTrials`
*`.remove [value]` to remove massage
*`player` to display player in your team 
