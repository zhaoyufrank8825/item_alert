from flask import render_template, request, session, make_response, Blueprint
from models.post import Post
from models.blog import Blog
from models.user import User

blog_blueprint = Blueprint("blogs", __name__)

    
@blog_blueprint.route("/")
def blogs():
    user = User.find_by_email(session['email'])
    blogs = user.get_blogs()
    return render_template("blogs/index.html", blogs=blogs, user=user)

@blog_blueprint.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    if request.method == "GET":
        return render_template("blogs/new_blog.html")
    else:
        user=User.get_by_email(session['email'])
        title = request.form['title']
        description = request.form['description']
        blog = Blog(user.email, user.username, user._id, title, description)
        blog.save_to_mongo()
        return make_response(blogs())

@blog_blueprint.route("/<string:blog_id>/posts")
def posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()
    return render_template("posts.html", posts=posts, blog=blog)

@blog_blueprint.route("/<string:blog_id>/posts/new_post", methods=['GET', 'POST'])
def new_post(blog_id):
    if request.method == "GET":
        return render_template("new_post.html", blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        post = Post(blog_id, title, content, session['email'])
        post.save_to_mongo()
        return make_response(posts(blog_id))
