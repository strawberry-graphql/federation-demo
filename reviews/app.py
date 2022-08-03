from typing import List, Optional

import strawberry
from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL


@strawberry.type
class Review:
    id: int
    body: str


def get_reviews(root: "Book") -> List[Review]:
    return [
        Review(id=id_, body=f"A review for {root.id}")
        for id_ in range(root.reviews_count)
    ]


@strawberry.federation.type(keys=["id"])
class Book:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews_count: int
    reviews: List[Review] = strawberry.field(resolver=get_reviews)
    hidden_field: str = strawberry.federation.field(inaccessible=True)
    a_field_that_will_be_overridden: str = strawberry.federation.field(
        override="Books",
        shareable=True,
        default="this is coming from the reviews service",
    )

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return Book(id=id, reviews_count=3, hidden_field="hidden")


@strawberry.type
class Query:
    _service: Optional[str]


schema = strawberry.federation.Schema(query=Query, types=[Book])

app = Starlette(debug=True, routes=[Route("/graphql", GraphQL(schema))])
