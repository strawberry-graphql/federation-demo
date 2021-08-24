from typing import List, Optional

import strawberry
from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL


@strawberry.type
class Review:
    body: str


def get_reviews() -> List[Review]:
    return [Review(body="This is a review")]


@strawberry.federation.type(extend=True, keys=["id"])
class Book:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews: List[Review] = strawberry.field(resolver=get_reviews)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return Book(id)


@strawberry.type
class Query:
    _service: Optional[str]


schema = strawberry.federation.Schema(query=Query, types=[Book])

app = Starlette(debug=True, routes=[Route("/graphql", GraphQL(schema))])
