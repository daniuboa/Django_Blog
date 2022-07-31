import graphene
from blog import queries, mutations

# Define type


schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation)