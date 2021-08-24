from typing import List

import strawberry
from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL


@strawberry.federation.type(keys=["id"])
class Book:
    id: strawberry.ID
    title: str


def get_all_books() -> List[Book]:
    return [Book(id=1, title="The Dark Tower")]


@strawberry.type
class Query:
    all_books: List[Book] = strawberry.field(resolver=get_all_books)


schema = strawberry.federation.Schema(query=Query)

app = Starlette(debug=True, routes=[Route("/graphql", GraphQL(schema))])
