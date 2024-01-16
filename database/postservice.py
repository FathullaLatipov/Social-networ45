from database.models import PostPhoto, UserPost
from database import get_db

# Получить все публикации
def get_all_posts():
    db = next(get_db())

    all_posts = db.query(UserPost).all()

    return all_posts

# Получить определенную публикацию -> смотря на userservice - >def get exact_post_db()
# Добавить публикацию -> смотря на userservice -> def add_new_post_db()
# Изменить текст к публикацию -> def edit_post_text_db(post_id, post_text)
# Удалить публикацию -> def delete_post_db()
# 50/50 Добавить лайк к публикации -> def like_post_db()
# Удаления лайка -> def unlike_post_db()