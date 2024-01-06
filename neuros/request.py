import aiohttp

from database import database as db
from texts import IB, ET

from .errors import *

class HTTPClient:
    """Base class for HTTP clients."""

    def __init__(self) -> None:
        self._method = "POST"
        self._URI = 'https://api.futureforge.dev/'
        # This is not a good idea, but context manager is not working on VDS/VPS.
        self._session = aiohttp.ClientSession()
        
    async def _request(self, 
                       neuro: str,
                       method: str, 
                       uri: str, 
                       **kwargs) -> dict:
        """Make request to URL.
        
        Args:
            method (str): HTTP method.
            uri (str): URL.
            **kwargs: Optional arguments.

        Returns:
            dict: Response from URL."""
        async with self._session.request(method, uri, **kwargs) as response:
            await self._check_status_code(response.status, neuro, uri, kwargs)
            return await response.json()
        
    async def _voice_request(self, 
                             neuro: str,
                             method: str, 
                             uri: str, 
                             **kwargs) -> dict:
        """Make request to URL, but for voice neuros."""
        async with self._session.request(method, uri, **kwargs) as response:
            await self._check_status_code(response.status, neuro, uri, kwargs)
            return await response.content.read()
        
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
            neuro = neuro.replace(IB.Callback.Neuros.start, '')
            await db.switch_neuro_status(neuro)
            raise FutureForgeError(ET.error_future_forge.format(f"Error (status code >>> {status_code}) while requesting {uri} with {kwargs}"))
