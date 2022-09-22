from typing import List

import strawberry
from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL


@strawberry.federation.type(keys=["id"])
class Book:
    id: strawberry.ID
    title: str
    a_field_that_will_be_overridden: str = strawberry.federation.field(
        default="this is coming from the books service", shareable=True
    )


def get_all_books() -> List[Book]:
    return [Book(id=strawberry.ID("1"), title="The Dark Tower")]


@strawberry.type
class Query:
    all_books: List[Book] = strawberry.field(resolver=get_all_books)


schema = strawberry.federation.Schema(query=Query, enable_federation_2=True)

app = Starlette(debug=True, routes=[Route("/", GraphQL(schema))])
