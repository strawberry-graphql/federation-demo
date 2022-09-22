ifneq (,$(wildcard ./.env))
    include .env
    export
endif

publish:
	# todo: maybe run these via docker-compose
	cd books && pdm export-schema > ../books.graphql
	cd reviews && pdm export-schema > ../reviews.graphql

	rover subgraph publish $(APOLLO_GRAPH_REF) \
		--name reviews --schema ./reviews.graphql \
		--routing-url http://reviews:4000

	rover subgraph publish $(APOLLO_GRAPH_REF) \
		--name books --schema ./books.graphql \
		--routing-url http://books:4000
