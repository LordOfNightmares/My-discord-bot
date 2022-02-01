#os image layers
FROM archlinux as base

RUN pacman -Syu python python-pip git --noconfirm

#bot image layers
FROM base
WORKDIR /bot/

RUN git clone --recursive https://github.com/LordOfNightmares/My-discord-bot.git bot
RUN python -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT start.sh

