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
Description=Telegram Bot
After=multi-user.target
 
[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/telegram_bot/messages.py <TOKEN> <CHAT_ID>
Restart=on-abort
 
[Install]
WantedBy=multi-user.target

sudo chmod 644 /lib/systemd/system/telegram_bot.service
chmod +x /home/pi/telegram_bot/messages.py
sudo systemctl daemon-reload
sudo systemctl enable telegram_bot.service
sudo systemctl start telegram_bot.service


### Check status
sudo systemctl status telegram_bot.service
 
### Start service
sudo systemctl start telegram_bot.service
 
### Stop service
sudo systemctl stop telegram_bot.service
 
### Check service's log
sudo journalctl -f -u telegram_bot.service
