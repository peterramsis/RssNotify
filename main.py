from win10toast import ToastNotifier
import feedparser
import time
toaster = ToastNotifier()


def getNews():
    url = "https://www.youm7.com/rss/SectionRss?SectionID=203" #url rss
    feed = feedparser.parse("https://www.youm7.com/rss/SectionRss?SectionID=203") #Get all feed from rss

    for item in feed["entries"]:
        toaster.show_toast("اليوم السابع",item["title"],duration=100)

    while toaster.notification_active():
        time.sleep(1000)


if __name__ == '__main__':
    getNews()


