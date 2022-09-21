import graphene
from graphene_django import DjangoObjectType
from blog import models

# Define type
class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

# Define query
class Query(graphene.ObjectType):
    site = graphene.Field(SiteType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )