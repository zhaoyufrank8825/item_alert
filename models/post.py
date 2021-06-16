import uuid, datetime
from models.model import Model
from dataclasses import dataclass, field


@dataclass
class Post(Model):
    collection: str = field(init=False, default="posts")
    blog_id: str
    title: str
    content: str
    author: str
    date: str = field(default_factory=lambda: datetime.datetime.utcnow() )
    _id: str = field(default_factory=lambda: uuid.uuid4().hex )


    def json(self):
        return {
            "_id": self._id,
            "blog_id": self.blog_id,
            "title": self.title,
            "author": self.author,
            "content": self.content,
            "date": self.date
        }

    @classmethod
    def from_mongo(cls, id):
        return cls.find_one_by('_id', id)

    @classmethod
    def from_blog(cls, id):
        return cls.find_many_by("blog_id", id)
