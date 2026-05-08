import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import json
from datetime import datetime, timedelta

# =====================================================
# 🔧 BAS YAHAN CHANGE KARO
# =====================================================

BOT_TOKEN = "7227323007:AAG7sFq7xE65LxLeuX6KzNE-9-7lQ7B9Wm4"
OWNER_ID = 6588590835

# APNI IMAGE KA LINK YAHAN DALO
START_IMAGE_URL = "https://telegra.ph/your-image-link-here"

# BAKI SAB SAME
DEMO_CHANNEL = "https://t.me/+T_YM_KTpFjU5MzE9"
PROOFS_CHANNEL = "https://t.me/+WZkPq0nJjyczMDM1"
UPI_ID = "paytmqr109tak3mus@paytm"

PREMIUM_CHANNELS = """
🎬 **𝐘𝐎𝐔𝐑 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒** 🎬

• [𝐌𝐚𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/your_main_channel)
• [𝐁𝐚𝐜𝐤𝐮𝐩 𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/your_backup_channel)
• [𝐕𝐈𝐏 𝐂𝐨𝐧𝐭𝐞𝐧𝐭](https://t.me/your_vip_channel)

⚠️ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 𝐭𝐨 𝐚𝐥𝐥 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐨𝐫 𝐟𝐮𝐥𝐥 𝐚𝐜𝐜𝐞𝐬𝐬!
"""

PLANS = {
    "69": {"text": "🔥 ₹𝟔𝟗/𝐌𝐨𝐧𝐭𝐡 🔥", "duration": "30"},
    "129": {"text": "💎 ₹𝟏𝟐𝟗/𝟑 𝐌𝐨𝐧𝐭𝐡𝐬 💎", "duration": "90"},
    "199": {"text": "👑 ₹𝟏𝟗𝟗/𝐋𝐢𝐟𝐞𝐭𝐢𝐦𝐞 👑", "duration": "365"},
    "299": {"text": "💦 ₹𝟐𝟗𝟗/𝐔𝐥𝐭𝐢𝐦𝐚𝐭𝐞 💦", "duration": "730"},
    "499": {"text": "⭐ ₹𝟒𝟗𝟗/𝐕𝐈𝐏 ⭐", "duration": "999"}
}

# =====================================================

bot = telebot.TeleBot(BOT_TOKEN)

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)

users = load_users()
pending = {}

# 𝐀𝐋𝐋 𝐌𝐄𝐒𝐒𝐀𝐆𝐄𝐒 𝐈𝐍 𝐁𝐎𝐋𝐃 𝐒𝐂𝐑𝐈𝐏𝐓 𝐅𝐎𝐑𝐌𝐀𝐓
msg = """🥵𝐀𝐋𝐋 𝐓𝐘𝐏𝐄 𝐏*𝐑𝐍 𝐕𝐈𝐃𝐄𝐎𝐒 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 🍑💦 

🫦𝐌𝐎𝐌-𝐒𝐎𝐍                     🫦💦 
🫦𝐂𝐇*𝐋𝐃-𝐏*𝐑𝐍                🫦💦 
🫦𝐑𝐏𝐄-𝐏*𝐑𝐍                      🫦💦
🫦 𝐃𝐄𝐒𝐈 𝐁𝐇𝐀𝐁𝐇𝐈              🫦💦 
🫦 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝐒𝐓𝐀𝐑     🫦💦 
🫦 𝐓𝐄𝐄𝐍 𝐈𝐍𝐃𝐈𝐀𝐍              🫦💦
🫦𝐁𝐑𝐎𝐓𝐇𝐄𝐑-𝐒𝐈𝐒𝐓𝐄𝐑     🫦💦 
🫦𝐀𝐔𝐍𝐓𝐘-𝐏*𝐑𝐍                🫦💦 
🫦𝐅𝐎𝐑𝐄𝐈𝐆𝐍𝐄𝐑                  🫦💦

🥵 𝘼𝙇𝙇 𝙏𝙃𝙀 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙎𝙏𝙐𝙁𝙁𝙎

⚡ 𝐈𝐧𝐬𝐭𝐚𝐧𝐭 𝐀𝐜𝐜𝐞𝐬𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐅𝐨𝐫 𝐘𝐨𝐮!
👇 𝐂𝐥𝐢𝐜𝐤 𝐆𝐄𝐓 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐧𝐝 𝐜𝐥𝐚𝐢𝐦 𝐲𝐨𝐮𝐫 𝐝𝐞𝐚𝐥 𝐧𝐨𝐰!"""

@bot.message_handler(commands=['start'])
def start_cmd(message):
    user_id = str(message.from_user.id)
    
    if user_id not in users:
        users[user_id] = {
            "first_seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "premium": False,
            "username": message.from_user.username or "𝐍𝐨 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞"
        }
        save_users(users)
        bot.send_message(OWNER_ID, f"🆕 𝐍𝐞𝐰 𝐔𝐬𝐞𝐫: {message.from_user.first_name}\n𝐈𝐃: {user_id}")
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("😍 𝐆𝐄𝐓 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 😍", callback_data="get_premium"),
        InlineKeyboardButton("👀 𝐒𝐄𝐄 𝐃𝐄𝐌𝐎", url=DEMO_CHANNEL)
    )
    
    try:
        bot.send_photo(message.from_user.id, START_IMAGE_URL, caption=msg, reply_markup=keyboard)
    except:
        bot.send_message(message.from_user.id, msg, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "get_premium")
def premium_entry(call):
    if users.get(str(call.from_user.id), {}).get("premium", False):
        bot.answer_callback_query(call.id, "✅ 𝐘𝐨𝐮 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐚𝐯𝐞 𝐏𝐫𝐞𝐦𝐢𝐮𝐦!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    bot.send_message(call.from_user.id, "💋 𝐎𝐍𝐋𝐘 𝐅𝐎𝐑 𝐘𝐎𝐔 💋")
    time.sleep(1)
    
    msg2 = """💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐄𝐍𝐓𝐑𝐘 💎
━━━━━━━━━━━━━━━━━━
⚡ 𝐄𝐧𝐭𝐫𝐲: 🚀 𝐈𝐧𝐬𝐭𝐚𝐧𝐭
👥 𝐀𝐜𝐭𝐢𝐯𝐞 𝐔𝐬𝐞𝐫𝐬: 𝟏𝟒,𝟓𝟎𝟎+
⭐ 𝐑𝐚𝐭𝐢𝐧𝐠: 𝟒.𝟗/𝟓.𝟎
━━━━━━━━━━━━━━━━━━

💋 𝐒𝐄𝐋𝐄𝐂𝐓 𝐘𝐎𝐔𝐑 𝐌𝐄𝐌𝐁𝐄𝐑𝐒𝐇𝐈𝐏 💋:
• 𝐋𝐢𝐟𝐞𝐭𝐢𝐦𝐞 𝐀𝐜𝐜𝐞𝐬𝐬 🥵
• 𝟐𝟒/𝟕 𝐏𝐫𝐢𝐨𝐫𝐢𝐭𝐲 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✅

👇 𝐂𝐇𝐎𝐎𝐒𝐄 𝐀 𝐏𝐋𝐀𝐍 𝐓𝐎 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐄 👇:"""
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    for amount, plan in PLANS.items():
        keyboard.add(InlineKeyboardButton(plan["text"], callback_data=f"plan_{amount}"))
    
    bot.send_message(call.from_user.id, msg2, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith("plan_"))
def payment_details(call):
    amount = call.data.split("_")[1]
    plan_text = PLANS[amount]["text"]
    
    user_id = str(call.from_user.id)
    
    payment_msg = f"""💸 **𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐃𝐄𝐓𝐀𝐈𝐋𝐒** 💸

📌 **𝐏𝐥𝐚𝐧:** {plan_text}
💰 **𝐀𝐦𝐨𝐮𝐧𝐭:** ₹{amount}
⏱️ **𝐕𝐚𝐥𝐢𝐝𝐢𝐭𝐲:** {PLANS[amount]['duration']} 𝐝𝐚𝐲𝐬

━━━━━━━━━━━━━━━━━━
**📤 𝐒𝐄𝐍𝐃 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐓𝐎:**
🏦 **𝐔𝐏𝐈 𝐈𝐃:** `{UPI_ID}`

**📝 𝐈𝐍𝐒𝐓𝐑𝐔𝐂𝐓𝐈𝐎𝐍𝐒:**
1. 𝐒𝐞𝐧𝐝 𝐞𝐱𝐚𝐜𝐭𝐥𝐲 ₹{amount} 𝐭𝐨 𝐚𝐛𝐨𝐯𝐞 𝐔𝐏𝐈 𝐈𝐃
2. 𝐓𝐚𝐤𝐞 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐨𝐟 𝐩𝐚𝐲𝐦𝐞𝐧𝐭
3. 𝐂𝐥𝐢𝐜𝐤 "✅ 𝐈 𝐇𝐀𝐕𝐄 𝐏𝐀𝐈𝐃" 𝐛𝐞𝐥𝐨𝐰
4. 𝐒𝐞𝐧𝐝 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐡𝐞𝐫𝐞

━━━━━━━━━━━━━━━━━━
⚠️ 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐯𝐞𝐫𝐢𝐟𝐢𝐞𝐝 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲
⏰ 𝐌𝐚𝐱 𝐰𝐚𝐢𝐭 𝐭𝐢𝐦𝐞: 𝟓-𝟏𝟎 𝐦𝐢𝐧𝐮𝐭𝐞𝐬

💬 **𝐀𝐟𝐭𝐞𝐫 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰:**"""

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("✅ 𝐈 𝐇𝐀𝐕𝐄 𝐏𝐀𝐈𝐃", callback_data=f"paid_{amount}"),
        InlineKeyboardButton("❌ 𝐂𝐀𝐍𝐂𝐄𝐋", callback_data="cancel_payment")
    )
    
    bot.send_message(call.from_user.id, payment_msg, reply_markup=keyboard, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data == "cancel_payment")
def cancel_payment(call):
    bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=None)
    bot.send_message(call.from_user.id, "❌ 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐜𝐚𝐧𝐜𝐞𝐥𝐥𝐞𝐝. 𝐔𝐬𝐞 /𝐬𝐭𝐚𝐫𝐭 𝐭𝐨 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("paid_"))
def payment_received(call):
    amount = call.data.split("_")[1]
    
    bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=None)
    
    pending[str(call.from_user.id)] = {
        "amount": amount,
        "plan": PLANS[amount]["text"],
        "duration": PLANS[amount]["duration"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    admin_msg = f"""🔔 **𝐍𝐄𝐖 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐑𝐄𝐐𝐔𝐄𝐒𝐓** 🔔

👤 **𝐔𝐬𝐞𝐫:** {call.from_user.first_name}
🆔 **𝐈𝐃:** `{call.from_user.id}`
💰 **𝐀𝐦𝐨𝐮𝐧𝐭:** ₹{amount}
📅 **𝐏𝐥𝐚𝐧:** {PLANS[amount]['text']}
⏱️ **𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {PLANS[amount]['duration']} 𝐝𝐚𝐲𝐬
🕐 **𝐓𝐢𝐦𝐞:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📤 **𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐩𝐚𝐲𝐦𝐞𝐧𝐭 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐡𝐞𝐫𝐞**

𝐔𝐬𝐞 /𝐚𝐩𝐩𝐫𝐨𝐯𝐞 {call.from_user.id} {amount} 𝐭𝐨 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞 𝐩𝐫𝐞𝐦𝐢𝐮𝐦"""
    
    bot.send_message(OWNER_ID, admin_msg)
    bot.send_message(call.from_user.id, """✅ **𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐑𝐄𝐂𝐄𝐈𝐕𝐄𝐃** ✅

📸 **𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐩𝐚𝐲𝐦𝐞𝐧𝐭 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐧𝐨𝐰**

⏰ 𝐎𝐮𝐫 𝐭𝐞𝐚𝐦 𝐰𝐢𝐥𝐥 𝐯𝐞𝐫𝐢𝐟𝐲 𝐢𝐭 𝐰𝐢𝐭𝐡𝐢𝐧 𝟓-𝟏𝟎 𝐦𝐢𝐧𝐮𝐭𝐞𝐬

💬 **𝐀𝐟𝐭𝐞𝐫 𝐯𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧, 𝐲𝐨𝐮𝐫 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝!**""")

@bot.message_handler(commands=['approve'])
def approve_user(message):
    if message.from_user.id != OWNER_ID:
        return
    
    try:
        parts = message.text.split()
        user_id = parts[1]
        amount = parts[2]
        
        if user_id in pending:
            users[user_id]["premium"] = True
            expiry = datetime.now() + timedelta(days=int(PLANS[amount]["duration"]))
            users[user_id]["expiry"] = expiry.strftime("%Y-%m-%d %H:%M:%S")
            users[user_id]["plan"] = PLANS[amount]["text"]
            save_users(users)
            
            bot.send_message(int(user_id), f"""✅ **𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃!** ✅

🎉 𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬! 𝐘𝐨𝐮𝐫 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐢𝐬 𝐧𝐨𝐰 𝐚𝐜𝐭𝐢𝐯𝐞.

📌 **𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧:** {PLANS[amount]['text']}
⏱️ **𝐕𝐚𝐥𝐢𝐝 𝐔𝐩𝐭𝐨:** {expiry.strftime('%Y-%m-%d %H:%M:%S')}

🚀 **𝐔𝐬𝐞 /premium 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐲𝐨𝐮𝐫 𝐜𝐨𝐧𝐭𝐞𝐧𝐭**

𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐣𝐨𝐢𝐧𝐢𝐧𝐠! 🥵""")
            
            bot.send_message(OWNER_ID, f"✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 `{user_id}`")
            del pending[user_id]
        else:
            bot.send_message(OWNER_ID, "❌ 𝐔𝐬𝐞𝐫 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐩𝐞𝐧𝐝𝐢𝐧𝐠 𝐥𝐢𝐬𝐭")
    except:
        bot.send_message(OWNER_ID, "❌ 𝐔𝐬𝐞: /𝐚𝐩𝐩𝐫𝐨𝐯𝐞 <𝐮𝐬𝐞𝐫_𝐢𝐝> <𝐚𝐦𝐨𝐮𝐧𝐭>")

@bot.message_handler(commands=['premium'])
def premium_content(message):
    user_id = str(message.from_user.id)
    
    if not users.get(user_id, {}).get("premium", False):
        bot.send_message(message.from_user.id, "❌ **𝐘𝐨𝐮 𝐝𝐨𝐧'𝐭 𝐡𝐚𝐯𝐞 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬!**\n\n𝐔𝐬𝐞 /𝐬𝐭𝐚𝐫𝐭 𝐭𝐨 𝐛𝐮𝐲 𝐩𝐫𝐞𝐦𝐢𝐮𝐦.")
        return
    
    expiry = users[user_id].get("expiry")
    if expiry and datetime.now() > datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S"):
        users[user_id]["premium"] = False
        save_users(users)
        bot.send_message(message.from_user.id, "❌ **𝐘𝐨𝐮𝐫 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐡𝐚𝐬 𝐞𝐱𝐩𝐢𝐫𝐞𝐝!**\n\n𝐔𝐬𝐞 /𝐬𝐭𝐚𝐫𝐭 𝐭𝐨 𝐫𝐞𝐧𝐞𝐰.")
        return
    
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton("🚀 𝐀𝐂𝐂𝐄𝐒𝐒 𝐍𝐎𝐖 🚀", url=PREMIUM_CHANNELS))
    
    premium_msg = f"""🎬 **𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐙𝐎𝐍𝐄** 🎬

👑 **𝐔𝐬𝐞𝐫:** {message.from_user.first_name}
📌 **𝐏𝐥𝐚𝐧:** {users[user_id].get('plan', 'Premium')}
⏱️ **𝐕𝐚𝐥𝐢𝐝 𝐔𝐩𝐭𝐨:** {users[user_id].get('expiry', 'Lifetime')}

━━━━━━━━━━━━━━━━━━
🥵 **𝐀𝐋𝐋 𝐂𝐎𝐍𝐓𝐄𝐍𝐓 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄** 🥵

• 𝐌𝐎𝐌-𝐒𝐎𝐍
• 𝐂𝐇*𝐋𝐃-𝐏*𝐑𝐍
• 𝐑𝐏𝐄-𝐏*𝐑𝐍
• 𝐃𝐄𝐒𝐈 𝐁𝐇𝐀𝐁𝐇𝐈
• 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝐒𝐓𝐀𝐑
• 𝐓𝐄𝐄𝐍 𝐈𝐍𝐃𝐈𝐀𝐍
• 𝐁𝐑𝐎𝐓𝐇𝐄𝐑-𝐒𝐈𝐒𝐓𝐄𝐑
• 𝐀𝐔𝐍𝐓𝐘-𝐏*𝐑𝐍
• 𝐅𝐎𝐑𝐄𝐈𝐆𝐍𝐄𝐑

━━━━━━━━━━━━━━━━━━
👇 **𝐂𝐥𝐢𝐜𝐤 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐚𝐥𝐥 𝐜𝐨𝐧𝐭𝐞𝐧𝐭** 👇"""
    
    bot.send_message(message.from_user.id, premium_msg, reply_markup=keyboard)

@bot.message_handler(commands=['users'])
def total_users(message):
    if message.from_user.id != OWNER_ID:
        return
    
    premium_count = sum(1 for u in users.values() if u.get("premium", False))
    total = len(users)
    
    bot.send_message(OWNER_ID, f"""📊 **𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒** 📊

👥 **𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬:** {total}
👑 **𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫𝐬:** {premium_count}
🆓 **𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫𝐬:** {total - premium_count}

📅 **𝐋𝐚𝐬𝐭 𝐔𝐩𝐝𝐚𝐭𝐞:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}""")

print("🤖 𝐁𝐨𝐭 𝐢𝐬 𝐫𝐮𝐧𝐧𝐢𝐧𝐠...")
bot.infinity_polling()