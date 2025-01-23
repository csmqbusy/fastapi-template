from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from typing import AsyncGenerator


class DatabaseSessionManager:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10
    ):
        self.engine: AsyncEngine = create_async_engine(
                url=url,
                echo=echo,
                echo_pool=echo_pool,
                pool_size=pool_size,
                max_overflow=max_overflow
        )

        self.session_factory: async_sessionmaker[
            AsyncSession] = async_sessionmaker(
                bind=self.engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False
        )

    async def dispose(self) -> None:
        """Shutting down the engine and freeing up database resources."""
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Obtaining a session for executing queries in the database."""
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()
