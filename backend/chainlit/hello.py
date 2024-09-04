# This is a simple example of a chainlit app.

# from chainlit import AskUserMessage, Message, on_chat_start, oauth_callback
import chainlit as cl
from typing import Optional


@cl.on_chat_start
async def main():
    res = await cl.AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        await cl.Message(
            content=f"Your name is: {res['output']}.\nChainlit installation is working!\nYou can now start building your own chainlit apps!",
        ).send()


@cl.oauth_callback
async def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    db_ids = []

    # if settings.db_whitelist_enabled:
    #     db_ids = await provider.get_whitelisted_db_ids(
    #         {
    #             "provider_id": provider_id,
    #             "token": token,
    #             "raw_user_data": raw_user_data,
    #             "default_user": default_user,
    #         }
    #     )
    #
    # default_user.metadata.update({"db_ids": db_ids})
    return default_user
