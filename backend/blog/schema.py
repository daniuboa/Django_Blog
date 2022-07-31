import graphene
from graphene_django import DjangoObjectType
from blog import models, queries

# Define type
class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )

schema = graphene.Schema(query=queries.Query)