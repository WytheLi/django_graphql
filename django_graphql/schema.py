# -*- coding: utf-8 -*-
# 总的schema入口

import graphene
import graphql_jwt

import book.schema
import account.schema
import blog.schema

class Query(
    blog.schema.Query,
    account.schema.Query,
    book.schema.Query,
    graphene.ObjectType
):
    # 总的Schema的query入口
    pass

class Mutations(graphene.ObjectType):
    # 总的Schema的mutations入口
    create_book = book.schema.CreateBook.Field()

    create_user = account.schema.CreateUser.Field(description='创建博客用户')
    create_blog = blog.schema.CreateBlog.Field(description='创建博客文章')

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)