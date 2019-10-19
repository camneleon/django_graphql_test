import graphene
from graphene_django import DjangoObjectType


from .models import Person, Movie, CastMembers


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(graphene.ObjectType):
    movie = graphene.List(MovieType)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()
