# bot.answer_callback_query(call.id, text="Дата выбрана")



@bot.message_handler(content_types = BOT.util.content_type_media)
def AllTransfer(message):
    bot.forward_message(message.user.id, message.chat.id, message.message_id)