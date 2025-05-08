import time
import os
import json
from requests_oauthlib import OAuth1Session

consumer_key = ''
consumer_secret = ''

joke = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
"Why did the programmer quit his job? He didn’t get arrays!",
"I told my computer I needed a break, and now it won’t stop sending me beach wallpapers.",
"I would tell you a joke about UDP, but you might not get it."
"My computer beat me at chess, but it was no match for me at kickboxing."
"Why do Java developers wear glasses? Because they don’t see sharp!"
"How do you comfort a JavaScript bug? You console it."
"I’m on a whiskey diet. I’ve lost three days already!"
"What’s a computer’s favorite beat? An algorithm!"
"Why was the computer cold? It left its Windows open!"
"I wanted to become a programmer, but I couldn’t find the right class."
"Why did the computer go to therapy? It had too many bytes of data!"
"I told my laptop a joke, but it just wouldn’t respond. Guess it had too many tabs open!"
"Why did the web developer walk out of the meeting? Too many cookies and not enough cache!"
"I have a joke about programming, but it only works on my machine."
]