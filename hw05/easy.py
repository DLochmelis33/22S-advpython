import sys
import asyncio
import aiohttp
import aiofiles


async def save_image(dir, fname):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://thisartworkdoesnotexist.com/') as response:
            f = await aiofiles.open(dir + fname, mode='wb')
            await f.write(await response.read())
            await f.close()


async def main(count, dir):
    # gather не работает, потому что изображение обновляется раз в секунду (проверил в браузере)
    # и если скачать их быстро подряд, то все получаются одинаковые
    # (есть шанс, что одно будет другое, если начать в конце текущей секунды)

    # без конкурентного выполнения теряется смысл, но увы :(

    # вместо await asyncio.gather(*[save_image(dir, f'artwork_{i}.png') for i in range(count)])
    for i in range(count):
        await save_image(dir, f'artwork_{i}.png')
        print(f'image {i} saved')
        await asyncio.sleep(1)


if __name__ == '__main__':
    count = int(sys.argv[1])
    dir = sys.argv[2]

    asyncio.run(main(count, dir))
