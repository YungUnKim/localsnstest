from flask import Flask
import os
import pusher

app = Flask('apps')
p = pusher.Pusher(
    app_id='86632',
    key='691096b1d647e3dc54f8',
    secret='f63617382cf1b4e0e384'
)

userlist = {}


import controller

