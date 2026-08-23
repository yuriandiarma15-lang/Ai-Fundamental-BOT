async def send_to_chat(
    bot,
    chat_id,
    text
):

    try:

        await bot.send_message(

            chat_id=chat_id,

            text=text,

            parse_mode="HTML",

            disable_web_page_preview=True

        )

        return True

    except Exception as e:

        print(
            "SEND ERROR:",
            e
        )

        return False
