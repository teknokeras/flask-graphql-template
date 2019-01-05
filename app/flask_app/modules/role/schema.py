import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_jwt_extended import jwt_required, current_user
from graphql import GraphQLError

from .model import Role as RoleModel
from flask_app.ext.database import db

from flask_app.applog import log

class Role(SQLAlchemyObjectType):
	class Meta:
		model = RoleModel
		interfaces = (graphene.relay.Node, )

class RoleConn(graphene.relay.Connection):
	class Meta:
		node = Role

class CreateRole(graphene.Mutation):
    role = graphene.Field(lambda: Role, description="Role created by this mutation.")

    class Arguments:
        name = graphene.String(required=True)

    @jwt_required
    def mutate(self, info, name):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        existing_role = RoleModel.query.filter_by(name=name).first()

        if existing_role is not None:
        	raise GraphQLError('Role with name {name} already exists'.format(name=name))

        role = RoleModel(name=name)
        db.session.add(role)
        db.session.commit()

        return CreateRole(role=role)

class UpdateRole(graphene.Mutation):
    """Update a role."""
    role = graphene.Field(lambda: Role, description="Role updated by this mutation.")

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    @jwt_required
    def mutate(self, info, id, name):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        existing_role = RoleModel.query.filter_by(name=name).first()

        if existing_role is not None:
        	raise GraphQLError('Role with name {name} already exists'.format(name=name))

        role = db.session.query(RoleModel).filter_by(id=id).first()

        if role is None:
        	raise GraphQLError('Role with id {id} does not exists'.format(id=str(id)))

        role.name = name
        db.session.commit()
        return UpdateRole(role=role)

class DeleteRole(graphene.Mutation):
    message = graphene.String()

    class Arguments:
    	id = graphene.Int(required=True)

    @jwt_required
    def mutate(self, info, id):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        role = RoleModel.query.get(id)

        if role is None:
            return DeleteRole(message="Role {id} doesn't exists".format(id=id))

        db.session.delete(role)
        db.session.commit()
        return DeleteRole(message="Role {name} is deleted".format(name=role.name))
	   

class RoleMutation:
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()

class RoleQuery:
	# Allows sorting over multiple columns, by default over the primary key
    all_roles = graphene.List(Role)

    role = graphene.relay.Node.Field(Role)

    role_by_name = graphene.List(Role, name=graphene.String())

    @jwt_required
    def resolve_all_roles(self, info, **args):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        name = args.get("name")
        role_query = Role.get_query(info)
        roles = role_query.all()
        return roles


    @jwt_required
    def resolve_role_by_name(self, info, **args):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        name = args.get("name")
        role_query = Role.get_query(info)
        role = role_query.filter_by(name=name).all()
        return role

