import tweepy, time, sys
from tkinter import *
import tkinter.messagebox

def tweet_data():
   input = tweet_text.get()
   api.update_status(status= input)
   tweet_text.delete(0, END)

CONSUMER_KEY = "N7e5kWDuVUZUIQvECbWLxMs4l"
CONSUMER_SECRET = "LGXwsNRAAZADnmXa1aq9fZu8AheOZCzC3jLqw3BzR83y7LVSBn"
ACCESS_KEY = "3162862942-ZeaQlEbeiDieXoJr7pdQr4BSLqXH2ZwGDncsWgh"
ACCESS_SECRET = "aN0lX8gEsaSAKGETBrem2ybdbM4BGEoAj1A1gIyIjwxjV"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


app = Tk()
app.title("Twitter")

app.geometry("300x300+100+100")
app.configure(background='cyan' )
Label(app, text = "Whatcha Thinkin?", background='cyan').pack()
tweet_text = Entry(app,  width = 150, background='cyan')
tweet_text.pack()

Button (app, text = "Tweet!",
             width = 20, command = tweet_data).pack()

app.mainloop()