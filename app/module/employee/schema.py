import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .model import Employee as EmployeeModel

class Employee(SQLAlchemyObjectType):
	class Meta:
		model = EmployeeModel
		interfaces = (graphene.relay.Node, )

class EmployeeConn(graphene.relay.Connection):
	class Meta:
		node = Employee

class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(lambda: Employee, description="Employee created by this mutation.")

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        department = DepartmentModel(name=name)
        db_session.add(department)
        db_session.commit()

        return CreateDepartment(department=department)

class EmployeeMutation:
    create_employee = CreateEmployee.Field()

class EmployeeQuery:
	# Allows sorting over multiple columns, by default over the primary key
	all_employees = SQLAlchemyConnectionField(EmployeeConn)

	employee = graphene.relay.Node.Field(Employee)

	employee_by_name = graphene.List(Employee, name=graphene.String())

	def resolve_employee_by_name(self, info, **args):
		name = args.get("name")

		employee_query = Employee.get_query(info)

		employees = employee_query.filter(EmployeeModel.name.contains(name)).all()

		return employees

