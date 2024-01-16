from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)

    reg_date = Column(DateTime)


# Таблица публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(String)
    likes = Column(Integer, default=0)

    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


# Таблица фотографий к определенному посту
class PostPhoto(Base):
    __tablename__ = 'post_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')


# Таблица комментарий
class PostComment(Base):
    __tablename__ = 'post_comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)

    post_id = Column(Integer, ForeignKey("user_posts.post_id"))
    user_id = Column(Integer, ForeignKey("users_user_id"))

    comment_text = Column(String)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')
