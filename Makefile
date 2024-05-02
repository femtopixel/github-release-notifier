VERSION ?= 0.4.5
CACHE ?= --no-cache=1

.PHONY: docker build-docker publish-docker
test: install check
	twine upload -r testpypi dist/*
publish: install check
	twine upload dist/*
install: clean
	sudo python3 setup.py sdist
check:
	twine check dist/*
build:
	mkdir -p build
dist:
	mkdir -p dist
clean: build dist
	sudo rm -Rf build/*
	sudo rm -Rf dist/*

docker: build-docker publish-docker
build-docker:
	docker buildx build --platform linux/arm/v7,linux/arm64/v8,linux/amd64,linux/arm/v6,linux/386 ${PUSH} --build-arg VERSION=${VERSION} --tag femtopixel/github-release-notifier --tag femtopixel/github-release-notifier:${VERSION} ${CACHE} .
publish-docker:
	PUSH=--push CACHE= make build-docker

