from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = '6841571188:AAH1Q7U3uR_UiNtFqCkgo7HRZdTVUBYs67I'
Bot_USERNAME: Final = '@Test2222_IQ_Bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi... Welcome to the chat box of Rajesh.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi... What help do you need?')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# Responses
def handle_response(text: str) -> str:
    processed = text.lower()
    if 'hello' in processed:
        return 'Hello amazing person.'

    if 'how are you?' in processed:
        return 'I am fine thank you. Glad you asked. What about you?'

    if 'what can you do?' in processed:
        return 'I can answer questions, provide information, and engage in conversation.'

    if 'tell me a joke' in processed:
        return 'Why do a fanta can be fantastic but cocacola cannot be cocacolastic?'

    if 'i love you' in processed:
        return 'I love you too.'

    if 'what is your name?' in processed:
        return 'My name is Rajesh KC'

    if 'will you be my girlfriend?' in processed:
        return 'Sorry bro, I am a boy.'

    if 'will you be my boyfriend?' in processed:
        return 'Let me ask my mom first.'

    if 'how old are you?' in processed:
        return 'I am 26 years old.'

    if 'what is your favourite food?' in processed:
        return 'Its aloo fried.'

    if 'do you love coding?' in processed:
        return 'Yes, unless i encounter an error.'

    if 'are you a human?' in processed:
        return 'I am a cyborg.'

    if 'what is the capital of Nepal?' in processed:
        return 'Kathmandu'

    if 'do you have a girlfriend?' in processed:
        return 'I am ugly, so use your logic.'

    if 'what is life?' in processed:
        return 'Its a short journey.'

    if 'where do you live?' in processed:
        return 'I live in Nepal.'

    if 'what is the tallest mountain of world?' in processed:
        return 'Mount Everest.'

    if 'who is the most beautiful woman in this world?' in processed:
        return 'My mom.'

    if 'What is the best part of yourself?' in processed:
        return 'My simplicity..'

    if 'How is this world?' in processed:
        return 'This world is beautiful and amazing.'

    if 'Do read books??' in processed:
        return 'I rarely do nowadays but priorly i used to do it alot.'

    if 'Whats your hobby?' in processed:
        return 'I love singing.'

    if 'What is your favourite color?' in processed:
        return 'Its blue.'

    if 'Are you boring?' in processed:
        return 'Ofcourse i am.'

    if 'Thank you.' in processed:
        return 'Welcome.'

    return 'I am sorry, I am not updated to answer these questions yet.'


# Message handling
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text.lower()

    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type != 'group':
        response = handle_response(text)
        print('Bot:', response)
        await update.message.reply_text(response)


# Error handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(Token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)
