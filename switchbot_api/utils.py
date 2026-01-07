"""util for  SwitchBot API."""
import aiohttp

from .exceptions import SwitchBotDeviceRequestError


async def get_file_stream_from_cloud(url: str, timeout:float=5) -> bytes:
    """get file stream from cloud."""
    # now only for download <AI Art Frame> Picture
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout) as response:
                if response.status != 200:
                    raise SwitchBotDeviceRequestError("get file stream error")
                file_stream = await response.read()
                return file_stream
    except Exception as e:
        raise SwitchBotDeviceRequestError(f"{e}")