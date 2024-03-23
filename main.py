import os
os.environ['OPENAI_API_KEY'] = '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'


from openai import AsyncOpenAI

import chainlit as cl

client = AsyncOpenAI(api_key= os.getenv('OPENAI_API_KEY'))

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    # ... more settings
}

@cl.on_message
async def on_message(message: cl.Message):
    print(message)
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot",
                "role": "system"
            },
            {
                "content": f'{message.content}',
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
