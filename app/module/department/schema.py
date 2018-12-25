import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .model import Department as DepartmentModel


class Department(SQLAlchemyObjectType):
	class Meta:
		model = DepartmentModel
		interfaces = (graphene.relay.Node, )

class DepartmentConn(graphene.relay.Connection):
    class Meta:
        node = Department

class CreateDepartment(graphene.Mutation):
    department = graphene.Field(lambda: Department, description="Department created by this mutation.")

    class Arguments:
        name = graphene.String()

    @classmethod
    def mutate(self, info, name):
        department = DepartmentModel(name=name)
        db_session.add(department)
        db_session.commit()

        return CreateDepartment(department=department)

class DepartmentMutation:
    create_department = CreateDepartment.Field()


class DepartmentQuery(graphene.ObjectType):

    all_departments = SQLAlchemyConnectionField(DepartmentConn)

    department = graphene.relay.Node.Field(Department)
