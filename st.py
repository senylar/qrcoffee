from DataBase.models.models import Users
from DataBase.core import get_db

u = Users(telegram_id=123456789, name="John Doe", phone="+1234567890", email="s@s.com")

async def main():

    async with get_db() as session:
        await u.add(session)
        print("User added:", u)

        fetched_user = await Users.get_by_id(session, u.id)
        print("Fetched User:", fetched_user)

        all_users = await Users.get_all(session)
        print("All Users:", all_users)

import asyncio

asyncio.run(main())