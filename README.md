# Flask-Template using completely GraphQL

Flask project template with user login and everything basics

This project contains only two models
- User Role Model
- User Model

This minimalistic so that this project can be used immediately and ready for whatever business logic you have.
All interactions are using GraphQL. Authorization is using Flask-JWT-Extended.

## Installation
Just clone it. You can rename the folder name to reflect your own project. 
Once installed there is a default role, which is Administrator, and administrator user that its name, email, and password can be defined in the .env file. Feel free to change these environment variables.

To build the project it will depend on the execution type but basically it is docker-compose-based project

## Execution Types
There are two execution types in this project:
- Development 
- Production

### Development Execution Type
For this type to build just run 

```bash
./build-dev.sh
```

This would build the project using docker-compose. Nothing is initially run once the built is finished. In other word no entrypoint no command.
Go to the flask container using this command

```bash
docker-compose exec flask bash
```
Once youa re in, run the development server by using this command

```bash
./init-dev.sh
```

It will initiate flask run based development server. By default, it will run behind nginx. This is so that you could also test the HTTPS functionality as well, which quite common. If you don't want it feel free to disable the nginx or exclude it completely for this execution type. 

For this type the flask service would be available on port 5000 just like flask's default port.

### Production Execution Type
This execution type is used if you already with you development stage. To build it run the following:

```bash
./build-dev.sh
```

This will build and run the flask application immediately one the built is finished. The service will be available at port 80.

### Batteries not included
The Database used is sqlite so if you want to change it feel free to change to what ever you want by modifying the sqlalchemy URL in base.py file.
Celery is also not included. In case you need to have asynchronous/background processor feel free to add celery.

## Endpoints
There is only one endpoint that is /graphql. All HTTP requests must be redirected here (including login).
Regarding all possible GraphQL request can be seen in the schema that is visible in the graphiql of this project.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
