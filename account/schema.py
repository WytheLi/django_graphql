from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


# Output Type约束
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

        exclude_fields = ['password', 'is_active']



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    msg = graphene.String()

    class Arguments:
        # Input Type约束
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String()
        gender = graphene.String()

    def mutate(self, info, **kwargs):
        User = get_user_model()
        user = User(
            username=kwargs['username'],
            email=kwargs.get('email', ''),
            gender=kwargs.get('gender', '')
        )
        user.set_password(kwargs['password'])
        user.save()
        return CreateUser(user=user, msg='用户创建成功！')


class Query(graphene.ObjectType):
    # 精准查询单条记录(主键或者唯一约束的字段)
    user = graphene.Field(UserType, id=graphene.Int())
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        # TODO 管理员权限
        return get_user_model().objects.filter(is_active=True)

    def resolve_me(self, info):
        user = info.context.user
        print(user, user.is_anonymous, user.is_authenticated)
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

    def resolve_user(self, info, **kwargs):
        # TODO 管理员权限
        # 精准查找，只适用于查询单条记录
        id = kwargs.get('id')

        if id:
            return get_user_model().objects.get(id=id)
