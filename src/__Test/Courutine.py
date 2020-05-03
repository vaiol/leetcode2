import asyncio


async def countdown35(tag: str, count: int) -> str:
    while count > 0:
        print('T-minus {} ({})'.format(count, tag))
        await asyncio.sleep(1)
        count -= 1
    return "Blastoff!"
asyncio.run(countdown35("Like", 350))