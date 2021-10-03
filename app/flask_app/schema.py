import graphene

from .modules.role.schema import RoleQuery, RoleMutation
from .modules.user.schema import UserQuery, UserMutation

class Mutation(RoleMutation, UserMutation, graphene.ObjectType):
	pass

class Query(RoleQuery, UserQuery, graphene.ObjectType):
	node = graphene.relay.Node.Field()
	
schema = graphene.Schema(query=Query, mutation=Mutation)
