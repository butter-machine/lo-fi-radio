Web Radio
===

This is a simple example of web radio based in [Django](https://www.djangoproject.com/), [Icecast](http://icecast.org/) and [Liquidsoap](https://www.liquidsoap.info/).

All scripts will be represented for Debian-based distributive, but you can modificate it for your server OS.

Deploying web app.
===

I prefer [Heroku](https:./dashboard.heroku.com/) so there is a complete
script *./static/scripts/heroku_deploy.sh* to deploy web-app to Heroku via GIT.

Configuring stream server
===

I choose AWS EC2 cause of its interactive command prompt. Copy folder *./server_setup* to your server at home directory.

Configuring Liquidsoap
---

Now you should configure your streaming schedule and other things. Just edit *./radio.liq*. [This is a good article about .liq files](http://u.delta9.pl/k/liquidsoap/quick_start.html). In my case there are jingles and music, wich will be played at 1:7 proportion. You can add few other moutnpoints with ogg source, for examle. You can find liquidsoap logs at */var/log/liquidsoap/basic-radio.log* (default path).

Configuring Icecast and installing all packages
---

If you are first time running server update repositories if it need. Run *./server_setup/server_setup.sh*, and chose "Yes" and configure icecast (leave *localhost* for this examle). If nothing goes wrong you can visit [http//your_server_ip/8000](http//your_server_ip/8000) (if you set another port at *icecast.xml* just replace 8000 to it) and see icecast server. Also you can login as admin.

Adding media
---

You can copy some music and jingles to */usr/share/liquidsoap/radio/music/mp3* and */usr/share/liquidsoap/radio/music/jingles* respectively (or other dirs you set in .liq file).
***
That*s it! Now you can enjoy your own web radio!

@Pavel Antsypovich, 2019