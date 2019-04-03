import graphene
import json
from datetime import datetime


# Just User class with many fields member
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()


class Query(graphene.ObjectType):
    # Create list of users because we want to be able to resolve a list of users
    # first=graphene.Int() first 10 user or first 2 users
    users = graphene.List(User, first=graphene.Int())

    # We use this method for get list of users when the query ask for users
    def resolve_users(self, info,first):
        return [
            User(username='dawoode', last_login=datetime.now()),
            User(username='ahmad', last_login=datetime.now()),
            User(username='omar', last_login=datetime.now())
        ][:first]

# We Write auto_camelcase for get rid of camelcase inside execute schema
schema = graphene.Schema(query=Query, auto_camelcase=False)
result = schema.execute(

    '''
    {
        users (first: 2){
            id
            username
            last_login
            }
    }
    '''

)
items = dict(result.data.items())

print(json.dumps(items, indent=4))  # space = indent
