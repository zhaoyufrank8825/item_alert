from flask import render_template, request, session, make_response, Blueprint, redirect, url_for
from models.post import Post
from models.blog import Blog
from models.user import User
from models.user import require_login

blog_blueprint = Blueprint("blogs", __name__)

    
@blog_blueprint.route("/")
def index():
    users = User.all()
    blogs = []
    for user in users:
        user_blogs = user.get_blogs()
        blogs.extend(user_blogs)
    return render_template("blogs/index.html", blogs=blogs, user=user)

@blog_blueprint.route("/new_blog", methods=["GET", "POST"])
@require_login
def new_blog():
    if request.method == "GET":
        return render_template("blogs/new_blog.html")
    else:
        user=User.get_by_email(session['email'])
        title = request.form['title']
        description = request.form['description']
        img = request.form['img']
        blog = Blog(user.email, user.username, user._id, title, description, img)
        blog.save_to_mongo()
        return make_response(index())

@blog_blueprint.route("/edit/<string:blog_id>", methods=['GET', 'POST'])
@require_login
def edit_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if request.method == 'POST':
        blog.title = request.form['title']
        blog.description = request.form['description']
        blog.img = request.form['img']
        blog.save_to_mongo()
        return redirect(url_for(".index"))
    return render_template("blogs/edit_blog.html", blog=blog)

@blog_blueprint.route("/remove/<string:blog_id>")
@require_login
def remove_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if blog.email == session['email']:
        blog.remove_from_mongo()
    return redirect(url_for(".index"))

@blog_blueprint.route("/<string:blog_id>/posts")
def posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()
    return render_template("posts/index.html", posts=posts, blog=blog)

@blog_blueprint.route("/<string:blog_id>/posts/new_post", methods=['GET', 'POST'])
@require_login
def new_post(blog_id):
    blog = Blog.get_by_id(blog_id)
    if request.method == "GET":
        return render_template("posts/new_post.html", blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        img = request.form['img']
        post = Post(blog_id, title, content, blog.author, img)
        post.save_to_mongo()
        return make_response(posts(blog_id))

@blog_blueprint.route("/<string:blog_id>/posts/edit/<string:post_id>", methods=['GET', 'POST'])
@require_login
def edit_post(blog_id, post_id):
    post = Post.get_by_id(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.img = request.form['img']
        post.save_to_mongo()
        return redirect(url_for(".posts", blog_id = blog_id))

    return render_template("posts/edit_post.html", post=post)

@blog_blueprint.route("/<string:blog_id>/posts/remove/<string:post_id>")
@require_login
def remove_post(blog_id, post_id):
    blog = Blog.get_by_id(blog_id)
    if blog.email == session['email']:
        post = Post.get_by_id(post_id)
        post.remove_from_mongo()
    return redirect(url_for(".posts", blog_id = blog_id))


@blog_blueprint.route("/<string:blog_id>/posts/show/<string:post_id>")
def show_post(blog_id, post_id):
    blog = Blog.get_by_id(blog_id)
    post = Post.get_by_id(post_id)
    return render_template("posts/show.html", post=post, blog=blog)

