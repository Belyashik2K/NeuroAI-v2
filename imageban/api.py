import aiohttp
import json
import ssl
import certifi

from config import Config
from neuros import HTTPClient

class ImageBanAPI(HTTPClient):
    def __init__(self) -> None:
        super().__init__()
        self._method = "POST"
        self._ssl_context = ssl.create_default_context(cafile=certifi.where())
        self._connector = aiohttp.TCPConnector(ssl=self._ssl_context)
        self._session = aiohttp.ClientSession(connector=self._connector)

        self._URI = 'https://api.imageban.ru/v1'
        self._secret_key = Config.SECRET_KEY
        self._headers = {'Authorization': f'Bearer {self._secret_key}'}

    async def _request(self, method: str, uri: str, **kwargs) -> str:
        """Make request to ImageBan."""
        async with self._session.request(method, uri, **kwargs) as response:
            return await response.text()
            
    async def upload_image(self, image: str) -> str:
        """Upload image to ImageBan.
        
        Args:
            image (str): Image url.
            
        Returns:
            str: Image url on ImageBan."""
        uri = self._URI + '/upload'
        data = {'url': image}
        result = await self._request(self._method, uri, headers=self._headers, data=data)
        json_result = json.loads(result)
        return json_result['data']['link']

