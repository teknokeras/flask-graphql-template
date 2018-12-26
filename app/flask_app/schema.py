import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .module.role.schema import RoleQuery, RoleMutation
from .module.user.schema import UserQuery, UserMutation


class Mutation(RoleMutation, UserMutation, graphene.ObjectType):
	pass

class Query(RoleQuery, UserQuery, graphene.ObjectType):
	node = graphene.relay.Node.Field()
	
schema = graphene.Schema(query=Query, mutation=Mutation)