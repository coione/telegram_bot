# telegram_bot

## Install
Raspberry Pi 3 - Telegram Bot
command /pic Take a pic

$ pip install telepot

$ pip install telepot --upgrade  # UPGRADE


## Run bot as service

cd /lib/systemd/system/

sudo nano telegram_bot.service

[Unit]
Description=Telegram bot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/telegram_bot/app.py <TOKEN> <CHAT_ID>
Restart=always

[Install]
WantedBy=multi-user.target

sudo chmod 644 /lib/systemd/system/telegram_bot.service

chmod +x /home/pi/telegram_bot/messages.py

sudo systemctl daemon-reload

sudo systemctl enable telegram_bot.service

sudo systemctl start telegram_bot.service

Example service systemd file (telegram_bot.service.example) is in root folder

### Check status
sudo systemctl status telegram_bot.service
 
### Start service
sudo systemctl start telegram_bot.service
 
### Stop service
sudo systemctl stop telegram_bot.service
 
### Check service's log
sudo journalctl -f -u telegram_bot.service
