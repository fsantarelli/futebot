import logging as puts
import random

from service import roll_service
from util.helpers import (
    get_json_fields_from_url,
    RANDOM_EXCEPTION_COMEBACKS as rec,
)

from .config import CHARADA_ENDPOINT
from .utils import bot


@bot.command()
async def charada(ctx):
    fields = get_json_fields_from_url(
        CHARADA_ENDPOINT,
        "pergunta",
        "resposta",
    )
    for field in fields:
        await ctx.send(field)


@bot.command()
async def roll(ctx, arg):
    try:
        response = roll_service.roll(arg)
        await ctx.send(response)
    except Exception as e:
        puts.info(e)
        await ctx.send(rec[random.randrange(0, len(rec) - 1)])