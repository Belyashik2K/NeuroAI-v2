from aiohttp import ClientSession

from typing import Any, Optional

from .errors import VisionCraftError
from ..base_request import HTTPClient
from ...config import config
from ...database import database
from ...keyboards import data


class VisionCraftRequest(HTTPClient):
    def __init__(self) -> None:
        super().__init__()

    async def _request(self,
                       neuro: str,
                       uri: str,
                       method: Optional[str] = "POST",
                       **kwargs):
        async with ClientSession() as session:
            async with session.request(method, uri, **kwargs) as response:
                await self._check_status_code(response.status, neuro, uri, kwargs)
                return await response.json()

    async def _voice_request(self, *args: Any, **kwargs: Any) -> bytes:
        ...

    async def _check_status_code(self, 
                                 status_code: dict,
                                 neuro: str, 
                                 uri: str,
                                 kwargs: dict) -> None:
        if status_code != 200:
            neuro = neuro.replace(data.Neuros.start, '')
            await database.switch_neuro_status(neuro)
            raise VisionCraftError(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}")

    def _check_api_key(self, kwargs: dict) -> dict:
        ...
    
    