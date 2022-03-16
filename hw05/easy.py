import sys
import asyncio
import aiohttp
import aiofiles


used_hashes = set()


async def save_image(dir, fname):
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get('https://thisartworkdoesnotexist.com/') as response:
                data = await response.read()
                h = hash(str(data))
                if h in used_hashes:
                    asyncio.sleep(0.2)
                    continue
                used_hashes.add(h)

                f = await aiofiles.open(dir + fname, mode='wb')
                await f.write(data)
                await f.close()
                print(f'image {fname} saved')
                break


async def main(count, dir):
    await asyncio.gather(*[save_image(dir, f'artwork_{i}.png') for i in range(count)])


if __name__ == '__main__':
    count = int(sys.argv[1])
    dir = sys.argv[2]

    asyncio.run(main(count, dir))
