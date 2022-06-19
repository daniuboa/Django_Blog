import graphene
from graphene_django.types import DjangoObjectType
from blog import models
from blog import types

#schema = graphene.Schema(query=queries.Query)

# Define type
class Sitetype(DjangoObjectType):
    class Meta:
        model = models.Site

# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )