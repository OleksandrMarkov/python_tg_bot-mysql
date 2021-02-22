import telebot

bot = telebot.TeleBot("1473515056:AAGw2jnDgCQhxNxXxyWUvMinG63vnl4e3IU")

user_data = {}

class User:
	def __init__(self, first_name):
		self.first_name = first_name
		self.last_name = ''

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    msg = bot.send_message(message.chat.id, "Enter your first name, please")
    bot.register_next_step_handler(msg, process_first_name_step)

def process_first_name_step(message):
    try:
        user_id = message.from_user.id 
        user = User(message.text)
        user_data[user_id] = user

        msg = bot.send_message(message.chat.id, 'Enter your last name, please')
        bot.register_next_step_handler(msg, process_last_name_step)
    except Exception as e:
        bot.reply_to(message, 'First name entry error...')

def process_last_name_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text

        bot.send_message(message.chat.id, 'You have successfully registered!')
    except Exception as e:
        bot.reply_to(message, 'Last name entry error...')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
	bot.polling(none_stop = True)