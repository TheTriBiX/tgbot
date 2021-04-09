# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    print(update.message)
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    txt = update.message.text
    if txt.lower() in ['привет', 'hello']:
        update.message.reply_text(f'ПРИВЕТ, {update.message["chat"]["first_name"]}!!!')
    else:
        update.message.reply_text(txt)


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


# def wikip(update, context):
#     search = ' '.join(context.args).strip()
#     result = search_wiki(search)
#     if search.lower() == 'бипки':
#         update.message.reply_text('потом расскажу')
#     elif result:
#         update.message.reply_text(result)
#     else:
#         update.message.reply_text('какая жалость я ничего не нашел(')


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)
    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


TOKEN = '1547371893:AAFmal4URfbdLvrd4pnLTTWXjJwyg8skvig'

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
