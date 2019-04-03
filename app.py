import graphene
import json


class Query(graphene.ObjectType):
    # There are two way to get rid of the camelCase issue.
    # The way Num1 for get rid of the camelCase and snake_case issue is
    # Write inside the (Any constructor )
    # Here We have a Boolean Constructor
    # We can path name parameter inside the constructor.
    # Till instanse graphene.Boolean(name = 'is_staff')
    # For get rid of camelcase issue inside execute schema mehtod.
    is_staff = graphene.Boolean()

    def resolve_is_staff(self, info):
        return True


# Way 2 for get rid of the camelCase and snake_case issue
# We Write parameter auto_camelcase inside the graphene.Schema(!!!, auto_camelcase=False) Constructor
# for get rid of camelcase issue inside execute schema
schema = graphene.Schema(query=Query, auto_camelcase=False)
result = schema.execute(

    '''
    {
        is_staff #Here we write the query
    }
    '''

)
items = dict(result.data.items())

print(json.dumps(items, indent=4))  # Here we dumps our objects so we will have 4 space(indent)
