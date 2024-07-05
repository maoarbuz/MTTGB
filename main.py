import pandas as pd
import re
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def load_dialogues(file_path):
    dialogues = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            queries, responses = line.strip().split(';', 1)
            queries = queries.split(':')
            responses = responses.split(';')
            dialogues.append({'queries': queries, 'responses': responses})
    return pd.DataFrame(dialogues)

dialogues = load_dialogues('dialogues.txt')

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).strip().lower()

def find_response(user_message, dialogues):
    cleaned_message = clean_text(user_message)
    for index, row in dialogues.iterrows():
        cleaned_queries = [clean_text(q) for q in row['queries']]
        if cleaned_message in cleaned_queries:
            response = random.choice(row['responses'])
            return response
    return "Sorry, idk."

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi!')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = find_response(user_message, dialogues)
    await update.message.reply_text(response)

def main():
    application = Application.builder().token('YOUR_TOKEN').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
