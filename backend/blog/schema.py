import graphene
from graphene_django import DjangoObjectType
from blog import models, queries

schema = graphene.Schema(query=queries.Query)