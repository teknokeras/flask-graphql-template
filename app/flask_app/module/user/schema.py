import graphene
from graphql import GraphQLError
from werkzeug.security import generate_password_hash, check_password_hash
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    current_user
) 

from .model import User as UserModel
from flask_app.base import db_session

from flask_app.module.role.model import Role as RoleModel

class User(SQLAlchemyObjectType):
	class Meta:
		model = UserModel
		interfaces = (graphene.relay.Node, )

class UserConn(graphene.relay.Connection):
	class Meta:
		node = User

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: User, description="User created by this mutation.")

    class Arguments:
        name = graphene.String(required=True)
        nick_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role_id = graphene.Int(required=True)
        
    @jwt_required
    def mutate(self, info, name, nick_name, email, password, role_id):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        role = RoleModel.query.get(role_id)

        if role is None:
            raise GraphQLError('Role with id {id} does not exists'.format(id=str(role_id)))

        existing_user = UserModel.query.filter_by(email=email).first()

        if existing_user is not None:
            raise GraphQLError('User with email {email} does not exists'.format(email=email))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        user = UserModel(email=email, name=name, nick_name=nick_name, password=hashed_password, role_id=role.id, role=role)
        db_session.add(user)
        db_session.commit()

        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    """Update a role."""
    user = graphene.Field(lambda: User, description="User updated by this mutation.")

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        nick_name = graphene.String(required=True)
        email = graphene.String(required=True)
        role_id = graphene.Int(required=True)

    @jwt_required
    def mutate(self, info, id, name, nick_name, email, role_id):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        role = RoleModel.query.get(role_id)

        if role is None:
            raise GraphQLError('Role with id {id} does not exists'.format(id=str(role_id)))

        user = UserModel.query.get(id)

        if user is None:
            raise GraphQLError('User does not exists')

        user.name = name
        user.nick_name = nick_name
        user.email = email
        user.role_id = role.id
        user.role = role

        db_session.commit()

        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    message = graphene.String()

    class Arguments:
    	id = graphene.Int(required=True)

    @jwt_required
    def mutate(self, info, name):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        user = UserModel.query.get(id)

        if user is None:
            raise GraphQLError('User does not exists')

        if current_user.id == user.id:
            raise GraphQLError('Cannot delete yourself')

        db_session.delete(user)
        db_session.commit()
        return DeleteRole(message="User {name} is deleted".format(name=user.name))

    
class LoginUser(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        user = UserModel.query.filter_by(email=email).first()

        if user is None:
            raise GraphQLError('Incorrect email and/or password')
        
        if not check_password_hash(user.password, password):
            raise GraphQLError('Incorrect email and/or password')

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return LoginUser(access_token=access_token, refresh_token=refresh_token)
	   

class UserMutation:
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()

class UserQuery:
	# Allows sorting over multiple columns, by default over the primary key
    all_users = graphene.List(User)
    user = graphene.relay.Node.Field(User)
    user_by_email = graphene.List(User, email=graphene.String())
    user_by_role_id = graphene.List(User, role_id=graphene.Int())

    @jwt_required
    def resolve_user_by_role_id(self, info, **args):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        role_id = args.get("role_id")

        user_query = User.get_query(info)

        users = user_query.filter_by(role_id=role_id).all()

        return users

    @jwt_required
    def resolve_all_users(self, info):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        user_query = User.get_query(info)

        users = user_query.all()

        return users

    @jwt_required
    def resolve_user_by_email(self, info, **args):
        if current_user.role.name != 'ADMINISTRATOR':
            raise GraphQLError('You are not authorized')

        name = args.get("email")

        user_query = User.get_query(info)

        users = user_query.filter_by(email=email).all()

        return users

