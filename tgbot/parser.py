from config import KEY
import aiohttp
import json

key = KEY


async def get_weather(city: str):
    global API_KEY
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=True)) as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no') as response:
            return json.loads(await response.text())