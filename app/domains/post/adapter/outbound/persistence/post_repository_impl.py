from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.post.application.port.post_repository_port import PostRepositoryPort
from app.domains.post.domain.entity.post import Post
from app.domains.post.infrastructure.mapper.post_mapper import PostMapper


class PostRepositoryImpl(PostRepositoryPort):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, post: Post) -> Post:
        post_orm = PostMapper.to_orm(post)
        self._session.add(post_orm)
        self._session.commit()
        self._session.refresh(post_orm)
        return PostMapper.to_entity(post_orm)