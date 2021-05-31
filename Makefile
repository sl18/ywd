# General docker manipulations and make tools:

help:	# Self-gen pseudo-help:
	@echo "\nYou can use this commands:\n"
	@egrep '^[^ ]*:\s+#' Makefile

status:	# Display container status
	@docker ps

list:	# List current created containers and images:
	@echo "== Containers: =="
	@docker ps -as --format "{{.ID}}: {{.Image}}\t{{.Names}}"
	@echo "\n== Images: =="
	@docker images

clean:	# Clean up some build trash
	@echo Cleaning containers:
	@if test "`docker ps -aq`" != ""; then echo "Cleaning up containers:"; docker rm `docker ps -aq` ; fi
	@echo Cleaning images:
	@if test "`docker images -f dangling=true -q`" != ""; then echo "Cleaning up dangling volumes:"; docker rmi `docker images -f dangling=true -q` ; fi

IMAGE_NAME=tt-yw


build:	# Build docker image $(IMAGE_NAME)
	@docker build --rm -f Dockerfile -t $(IMAGE_NAME) .


run:	# Start Python docker image
	@docker run -it --rm -p 8000:8000 $(IMAGE_NAME) /bin/bash -c \
		"cd /home/testuser/tt-yw/; \
		 FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=8000 \
		 FLASK_ENV=development FLASK_DEBUG=0 \
		 FLASK_APP=ya_weather/__init__.py python3 -m flask run --reload"

shell-root:          # Run an interactive shell as root
	@docker run -it --rm -p 3000:3000 -u 0 $(IMAGE_DEV) /bin/bash