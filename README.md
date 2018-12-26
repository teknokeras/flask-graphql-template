# flask-template
Flask project template with user login and everything basics

This project contains only two models
- User Role Model
- User Model

This minimalistic so that this project can be used immediately and ready for whatever business logic you have.
All interactions are using GraphQL.

## Installation
Just clone it. You can rename the folder name to reflect your own project. 
Once installed there is a default role, which is Administrator, and administrator user that its name, email, and password can be defined in the .env file. Feel free to change these environment variables.

## Endpoints
There is only one endpotin that is /graphql. All HTTP requests must be redirected here (including login).
Regarding all possible GraphQL request can be seen in the schema that is visible in the graphiql of this project.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
