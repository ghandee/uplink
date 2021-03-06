"""
This package defines an adapter for consuming requests built
by Uplink's high-level, declarative API with existing HTTP clients
(`requests`, `asyncio`, etc.).

We refer to this layer as the backend, as these adapters handle the
actual client behavior (i.e., making a request to a server), and
thus, we refer to this layer as the backend.

Note:
    At some point, we may want to expose this layer to the user, so
    they can create custom adapters.
"""
from uplink.clients.requests_ import Requests
from uplink.clients.twisted_ import Twisted

try:
    from uplink.clients.aiohttp_ import Aiohttp
except (SyntaxError, ImportError) as error:  # pragma: no cover
    from uplink.clients import interfaces

    class Aiohttp(interfaces.HttpClientAdapter):
        error_message = str(error)

        def __init__(self, *args, **kwargs):
            pass

        def create_request(self):
            raise NotImplementedError(
                "Failed to load `asyncio` client: %s" % self.error_message
            )

__all__ = [
    "Requests",
    "Aiohttp",
    "Twisted",
]

DEFAULT_CLIENT = Requests
