from datetime import datetime, timedelta


def getDays(time):
    time = str(time)
    length = len(time)
    if(time[length-2] != "1"):
        if(time[length-1] == "1"): return "день"
        if(time[length-1] in ["2", "3", "4"]): return "дня"
    if(length == 1):
        if(time[length-1] == "1"): return "день"
        if(time[length-1] in ["2", "3", "4"]): return "дня"
    return "дней"


def getHours(time):
    time = str(time)
    length = len(time)
    if(time[length-2] != "1"):
        if(time[length-1] == "1"): return "час"
        if(time[length-1] in ["2", "3", "4"]): return "часа"
    if(length == 1):
        if(time[length-1] == "1"): return "час"
        if(time[length-1] in ["2", "3", "4"]): return "часа"
    return "часов"

def getMinutes(time):
    time = str(time)
    length = len(time)
    if(time[length-2] != "1"):
        if(time[length-1] == "1"): return "минуту"
        if(time[length-1] in ["2", "3", "4"]): return "минуты"
    if(length == 1):
        if(time[length-1] == "1"): return "минуту"
        if(time[length-1] in ["2", "3", "4"]): return "минуты"
    return "минут"

def getSeconds(time):
    time = str(time)
    length = len(time)
    if(time[length-2] != "1"):
        if(time[length-1] == "1"): return "секунду"
        if(time[length-1] in ["2", "3", "4"]): return "секунды"
    if(length == 1):
        if(time[length-1] == "1"): return "секунду"
        if(time[length-1] in ["2", "3", "4"]): return "секунды"
    return "секунд"



def getTime(time):
    now = datetime.now()
    time = now - time
    m, s = divmod(time.seconds, 60)
    h, m = divmod(m, 60)
    hours = getHours(h)
    days = getDays(time.days)
    minutes = getMinutes(m)
    seconds = getSeconds(s)
    return ("%d %s %d %s %02d %s %02d %s" % (time.days, days, h, hours, m, minutes, s, seconds))
