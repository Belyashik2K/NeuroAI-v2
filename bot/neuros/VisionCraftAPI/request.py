import json

from aiohttp import ClientSession

from typing import Any, Optional

from .errors import VisionCraftError
from ..base_request import HTTPClient
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

    async def _upscale_request(self,
                               method: str,
                               neuro: str,
                               uri: str,
                               **kwargs) -> bytes:
        async with ClientSession() as session:
            async with session.request(method, uri, **kwargs) as response:
                await self._check_status_code(response.status, neuro, uri, kwargs)
                return await self._check_exception(result=await response.read(),
                                                   neuro=neuro,
                                                   uri=uri,
                                                   kwargs=kwargs)

    async def _check_status_code(self, 
                                 status_code: dict,
                                 neuro: str, 
                                 uri: str,
                                 kwargs: dict) -> None:
        if status_code != 200:
            await database.switch_neuro_status(neuro)
            raise VisionCraftError(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}")

    def _check_api_key(self, kwargs: dict) -> dict:
        ...

    async def _check_exception(self,
                                result: bytes,
                                neuro: str, 
                                uri: str,
                                kwargs: dict):
        if "code" in str(result):
            json_string = result.decode('utf-8')
            json_data = json.loads(json_string)
            if json_data[0]['code'] == 0:
                neuro = neuro.replace(data.Neuros.start, '')
                await database.switch_neuro_status(neuro)
                raise VisionCraftError(f"Error (message >>> {json_data[0]['message']}) while requesting {uri} with {kwargs}")
        return result