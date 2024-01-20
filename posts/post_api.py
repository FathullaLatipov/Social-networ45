from fastapi import APIRouter
from database.postservice import get_all_posts_db, get_exact_post_db

post_router = APIRouter(prefix='/post', tags=['Управления постами'])


@post_router.get('/all-posts')
async def all_posts():
    result = get_all_posts_db()
    return result

@post_router.get('/get-exact-post')
async def get_post(post_id):
    result = get_exact_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Not Found'}