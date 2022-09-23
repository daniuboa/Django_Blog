import graphene
from graphene_django import DjangoObjectType
from blog import queries, mutations

schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation)