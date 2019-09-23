#!/usr/bin/liquidsoap

set("log.file.path", "/var/log/liquidsoap/basic-radio.log")

music = mksafe(playlist(mode='randomize', reload=10, reload_mode="rounds", "~/radio/music/mp3"))
jingles = mksafe(playlist(mode='normal', reload=100, "~/radio/music/jingles"))

radio = random(weights = [1, 7], [jingles, music])

output.icecast(%mp3,
host = "localhost",
port = 8000,
url = "lo-fi-radio.herokuapp.com",
password = "hackme",
mount = "lo-fi-radio",
description = "",
genre = "lo-fi",
radio)
