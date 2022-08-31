publish:
	cd books && pdm run strawberry export-schema app > ../books.graphql
	cd reviews && pdm run strawberry export-schema app > ../reviews.graphql

	APOLLO_KEY=service:strawberry-federation:fsxTmw4aZJ4WEVhI1fdnnw \
		rover subgraph publish strawberry-federation@current \
		--name reviews --schema ./reviews.graphql \
		--routing-url http://reviews:4000/graphql

	APOLLO_KEY=service:strawberry-federation:fsxTmw4aZJ4WEVhI1fdnnw \
		rover subgraph publish strawberry-federation@current \
		--name books --schema ./books.graphql \
		--routing-url http://books:4000/graphql
