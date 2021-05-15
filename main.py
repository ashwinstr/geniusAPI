import os
import aiohttp
import json
import lyricsgenius
from userge import userge, Message


genius = lyricsgenius.Genius("2_UkgCR50RbUHF9rQMwemGbAj0JCWKesi8RWwsW31kKGrIlWzCvd9G_lVajRSszQ")


@userge.on_message(
    filters.commands("glyrics")
)
async def g_lyrics(message: Message):
    name = "eminem higher"
    data = {"searchTerm": name}
    async with aiohttp.request(
        "POST",
        genius,
        headers={
            "content-type": "application/json",
        },
        data=json.dumps(data),
    ) as result:
        lyr = json.loads(result)
        return lyr
