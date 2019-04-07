from win10toast import ToastNotifier
import reddit
import json
import threading


class Notifier:
    def __init__(self):
        with open('setting.json','r') as s:
            setting = json.load(s)
        self.red = reddit.Reddit(client_id = setting['reddit_client_id'], client_secret = setting['reddit_client_secret'], user_agent = setting['reddit_user_agent'], username = setting['reddit_username'], password = setting['reddit_password'])

        self.toaster = ToastNotifier()

        self.last_msg = {}
        self.subs = setting['reddit_sub_tracking']
        for sub in self.subs:
            self.last_msg[sub] = ''



    def reddit_notification(self):
        threading.Timer(300.0, self.reddit_notification).start()
        for sub in self.subs:
            try:
                new_story = self.red.getTopStory(sub=sub, lim=1)
                if self.last_msg[sub] != new_story:
                    self.last_msg[sub] = new_story
                    self.toaster.show_toast("Reddit", new_story, icon_path='icons/reddit.ico', duration=20)
            except:
                print('Error: Reddit notification')

noti = Notifier()
noti.reddit_notification()

