import graphene
from graphene_django import DjangoObjectType
from blog import models, queries

# Define type
class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

class Query(graphene.ObjectType):
    site = graphene.Field(SiteType)

    def resolve_site(self, info):
        return (
            models.Site.objects.get()
        )

schema = graphene.Schema(query=queries.Query)
