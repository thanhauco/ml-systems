import asyncio
import aiohttp

async def mirror_traffic(shadow_url: str, request_payload: dict):
    """
    Fire and forget shadow request.
    """
    try:
        async with aiohttp.ClientSession() as session:
            # Short timeout, we don't care about response
            await session.post(shadow_url, json=request_payload, timeout=0.1)
    except Exception:
        pass # Ignore failures

# Middleware usage:
# asyncio.create_task(mirror_traffic("http://v2-service/predict", req.json()))
