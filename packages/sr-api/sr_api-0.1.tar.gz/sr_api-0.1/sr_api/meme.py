import io

from sr_api.http import HTTPClient

class Meme:
    def __init__(self, http_client: HTTPClient, data):
        self.id = data['id']
        self.image = data['image']
        self.caption = data['caption']
        self.category = data['category']
        self._http_client = http_client


    async def read(self):
        return await self._http_client.get(self.url)

    async def save(self, fp, seek_start=True):
        data = await self.read()
        if isinstance(fp, io.IOBase) and fp.writable():
            written = fp.write(data)

            if seek_start:
                fp.seek(0)

            return written
        else:
            with open(fp, 'wb') as f:
                return f.write(data)
