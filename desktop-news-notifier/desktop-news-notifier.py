import feedparser
import time
from win10toast import ToastNotifier

def Parsefeed():
    f = feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms")
    for newsitem in f['items']:
        print(newsitem['title'])
        # print(newsitem['summary'])
        print('\n')
        #notifier
        notifier=ToastNotifier()
        message=f"{newsitem['title']}"
        notifier.show_toast(title="News Notify",msg=message,duration=7, icon_path=r"icon.ico")
        time.sleep(3)
        
if __name__ == '__main__':
    try:
        Parsefeed()
    except:
        print("Error")