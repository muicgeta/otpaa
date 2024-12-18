import os
import shutil
import sys
import subprocess
from telebot import TeleBot, types

API_TOKEN = "7577043232:AAEIh0T0JzXYSf6NwP_cjlP39dChhtcqZ0g"
bot = TeleBot(API_TOKEN)

# قائمة معرّفات المسؤولين
admins = [7069250607, '7069250607']

# مسار المجلد الذي يحتوي على ملفات البوت
BOT_FOLDER = '.'

# لحفظ عمليات التشغيل
processes = {}

def create_backup(file_path):
    """يحفظ نسخة احتياطية من الملف المحدد"""
    backup_path = f"{file_path}.bak"
    try:
        if os.path.exists(file_path):
            shutil.copy(file_path, backup_path)
            return backup_path
    except Exception as e:
        print(f"Error creating backup: {e}")
    return None

def restore_backup(file_path, backup_path):
    """يستعيد النسخة الاحتياطية من الملف المحدد"""
    try:
        if os.path.exists(backup_path):
            shutil.copy(backup_path, file_path)
            return True
    except Exception as e:
        print(f"Error restoring backup: {e}")
    return False

def restart_bot():
    """يعيد تشغيل البوت"""
    for admin_id in admins:
        try:
            bot.send_message(admin_id, 'Bot is restarting...')
        except Exception as e:
            print(f"Failed to send restart message to admin {admin_id}: {e}")

    # إعادة تشغيل البوت
    os.system(f'pkill -f {sys.argv[0]}')
    os.system(f'python3 {sys.argv[0]} &')

def list_files():
    """يعرض جميع الملفات في مجلد البوت"""
    try:
        files = os.listdir(BOT_FOLDER)
        files_list = [f for f in files if os.path.isfile(os.path.join(BOT_FOLDER, f))]
        return files_list
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    files_list = list_files()
    if not files_list:
        bot.reply_to(message, 'No files found in the bot directory.')
        return

    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton('قائمة الملفات')
    item2 = types.KeyboardButton('استرداد نسخة احتياطية')
    item3 = types.KeyboardButton('تشغيل ملف')
    item4 = types.KeyboardButton('إيقاف ملف')
    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, 'ما الذي تريد فعله؟', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'قائمة الملفات')
def list_files_command(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    files_list = list_files()
    if not files_list:
        bot.reply_to(message, 'No files found in the bot directory.')
        return

    file_list_message = '\n'.join([f"{idx + 1}. {file}" for idx, file in enumerate(files_list)])
    bot.send_message(message.chat.id, f"Files in the bot directory:\n{file_list_message}\n\nSend the number of the file you want to download or update.")

    bot.register_next_step_handler(message, file_choice)

def file_choice(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    try:
        choice = int(message.text) - 1
        files_list = list_files()
        if 0 <= choice < len(files_list):
            chosen_file = files_list[choice]
            bot.send_message(message.chat.id, f"You chose {chosen_file}. Send the file content to update it, or type 'download' to download the file.")
            bot.register_next_step_handler(message, lambda msg: handle_file_action(msg, chosen_file))
        else:
            bot.reply_to(message, 'Invalid choice. Please choose a valid number.')
            bot.register_next_step_handler(message, file_choice)
    except ValueError:
        bot.reply_to(message, 'Please enter a valid number.')
        bot.register_next_step_handler(message, file_choice)

def handle_file_action(message, file_name):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    # Check if the message contains text
    if message.text is not None and message.text.lower() == 'download':
        file_path = os.path.join(BOT_FOLDER, file_name)
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
    elif message.document:
        if message.document.file_name != file_name:
            bot.reply_to(message, 'File name mismatch. Please send the correct file.')
            return
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(BOT_FOLDER, file_name)
        
        # Save the backup
        backup_path = create_backup(file_path)
        if backup_path:
            bot.reply_to(message, 'Backup created successfully.')
        else:
            bot.reply_to(message, 'Failed to create backup.')

        # Replace the file content
        with open(file_path, 'wb') as file:
            file.write(downloaded_file)
        
        bot.reply_to(message, f'File {file_name} updated successfully.')
        restart_bot()
    else:
        bot.reply_to(message, 'Invalid action. Please send the correct file or type "download" to download the file.')

@bot.message_handler(func=lambda message: message.text == 'استرداد نسخة احتياطية')
def restore_backup_command(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    files_list = list_files()
    if not files_list:
        bot.reply_to(message, 'No files found in the bot directory.')
        return

    file_list_message = '\n'.join([f"{idx + 1}. {file}" for idx, file in enumerate(files_list)])
    bot.send_message(message.chat.id, f"Select a file to restore:\n{file_list_message}")
    bot.register_next_step_handler(message, restore_backup_choice)

def restore_backup_choice(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    try:
        choice = int(message.text) - 1
        files_list = list_files()
        if 0 <= choice < len(files_list):
            file_name = files_list[choice]
            file_path = os.path.join(BOT_FOLDER, file_name)
            backup_path = f"{file_path}.bak"
            if restore_backup(file_path, backup_path):
                bot.reply_to(message, f'Backup for {file_name} restored successfully.')
                restart_bot()
            else:
                bot.reply_to(message, f'Failed to restore backup for {file_name}.')
        else:
            bot.reply_to(message, 'Invalid choice. Please choose a valid number.')
            bot.register_next_step_handler(message, restore_backup_choice)
    except ValueError:
        bot.reply_to(message, 'Please enter a valid number.')
        bot.register_next_step_handler(message, restore_backup_choice)

@bot.message_handler(func=lambda message: message.text == 'تشغيل ملف')
def start_file_command(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    files_list = list_files()
    if not files_list:
        bot.reply_to(message, 'No files found in the bot directory.')
        return

    file_list_message = '\n'.join([f"{idx + 1}. {file}" for idx, file in enumerate(files_list)])
    bot.send_message(message.chat.id, f"Select a file to start:\n{file_list_message}")
    bot.register_next_step_handler(message, start_file_choice)

def start_file_choice(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    try:
        choice = int(message.text) - 1
        files_list = list_files()
        if 0 <= choice < len(files_list):
            file_name = files_list[choice]
            file_path = os.path.join(BOT_FOLDER, file_name)
            
            # Start the file
            process = subprocess.Popen(['python3', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes[file_name] = process
            bot.reply_to(message, f'File {file_name} started successfully.')
        else:
            bot.reply_to(message, 'Invalid choice. Please choose a valid number.')
            bot.register_next_step_handler(message, start_file_choice)
    except ValueError:
        bot.reply_to(message, 'Please enter a valid number.')
        bot.register_next_step_handler(message, start_file_choice)

@bot.message_handler(func=lambda message: message.text == 'إيقاف ملف')
def stop_file_command(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    if not processes:
        bot.reply_to(message, 'No running files to stop.')
        return

    running_files_list = '\n'.join([f"{idx + 1}. {file}" for idx, file in enumerate(processes.keys())])
    bot.send_message(message.chat.id, f"Select a file to stop:\n{running_files_list}")
    bot.register_next_step_handler(message, stop_file_choice)

def stop_file_choice(message):
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, 'You are not authorized to perform this action.')
        return

    try:
        choice = int(message.text) - 1
        running_files = list(processes.keys())
        if 0 <= choice < len(running_files):
            file_name = running_files[choice]
            process = processes.pop(file_name, None)
            if process:
                process.terminate()
                bot.reply_to(message, f'File {file_name} stopped successfully.')
            else:
                bot.reply_to(message, f'Failed to stop {file_name}.')
        else:
            bot.reply_to(message, 'Invalid choice. Please choose a valid number.')
            bot.register_next_step_handler(message, stop_file_choice)
    except ValueError:
        bot.reply_to(message, 'Please enter a valid number.')
        bot.register_next_step_handler(message, stop_file_choice)

@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.reply_to(message, "Invalid command. Please use the provided options.")

if __name__ == "__main__":
    bot.polling(none_stop=True)