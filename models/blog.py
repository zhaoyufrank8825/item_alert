import datetime, uuid
from models.post import Post
from models.model import Model
from dataclasses import dataclass, field


@dataclass
class Blog(Model):
    collection: str = field(init=False, default="blogs")
    email: str
    author: str
    author_id: str
    title: float
    description: str
    img: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex )
    
    def new_post(self, title, content):
        post = Post(blog_id = self._id, 
                    title=title, 
                    content=content, 
                    author=self.author, 
                    img=self.img,
                    date=datetime.datetime.utcnow())
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "author_id": self.author_id,
            "_id": self._id,
            "email": self.email,
            "img": self.img
        }
    
    @classmethod
    def from_mongo(cls, id):
        return cls.find_one_by("_id", id)

    @classmethod
    def find_by_author_id(cls, id):
        return cls.find_many_by("author_id", id)

    

