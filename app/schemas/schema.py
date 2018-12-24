import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .schema_department import CreateDepartment, DepartmentQuery
from .schema_employee import CreateEmployee, EmployeeQuery


class Mutation(CreateDepartment, CreateEmployee, graphene.ObjectType):
	pass

class Query(DepartmentQuery, EmployeeQuery, graphene.ObjectType):
	node = graphene.relay.Node.Field()
	


schema = graphene.Schema(query=Query, mutation=Mutation)