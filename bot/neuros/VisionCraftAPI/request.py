import json

from aiohttp import ClientSession

from typing import Any, Optional

from .errors import VisionCraftError
from ..base_request import HTTPClient


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
            from ...database import database
            await database.switch_neuro_status(neuro)
            raise VisionCraftError(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}")

    def _check_api_key(self, kwargs: dict) -> dict:
        ...