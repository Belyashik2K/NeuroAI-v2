from aiohttp import ClientSession

from ..database import database
from ..config import config

from ..keyboards.inline.callback import Callback

from .errors import *

class HTTPClient:
    """Base class for HTTP clients."""

    def __init__(self) -> None:
        self._URI = 'https://api.futureforge.dev/'
        
    async def _request(self, 
                       method: str,
                       neuro: str, 
                       uri: str, 
                       **kwargs) -> dict:
        """Make request to URL.
        
        Args:
            method (str): HTTP method.
            neuro (str): Neuro name.
            uri (str): URL.
            **kwargs: Optional arguments.

        Returns:
            dict: Response from URL."""
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
        """Make request to URL, but for voice neuros.
        
        Args:
            neuro (str): Neuro name.
            uri (str): URL.
            **kwargs: Optional arguments.
        
        Returns:
            bytes: Response from URL."""
        kwargs = self._check_api_key(kwargs)
        async with ClientSession() as session:
            async with session.request(method, uri, **kwargs) as response:
                await self._check_status_code(response.status, neuro, uri, kwargs)
                return await response.read()
        
    async def _check_status_code(self, 
                                status_code: dict,
                                neuro: str, 
                                uri: str,
                                kwargs: dict) -> None:
        """Check status code.
        
        Args:
            status_code (dict): Status code.
            neuro (str): Neuro name.
            uri (str): URL.
            **kwargs: Optional arguments.
        Raises:
            FutureForgeError: If status code is not 200."""
        if status_code != 200:
            neuro = neuro.replace(Callback.Neuros.start, '')
            await database.switch_neuro_status(neuro)
            raise FutureForgeError(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}")
    
    def _check_api_key(self,
                       kwargs: dict) -> dict:
        """Check API key.

        Args:
            kwargs (dict): Optional arguments.

        Returns:
            dict: Optional arguments with API key."""
        try:
            kwargs['params']['apikey'] = config.FUTURE_FORGE_API_KEY.get_secret_value()
        except KeyError:
            kwargs['params'] = {'apikey': config.FUTURE_FORGE_API_KEY.get_secret_value()}
        return kwargs