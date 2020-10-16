import graphene
from graphene_django.types import DjangoObjectType

from .models import User, Blog


# Output Type约束
class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


# 定义动作约束输入类型
# Input Type约束
class BlogInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    user = graphene.String(required=True)
    content = graphene.String(required=True)


# 定义一个创建blog的mutation
class CreateBlog(graphene.Mutation):
    class Arguments:
        blog_data = BlogInput(required=True)

    blog = graphene.Field(BlogType)

    def mutate(self, info, blog_data):
        blog = Blog.objects.create(title=blog_data['title'], user_id=blog_data['user'], content=blog_data['content'])
        return CreateBlog(blog=blog)


# 定义一个查询语句
class Query(object):


    all_blog = graphene.List(BlogType)


    def resolve_all_blog(self, info, **kwargs):
        return Blog.objects.select_related('user').all()




