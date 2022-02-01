#os image layers
FROM archlinux

RUN pacman -Syu python python-pip git --noconfirm
RUN git clone https://github.com/LordOfNightmares/My-discord-bot bot
WORKDIR bot
RUN python -m pip install -r requirements.txt --no-cache-dir
CMD ["python", "bot.py"]

