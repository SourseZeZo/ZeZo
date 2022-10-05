from os import listdir, mkdir
from pyrogram import Client
from ZeZo import config
from ZeZo.MusicUtilities.tgcallsrun.queues import (clear, get, is_empty, put, task_done)
from ZeZo.MusicUtilities.tgcallsrun.downloader import download
from ZeZo.MusicUtilities.tgcallsrun.convert import convert
from ZeZo.MusicUtilities.tgcallsrun.music import run
from ZeZo.MusicUtilities.tgcallsrun.music import smexy as ASS_ACC
smexy = 1
