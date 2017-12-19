import sys,orm,asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

    d = User(id='0015136657838087ed83c789bb14fc385e32f6deb73fd55000')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await d.remove()
    await u.save()
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
