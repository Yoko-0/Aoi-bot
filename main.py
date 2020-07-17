from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api, random, shelve
from random import randint
from datetime import datetime, timedelta
from reloadMusic import reloadMusic


kick_album = []
tie_album = []
kiss_album = []
spank_album = []
hug_album = []
feed_album = []
pout_album = []
night_album = []
morning_album = []
lift_album = []
hi_album = []
hit_album = []
sad_album = []
bite_album = []
put_on_the_knees_album = []
pat_on_the_head_album = []
squeeze_by_cheeks_album = []
heart_album = []
rrrrr_album = []
be_embarrassed_album = []
lick_album = []
press_album = []
take_hand_album = []
cling_to_album = []
chain_album = []
dance_album = []
hickey_album = []
kiss_cheek_album = []
hug_all_album = []


gifs_album = {}
photos_album = {}
audios_album = {}
main_album = ["457240076"]

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

def send_message(peer_id, text, photo):
    vk.method("messages.send", {"peer_id": peer_id, "message": text, "random_id": 0, "attachment": photo})

def get_name(user_id, case):
    full = vk.method("users.get", {"user_ids": user_id, "name_case": case})
    return (full[0]["first_name"] + " " + full[0]["last_name"])

def get_sex(user_id):
    return vk.method("users.get", {"user_ids": user_id, "fields": "sex"})[0]["sex"]

def getIdFromDB(user):
    for key in db.keys():
        if(db[key] == user): return key
    return 0

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



def getPhotos(album_id):
    print(album_id)
    return photos_album[album_id]


def getGifs(name):
    print(name)
    new_gifs = []

    for i in range(gifs_album["count"]):
        id = gifs_album["items"][i]["id"]
        title = gifs_album["items"][i]["title"]
        if(name in title):
            new_gifs.append(str(id))
    return new_gifs


def addNewPhotos(photos):
    global photos_album
    for i in range(len(photos["items"])):
        try:
            photos_album[photos["items"][i]["album_id"]].append(str(photos["items"][i]["id"]))
        except:
            photos_album[photos["items"][i]["album_id"]] = [str(photos["items"][i]["id"])]


def getAllGifs():
    return vk1.method("docs.get", {"owner_id": -195205545, "type": 3})

def getAllPhotos():
    global photos_album
    photos_album = {}
    offset = 0

    photos = vk1.method("photos.getAll", {"owner_id": -195205545, "count": 200, "offset": offset})
    addNewPhotos(photos)

    for i in range(photos["count"] // 200):
        offset += 200
        addNewPhotos(vk1.method("photos.getAll", {"owner_id": -195205545, "count": 200, "offset": offset}))



def sendMessage(text, album, type):
    photos = None
    if(album): photos = type + "-195205545_" + album[randint(0, len(album) - 1)]
    send_message(peer_id, text, photos)
    print("answer = " + text)



def checkBan():
    for key in db_ban.keys():
        if(datetime.now() - db_ban[key] > timedelta(minutes=1)):
            db_ban.pop(key)



def reloadPhotos():
    global kick_album
    global tie_album
    global kiss_album
    global spank_album
    global hug_album
    global feed_album
    global pout_album
    global night_album
    global morning_album
    global lift_album
    global hi_album
    global hit_album
    global sad_album
    global bite_album
    global put_on_the_knees_album
    global pat_on_the_head_album
    global squeeze_by_cheeks_album
    global heart_album
    global rrrrr_album
    global be_embarrassed_album
    global lick_album
    global press_album
    global take_hand_album
    global cling_to_album
    global chain_album
    global hickey_album
    global kiss_cheek_album
    global hug_all_album

    getAllPhotos()
    kick_album = getPhotos(272136375)
    tie_album = getPhotos(272136372)
    kiss_album = getPhotos(272136370)
    spank_album = getPhotos(272136367)
    hug_album = getPhotos(272136362)
    feed_album = getPhotos(272136359)
    pout_album = getPhotos(272136355)
    night_album = getPhotos(272151195)
    morning_album = getPhotos(272151986)
    lift_album = getPhotos(272152171)
    hi_album = getPhotos(272151185)
    hit_album = getPhotos(272154293)
    sad_album = getPhotos(272171414)
    bite_album = getPhotos(272173642)
    put_on_the_knees_album = getPhotos(272178865)
    pat_on_the_head_album = getPhotos(272178874)
    squeeze_by_cheeks_album = getPhotos(272178882)
    heart_album = getPhotos(272178918)
    rrrrr_album = getPhotos(272178943)
    be_embarrassed_album = getPhotos(272178945)
    lick_album = getPhotos(272178947)
    press_album = getPhotos(272178949)
    take_hand_album = getPhotos(272178950)
    cling_to_album = getPhotos(272178975)
    chain_album = getPhotos(272197731)
    hickey_album = getPhotos(272684195)
    kiss_cheek_album = getPhotos(272972761)
    hug_all_album = getPhotos(273013062)



def reloadGifs():
    global dance_album
    global gifs_album

    gifs_album = getAllGifs()
    dance_album = getGifs("dance")



def reloadAll():
    reloadPhotos()
    reloadGifs()
    global audios_album
    audios_album = reloadMusic()
    print("Ready")


db = shelve.open("Databases/users")
db_time = shelve.open("Databases/time")
db_ban = shelve.open("Databases/ban")
db_commands = shelve.open("Databases/commands_list")

try_married = {}
timer = {}

off = 0


vk = vk_api.VkApi(token="927d0c2eb68bc3197ee29a3634b0de4466b1b66ec0cddbc76142138a1e1c8dc83f2b35fb8354e013c3a25")
vk._auth_token()
vk.get_api()


vk1 = vk_api.VkApi(token="beca55e59eeb78065d9c448d195ed79ea32d72e1d5c280be6a0116588df0e544a8eb29196f3b1c3487a79")
vk1._auth_token()
vk1.get_api()


longpoll = VkBotLongPoll(vk, 195205545)

commands = db_commands["commands"]
married_commands = db_commands["married_commands"]
admin_commands = db_commands["admin_commands"]
father_commands = db_commands["father_commands"]
no_commands = db_commands["no_commands"]
music_commands = db_commands["music_commands"]

db_commands.close()

admins = [146389567, 153612096, 502405809, 227542031, 451855119]
father = [146389567]

group_check = 0

reloadAll()

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                    print()
                    print(event.obj)

                    if('action' in event.obj.keys()):
                        if(event.obj['action']['type'] == "chat_invite_user_by_link"):
                            answer = "Привет, @id" + str(event.obj.from_id) + "(" + str(get_name(event.obj.from_id, "nom")) + ") :з\nрада видеть тебя в нашей уютной беседке, надеюсь тебе понравится атмосфера тут и ты останешься с нами🧸🧡"
                            send_message(event.obj.peer_id, answer, None)
                            continue
                        elif(event.obj['action']['type'] == "chat_invite_user"):
                            answer = "Привет, @id" + str(event.obj['action']['member_id']) + "(" + str(get_name(event.obj['action']['member_id'], "nom")) + ") :з\nрада видеть тебя в нашей уютной беседке, надеюсь тебе понравится атмосфера тут и ты останешься с нами🧸🧡"
                            send_message(event.obj.peer_id, answer, None)
                            continue
                        elif(event.obj['action']['type'] == "chat_kick_user"):
                            answer = "Прощай, @id" + str(event.obj['action']['member_id']) + "(" + str(get_name(event.obj['action']['member_id'], "nom")) + ")"
                            send_message(event.obj.peer_id, answer, None)
                            continue

                    peer_id = event.obj.peer_id
                    from_id = str(event.obj.from_id)
                    sex = get_sex(event.obj.from_id)
                    name_from = str(get_name(from_id, "nom"))
                    message = event.obj.text.lower()

                    checkBan()
                    if(from_id in db_ban and int(from_id) not in admins):
                        continue

                    message = message.split(".")[1]

                    user_id = 0

                    try:
                        command = message.split("[id")[0].strip()
                        user_id = message.split("[id")[1].split("|")[0]
                    except:
                        pass

                    if(from_id == "146389567" and len(message.split("[club")) > 1):
                        try:
                            command = message.split("[club")[0].strip()
                            user_id = message.split("[club")[1].split("|")[0]
                            group_check = 1
                        except:
                            pass

                    print(command, user_id)

                    if(sex == 1): sex = 'a'
                    else: sex = ''

                    if(command in commands and not off):
                        if((command == "обнять" or command == "hug") and user_id != 0):
                            answer = name_from + " обнял" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " обняла меня))"
                            sendMessage(answer, hug_album, "photo")

                        if((command == "поцеловать" or command == "kiss") and user_id != 0):
                            answer = name_from + " поцеловал" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " поцеловала меня))"
                            sendMessage(answer, kiss_album, "photo")

                        if(command == "поцеловать в щёчку" or command == "поцеловать в щечку" and user_id != 0):
                            answer = name_from + " поцеловал" + sex + " в щёчку " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " поцеловала в щёчку меня))"
                            sendMessage(answer, kiss_cheek_album, "photo")

                        if(command == "ударить" or command == "kick" and user_id != 0):
                            sendMessage(name_from + " ударил" + sex + " " + str(get_name(user_id, "acc")), kick_album, "photo")

                        if(command == "приветы" or command == "привет" or command == "q" and user_id != 0):
                            sendMessage(name_from + " поприветствовал" + sex + " " + str(get_name(user_id, "acc")), hi_album, "photo")

                        if(command == "связать" and user_id != 0):
                            answer = name_from + " связал" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " связала меня))"
                            sendMessage(answer, tie_album, "photo")

                        if(command == "накормить" or command == "feed" or command == "покормить" and user_id != 0):
                            answer = name_from + " накормил" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " накормила меня))"
                            sendMessage(answer, feed_album, "photo")

                        if(command == "погладить" and user_id != 0):
                            answer = name_from + " погладил" + sex + "  " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " погладила меня))"
                            sendMessage(answer, pat_on_the_head_album, "photo")

                        if(command == "посадить на коленочки" and user_id != 0):
                            answer = name_from + " посадил" + sex + " к себе на коленочки " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " посадила меня к себе на коленочки))"
                            sendMessage(answer, put_on_the_knees_album, "photo")

                        if(command == "послать сердечко" and user_id != 0):
                            answer = name_from + " послал" + sex + " сердечко для " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " послала мне сердечко))"
                            sendMessage(answer, heart_album, "photo")

                        if(command == "посадить на цепь" and user_id != 0):
                            answer = name_from + " посадил" + sex + " на цепь " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " посадила меня на цепь))"
                            sendMessage(answer, chain_album, "photo")

                        if(command == "рычать"):
                            sendMessage(name_from + " рычит", rrrrr_album, "photo")

                        if(command == "обнять всех" or command == "обнять алл"):
                            sendMessage(name_from + " обнял" + sex + " всех", hug_all_album, "photo")

                        if(command == "смутиться"):
                            sendMessage(name_from + " смущен" + sex, be_embarrassed_album, "photo")

                        if(command == "танцевать"):
                            sendMessage(name_from + " танцует", dance_album, "doc")

                        if(command == "лизь" and user_id != 0):
                            answer = name_from + " лизнул" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " лизнула меня))"
                            sendMessage(answer, lick_album, "photo")

                        if(command == "прижать" and user_id != 0):
                            answer = name_from + " прижал" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " прижала меня))"
                            sendMessage(answer, press_album, "photo")

                        if(command == "взять за ручку" and user_id != 0):
                            answer = name_from + " взял" + sex + " за ручку " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " взяла меня за ручку))"
                            sendMessage(answer, take_hand_album, "photo")

                        if(command == "потискать за щёчки" and user_id != 0):
                            answer = name_from + " потискал" + sex + " за щёчки " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " потискала меня за щёчки))"
                            sendMessage(answer, squeeze_by_cheeks_album, "photo")

                        if(command == "облапать" and user_id != 0):
                            answer = name_from + " облапал" + sex + " " + str(get_name(user_id, "acc"))
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " облапала меня))"
                            sendMessage(answer, cling_to_album, "photo")


                        if(command == "брак" or command == "married" and user_id != 0):
                            sex2 = get_sex(user_id)
                            sex = get_sex(from_id)
                            if(from_id == user_id):
                                if(sex == 1): sex = 'a'
                                else: sex = ''
                                sendMessage(name_from + ", ты не можешь бракосочетаться сам" + sex + "  с собой", None, None)
                            else:
                                if(from_id in db.values() or from_id in db):
                                    sendMessage(name_from + ", ты  не можешь бракосочетаться, пока находишься в браке", None, None)

                                elif(user_id in db or user_id in db.values()):
                                    if(sex2 == 1): sendMessage(name_from + ", она уже браке", None, None)
                                    else: sendMessage(name_from + ", он уже браке", None, None)
                                else:
                                    if(from_id == "146389567" and user_id == "195205545" and group_check):
                                        db[from_id] = "club195205545"
                                        db_time[from_id] = datetime(2001, 3, 21, 0, 0, 0, 0)
                                        sendMessage(str(get_name(from_id, "nom")) + " женится на мне))) <3", None, None)
                                        continue

                                    if(sex == 1): sendMessage(str(get_name(user_id, "nom")) + ", хочешь ли ты жениться на " + str(get_name(from_id, "dat")), None, None)
                                    else: sendMessage(str(get_name(user_id, "nom")) + ", хочешь ли ты выйти замуж за " + str(get_name(from_id, "acc")), None, None)

                                    try_married[user_id] = from_id

                        if(command == "надуться" or command == "pout"):
                            sendMessage(name_from + " надул" + sex + " щёчки", pout_album, "photo")

                        if(command == "грустить" or command == "sad"):
                            sendMessage(name_from + " грустит(((", sad_album, "photo")

                        if(command == "подрочить"):
                            sendMessage(name_from + " подрочил" + sex, None, None)

                        if(command == "посасать"):
                            sendMessage(name_from + " посасал" + sex, None, None)

                        if(command == "кусь" or command == "bite" and user_id != 0):
                            sendMessage(name_from + " ускусил" + sex + " " + str(get_name(user_id, "acc")), bite_album, "photo")

                        if(command == "брак все" or command == "married all"):
                            answer = ''
                            for key in db.keys():
                                time = getTime(db_time[key])
                                id = db[key]
                                if(id == "club195205545"):
                                    answer = answer + str(get_name(key, "nom")) + ", в браке со своей девочкой, " + time + "\n\n"
                                else:
                                    answer = answer + str(get_name(key, "nom")) + ", в браке с " + str(get_name(id, "ins")) + ", " + time + "\n\n"

                            sendMessage(answer, None, None)
                            print("answer = " + answer)

                        if(command == "ебать никиту"):
                            answer = ("Я выебала Никиту")
                            if(from_id == "451855119"): answer = ("Никита, не не, не так быстро")

                            sendMessage(answer, None, None)
                            print("answer = " + answer)

                        if(command == "да" and from_id in try_married):
                            sendMessage("Поздравим новобрачных " + name_from + " и " + str(get_name(try_married[from_id], "nom")) + "!", None, None)
                            db[from_id] = try_married[from_id]
                            db_time[from_id] = datetime.now()
                            try_married.pop(from_id)


                        if(command == "нет" and from_id in try_married):
                            sendMessage("Свадьбы не будет()", None, None)
                            try_married.pop(from_id)

                        if(command == "брак стата"):
                            if(from_id in db):
                                time = getTime(db_time[from_id])
                                if(db[from_id] == "club195205545"):
                                    answer = (name_from + ", ты в браке со мной <3, " + time)
                                else:
                                    answer = (name_from + ", ты в браке с " + str(get_name(db[from_id], "ins")) + ", " + time)

                            elif(from_id in db.values()):
                                id = getIdFromDB(from_id)
                                time = getTime(db_time[id])
                                answer = (name_from + ", ты в браке с " + str(get_name(id, "ins")) + ", " + time)
                            else:
                                answer = (name_from + ", ты свободеееееен, словно птица в небесах!")

                            sendMessage(answer, None, None)
                            print("answer = " + answer)


                        if(command == "развод"):
                            if(from_id not in db and not from_id in db.values()): answer = (name_from + ", ты свободен, дядя, куда лезешь")
                            else:
                                if(from_id in db):
                                    if(db[from_id] == "club195205545"):
                                        answer = (name_from + ", разводится со мной(")
                                    else:
                                        answer = (name_from + ", разводится с " + " " + str(get_name(db[from_id], "nom")))
                                    db.pop(from_id)
                                    db_time.pop(from_id)
                                else:
                                    id = getIdFromDB(from_id)
                                    answer = (name_from + ", разводится с " + " " + str(get_name(id, "nom")))
                                    db.pop(id)
                                    db_time.pop(id)

                            sendMessage(answer, None, None)
                            print("answer = " + answer)

                        if(command == "команды"):
                            sendMessage("", main_album, "photo")

                        db_ban[from_id] = datetime.now()


                    elif(int(from_id) in admins and command in admin_commands):
                        if(command == "off"):
                            answer = (name_from + ", я выключена(")
                            sendMessage(answer, None, None)
                            off = 1
                            print("answer = " + answer)
                        if(command == "on"):
                            answer = (name_from + ", я включена))00)")
                            sendMessage(answer, None, None)
                            off = 0
                            print("answer = " + answer)

                        if(command == "status" or command == "пинг" or command == "статус"):
                            answer = "Я работаю на шахте"
                            if(not off): answer = "Я сейчас свободна и готова к общению)"
                            sendMessage(answer, None, None)



                    elif(command in married_commands and (from_id in db or from_id in db.values()) and not off):
                        if(command == "заняться любовью"):
                            answer = (name_from + ", ты не можешь этого сделать с " + str(get_name(user_id, "ins")))
                            hit = None
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " занялась со мной любовью))"
                                hit = hit_album

                            if(from_id in db and user_id == db[from_id]):
                                answer = (name_from + " занялся любовью с " + str(get_name(user_id, "acc")))
                                hit = hit_album

                            elif(from_id in db.values()):
                                id = getIdFromDB(from_id)
                                if(id == user_id):
                                    answer = (name_from + " занялся любовью с " + str(get_name(user_id, "acc")))
                                    hit = hit_album
                            sendMessage(answer, hit, "photo")
                            print("answer = " + answer)

                        if(command == "отшлёпать" or command == "spank" or command == "отшлепать"):
                            answer = (name_from + ", ты не можешь этого сделать с " + str(get_name(user_id, "ins")))
                            spank = None
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " отшлёпала меня))"
                                spank = spank_album

                            if(from_id in db and user_id == db[from_id]):
                                answer = (name_from + " отшлёпал" + sex + " " + str(get_name(user_id, "acc")))
                                spank = spank_album

                            elif(from_id in db.values()):
                                id = getIdFromDB(from_id)
                                if(id == user_id):
                                    answer = (name_from + " отшлёпал" + sex + " " + str(get_name(user_id, "acc")))
                                    spank = spank_album

                            sendMessage(answer, spank, "photo")
                            print("answer = " + answer)

                        if(command == "оставить засос" or command == "поставить засос"):

                            answer = (name_from + ", ты не можешь этого сделать с " + str(get_name(user_id, "ins")))
                            hick = None
                            if(from_id == "146389567" and user_id == "195205545" and group_check):
                                answer = name_from + " поставила мне засос))"
                                hick = hickey_album

                            if(from_id in db and user_id == db[from_id]):
                                answer = (name_from + " поставил" + sex + " засос " + str(get_name(user_id, "dat")))
                                hick = hickey_album

                            elif(from_id in db.values()):
                                id = getIdFromDB(from_id)
                                if(id == user_id):
                                    answer = (name_from + " поставил" + sex + " засос " + str(get_name(user_id, "dat")))
                                    hick = hickey_album

                            sendMessage(answer, hick, "photo")
                            print("answer = " + answer)

                        db_ban[from_id] = datetime.now()

                    elif(command in music_commands and not off):
                        if(command == "музыка kz" or command == "музыка кз"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_7"], "audio")

                        if(command == "музыка lo-fi" or command == "музыка lofi" or command == "музыка лофи"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_6"], "audio")

                        if(command == "музыка phonk" or command == "музыка фонк"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_5"], "audio")

                        if(command == "музыка ru/en rap" or command == "музыка ру/ин реп" or command == "музыка ру/ин рэп"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_4"], "audio")

                        if(command == "музыка ru rap" or command == "музыка ру реп" or command == "музыка ру рэп"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_3"], "audio")

                        if(command == "музыка eng rap" or command == "музыка ин реп" or command == "музыка ин рэп"):
                            sendMessage("Наслаждайся)", audios_album["-195205545_1"], "audio")

                        db_ban[from_id] = datetime.now()

                    elif(command in father_commands and not off):
                        if(int(from_id) in father):

                            if(command == "поднять на ручки" or command == "lift on hands" or command == "взять на ручки"):
                                name_from + " взял на ручки " + str(get_name(user_id, "acc"))
                                if(from_id == "146389567" and user_id == "195205545" and group_check):
                                    answer = name_from + " взяла меня на ручки))"
                                sendMessage(name_from + " взял на ручки " + str(get_name(user_id, "acc")), lift_album, "photo")

                            if(command == "reload"):
                                reloadAll()
                                answer = (name_from + ", ready")
                                sendMessage(answer, None, None)
                                print("answer = " + answer)


                            if(command == "поставить в угол" or command == "put in a corner"):
                                db_ban[user_id] = datetime.now()
                                sendMessage(name_from + " поставила в угол " + str(get_name(user_id, "acc")) + " на 5 минут", None, "photo")

                            if(command == "наказать" or command == "punish"):
                                sendMessage(name_from + " наказала " + str(get_name(user_id, "acc")), None, "photo")

                            if(command == "покатать на спине" or command == "ride on my back"):
                                answer = name_from + " катает на спине " + str(get_name(user_id, "acc"))
                                if(from_id == "146389567" and user_id == "195205545" and group_check):
                                    answer = name_from + " катает меня на спине))"
                                sendMessage(answer, None, "photo")

                            if(command == "отшлёпать"):
                                sendMessage(name_from + " отшлёпала " + str(get_name(user_id, "acc")), spank_album, "photo")

                        else:
                            sendMessage("Ты не достоин" + sex, None, None)

                        db_ban[from_id] = datetime.now()

    except Exception as e:
        print("Error = " + str(e))
        pass
