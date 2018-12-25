import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from module.department.schema import CreateDepartment, DepartmentQuery
from module.employee.schema import CreateEmployee, EmployeeQuery


class Mutation(CreateDepartment, CreateEmployee, graphene.ObjectType):
	pass

class Query(DepartmentQuery, EmployeeQuery, graphene.ObjectType):
	node = graphene.relay.Node.Field()
	


schema = graphene.Schema(query=Query, mutation=Mutation)