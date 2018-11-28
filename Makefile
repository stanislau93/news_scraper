.PHONY: all build run clean

DOCKER_IMAGE_NAME = news_crawler

all: build run

build:
	@docker image build -t ${DOCKER_IMAGE_NAME} .

run:
	@docker run ${DOCKER_IMAGE_NAME}

clean:
	# remove all containers based on the image and then (providing all containers were stopped before) the image itself
	@docker ps -a | awk '{ print $$1,$$2 }' | grep ${DOCKER_IMAGE_NAME} | awk '{ print $$1 }' | xargs docker rm && docker rmi ${DOCKER_IMAGE_NAME}
