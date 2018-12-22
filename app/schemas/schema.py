import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from database.base import db_session
from database.department import Department as DepartmentModel
from database.employee import Employee as EmployeeModel

class Department(SQLAlchemyObjectType):
	class Meta:
		model = DepartmentModel
		interfaces = (graphene.relay.Node, )

class DepartmentConn(graphene.relay.Connection):
	class Meta:
		node = Department

class Employee(SQLAlchemyObjectType):
	class Meta:
		model = EmployeeModel
		interfaces = (graphene.relay.Node, )

class EmployeeConn(graphene.relay.Connection):
	class Meta:
		node = Employee


class CreateDepartment(graphene.Mutation):
    department = graphene.Field(lambda: Department, description="Department created by this mutation.")

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        department = DepartmentModel(name=name)
        db_session.add(department)
        db_session.commit()

        return CreateDepartment(department=department)



class Mutation(graphene.ObjectType):
    create_department = CreateDepartment.Field()


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()
	# Disable sorting over this field
	all_departments = SQLAlchemyConnectionField(DepartmentConn, sort=None)
	# Allows sorting over multiple columns, by default over the primary key
	all_employees = SQLAlchemyConnectionField(EmployeeConn)

	department = graphene.relay.Node.Field(Department)

	employee = graphene.relay.Node.Field(Employee)

	employee_by_name = graphene.List(Employee, name=graphene.String())

	def resolve_employee_by_name(self, info, **args):
		name = args.get("name")

		employee_query = Employee.get_query(info)

		employees = employee_query.filter(EmployeeModel.name.contains(name)).all()

		return employees

class Mutation(graphene.ObjectType):
    createDepartment = CreateDepartment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)