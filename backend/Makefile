# Build options
IMAGE_NAME?="backend"
IMAGE_TAG?="alpha"

DOCKER_NO_CACHE?="false"

# Publish options
DOCKER_PUBLISH_NAME?="shmileee/backend"
DOCKER_PUBLISH_TAG?=$(IMAGE_TAG)

.PHONY: build
build:
	docker build -f Dockerfile --no-cache=$(DOCKER_NO_CACHE) \
	-t $(IMAGE_NAME):$(IMAGE_TAG) .

.PHONY: clean
clean: test-clean
	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: publish
publish:
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(DOCKER_PUBLISH_NAME):$(DOCKER_PUBLISH_TAG)
	docker push $(DOCKER_PUBLISH_NAME):$(DOCKER_PUBLISH_TAG)
