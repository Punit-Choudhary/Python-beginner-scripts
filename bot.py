from telegram import *
from telegram.ext import *
import requests
from bs4 import BeautifulSoup

def price(update: Updater, context: CallbackContext):
    URL = 'https://finance.yahoo.com/quote/BTC-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAKag91Xt7nUXOyMx3LF2u6obPjWGNprSxdZxgB8EAOz76XNxSTEVyfIgzvYxqMhbL8YIxWACcoMkcPsnyFhvqp4OZSgDY8CqIiwKfw_kUZ-S095-kZvmncLFS56Rl3wsm3Ls8JtfVigvVWeU-7kU9KhDGsfZYMv_-p_z8OU0ttSD'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = []
    for element in soup.findAll(attrs="D(ib) Mend(20px)"):
        price = element.find('span')
        if price not in results:
            results.append(price.text)
            print(results)
            bitcoin = "Bitcoin Price: " + results[0]
            print(bitcoin)
            bot.send_message(chat_id=update.effective_chat.id, text=results[0])

updater = Updater("<bot token>", use_context=True)
dispatcher = updater.dispatcher
bot = Bot("<bot token>")
print(bot.get_me())

def start(update: Updater, context: CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, text="I'm Up")


def message_handler(update: Updater, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(
        chat_id = chat_id,
        text = text,
        parse_mode = ParseMode.HTML
    )
start_handler = CommandHandler("start", start)
price_handler = CommandHandler("bit", price)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(price_handler)
updater.start_polling()
updater.idle()