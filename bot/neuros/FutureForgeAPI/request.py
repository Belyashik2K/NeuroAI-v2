from aiohttp import ClientSession

from typing import Optional

from .errors import FutureForgeError
from ..base_request import HTTPClient
from ...config import config


class FutureForgeRequest(HTTPClient):
    def __init__(self) -> None:
        super().__init__()

    async def _request(self,
                       neuro: str,
                       uri: str,
                       method: Optional[str] = "POST",
                       **kwargs):
        kwargs = self._check_api_key(kwargs)
        async with ClientSession() as session:
            async with session.request(method, uri, **kwargs) as response:
                await self._check_status_code(response.status, neuro, uri, kwargs)
                return await response.json()

    async def _voice_request(self,
                             method: str,
                             neuro: str,
                             uri: str,
                             **kwargs) -> bytes:
        kwargs = self._check_api_key(kwargs)
        async with ClientSession() as session:
            async with session.request(method, uri, **kwargs) as response:
                await self._check_status_code(response.status, neuro, uri, kwargs)
                return await response.read()

    async def _check_status_code(self,
                                 status_code: int,
                                 neuro: str,
                                 uri: str,
                                 kwargs: dict) -> None:
        if status_code != 200:
            from ...database import database
            await database.switch_neuro_status(neuro)
            raise FutureForgeError(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}")

    def _check_api_key(self, kwargs: dict) -> dict:
        try:
            kwargs['params']['apikey'] = config.FUTURE_FORGE_API_KEY.get_secret_value()
        except KeyError:
            kwargs['params'] = {'apikey': config.FUTURE_FORGE_API_KEY.get_secret_value()}
        return kwargs
