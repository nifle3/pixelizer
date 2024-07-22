from asyncio import run


async def _main():
    import uvicorn

    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    run(_main)
