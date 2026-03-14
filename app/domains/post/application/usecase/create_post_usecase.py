from app.domains.post.application.port.post_repository_port import PostRepositoryPort
from app.domains.post.application.request.create_post_request import CreatePostRequest
from app.domains.post.application.response.create_post_response import CreatePostResponse
from app.domains.post.domain.entity.post import Post


class CreatePostUseCase:
    def __init__(self, post_repository: PostRepositoryPort):
        self._post_repository = post_repository

    async def execute(self, request: CreatePostRequest) -> CreatePostResponse:
        post = Post(title=request.title, content=request.content)
        saved_post = await self._post_repository.save(post)
        return CreatePostResponse(id=saved_post.id, created_at=saved_post.created_at)