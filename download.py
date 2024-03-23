import asyncio
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types import InputMessagesFilterPhotos, InputPhoto

# Your Telegram API credentials
api_id = '24313030'
api_hash = 'efad64d6ef06227bdb2734fc00eaaac3'

# Your phone number
phone_number = '+4792962828'

# Path to the directory where you want to save the photos
download_path = r'.\download\WesternHeritage'

# Initialize the Telegram client
client = TelegramClient('the_dogs', api_id, api_hash)

async def download_photos():
    await client.start(phone_number)
    print("Client created")

    # Fetch all albums from the group/channel
    async for message in client.iter_messages('https://t.me/WesternHeritage', filter=InputMessagesFilterPhotos):
        # Check if the message contains an album
        if hasattr(message, 'media') and hasattr(message.media, 'photo_album') and message.media.photo_album is not None:
            album_id = message.media.photo_album.id
            # Fetch photos from the album
            photos = await client(GetUserPhotosRequest(
                await client.get_input_entity('https://t.me/WesternHeritage'), 
                offset=0,
                max_id=0,
                limit=100,
                hash=0))
            
            # Download each photo in the album
            for photo in photos:
                await client.download_media(InputPhoto(id=photo.id, access_hash=photo.access_hash),
                                            file=download_path)
                print(f"Downloaded photo: {photo.id}.jpg")
                
                # Introduce a 3-second wait time before downloading the next photo
                await asyncio.sleep(2)
            
        else:
            # Download standalone photos
            await client.download_media(message.photo, file=download_path)
            print(f"Downloaded photo: {message.id}.jpg")
            
            # Introduce a 3-second wait time before downloading the next photo
            await asyncio.sleep(2)

asyncio.get_event_loop().run_until_complete(download_photos())


