from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api, random, shelve
from random import randint
from datetime import datetime, timedelta
from upload_media.reloadMusic import reloadMusic
from time_library import *
import config.commands as conf




dance_album = []

gifs_album = {}
photos_album = {}
audios_album = {}
main_album = ["457240076"]



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


def getPhotos(album_id):
    #print(album_id)
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

def reloadPhotos():
    global photos_album
    photos_album = {}
    offset = 0

    photos = vk1.method("photos.getAll", {"owner_id": -195205545, "count": 200, "offset": offset})
    addNewPhotos(photos)

    for i in range(photos["count"] // 200):
        offset += 200
        addNewPhotos(vk1.method("photos.getAll", {"owner_id": -195205545, "count": 200, "offset": offset}))



def sendMessage(text, album, type):
    media = None
    if(album): media = type + "-195205545_" + album[randint(0, len(album) - 1)]
    send_message(peer_id, text, media)
    print("answer = " + text)



def checkBan():
    for key in db_ban.keys():
        if(datetime.now() - db_ban[key] > timedelta(minutes=1)):
            db_ban.pop(key)


def reloadGifs():
    global dance_album
    global gifs_album

    gifs_album = getAllGifs()
    dance_album = getGifs("dance")


def getAllInfoConversations():
    #conversations = vk.method("messages.getConversations", {"owner_id": -195205545, "count": 200, "offset": offset})
    allInfoConversations = {}
    admins = []
    conversations = ['2000000001']#, 2000000016] 2000000002 2000000019


    for conversation in conversations:
        allInfoConversations[conversation] = {}
        users = vk.method("messages.getConversationMembers", {"peer_id": conversation})
        for user in users['items']:
            print(user)
            if(user['member_id'] < 0):
                continue
            try:
                acc = get_name(user['member_id'], 'acc')
                nom = get_name(user['member_id'], 'nom')
            except:
                pass
            allInfoConversations[conversation][str(user['member_id'])] = {
                                                        'acc': acc,
                                                        'nom': nom
                                                        }
            if('is_admin' in user):
                try:
                    allInfoConversations[conversation]['admins']
                except:
                    allInfoConversations[conversation]['admins'] = []

                allInfoConversations[conversation]['admins'].append(str(user['member_id']))

        print(allInfoConversations)
        return allInfoConversations







def reloadAll():
    reloadPhotos()
    reloadGifs()
    global audios_album
    global conversations
    conversations = getAllInfoConversations()
    #audios_album = reloadMusic()
    print("Ready")


db = shelve.open('db/users') #married users
db_time = shelve.open('db/time') #time married
db_ban = shelve.open('db/ban') #cooldown
#db_commands = shelve.open('db/commands_list') # all commands




try_married = {}
timer = {}

off = 0


vk = vk_api.VkApi(token="927d0c2eb68bc3197ee29a3634b0de4466b1b66ec0cddbc76142138a1e1c8dc83f2b35fb8354e013c3a25") #bot
vk._auth_token()
vk.get_api()


vk1 = vk_api.VkApi(token="beca55e59eeb78065d9c448d195ed79ea32d72e1d5c280be6a0116588df0e544a8eb29196f3b1c3487a79") # second account
vk1._auth_token()
vk1.get_api()


longpoll = VkBotLongPoll(vk, 195205545)

'''
married_commands = db_commands["married_commands"]
admin_commands = db_commands["admin_commands"]
father_commands = db_commands["father_commands"]
no_commands = db_commands["no_commands"]
music_commands = db_commands["music_commands"]
'''


conversations = {}
father = ['146389567']

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

                    peer_id = str(event.obj.peer_id)
                    from_id = str(event.obj.from_id)
                    sex = get_sex(event.obj.from_id)
                    name_from = conversations[peer_id][from_id]['nom']
                    message = event.obj.text.lower()

                    checkBan()

                    if(from_id in db_ban and from_id not in conversations[peer_id]['admins']):
                        continue

                    if(peer_id == 2000000016 and peer_id == 2000000002):
                        continue

                    message = message.split(".")[1]

                    user_id = 0

                    try:
                        command = message.split("[id")[0].strip()
                        user_id = message.split("[id")[1].split("|")[0]
                    except:
                        pass


                    print(command, user_id)

                    if(sex == 1): conf.sex = 'a'
                    else: conf.sex = ''

                    answer = ''
                    media = None
                    type = None

                    dict = conf.get_dict()


                    if(command in dict['default']['all']):# and conversations[peer_id]['online']):
                        answer = name_from + dict['default']['all'][command]['answer'] + conversations[peer_id][user_id]['acc'] + ' new bot'
                        media = photos_album[dict['default']['all'][command]['media']]
                        type = 'photo'
                        db_ban[from_id] = datetime.now()

                    if(peer_id in dict.keys()): # and conversations[peer_id]['online']):
                        if(command in dict[peer_id]['all']):
                            answer = name_from + dict[peer_id]['all'][command]['answer'] + conversations[peer_id][user_id]['acc'] + ' new bot'
                            media = photos_album[dict[peer_id]['all'][command]['media']]
                            type = 'photo'
                            db_ban[from_id] = datetime.now()


                    if(command in dict['default']['admins'] and from_id in conversations[peer_id]['admins']):
                        if(command == "off"):
                            pass


                    sendMessage(answer, media, type)


    except Exception as e:
        print("Error = " + str(e))
        pass
