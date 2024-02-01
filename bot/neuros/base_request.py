from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Callable, Awaitable, Any


class HTTPClient(ABC):
    """Base class for HTTP clients."""
        
    if TYPE_CHECKING:
        _request: Callable[..., Awaitable[dict]]
        _voice_request: Callable[..., Awaitable[bytes]]
        _check_status_code: Callable[..., Awaitable[None]]
        _check_api_key: Callable[..., Awaitable[dict]]
    else:
        @abstractmethod
        async def _request(self, *args: Any, **kwargs: Any) -> dict:
            ...

        @abstractmethod
        async def _voice_request(self, *args: Any, **kwargs: Any) -> bytes:
            ...

        @abstractmethod
        async def _check_status_code(self, *args: Any, **kwargs: Any) -> None:
            ...

        @abstractmethod
        def _check_api_key(self, kwargs: dict) -> dict:
            ...