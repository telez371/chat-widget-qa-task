# test-automation

## Install Pre-Commits

```shell
pre-commit install
```

# Run
```shell
docker build -t chat-widget-qa-task/base -f api.Dockerfile .
```

```shell
docker run -it -v $(pwd):/app -w /app chat-widget-qa-task/base:latest poetry add [name-libs]
```

```shell
docker run -it -v $(pwd):/app -w /app chat-widget-qa-task/base:latest poetry update --lock
```

## Update requirements.txt

```shell
docker run -it -v $(pwd):/app -w /app chat-widget-qa-task/base:latest poetry export --without-hashes --with e2e -o requirements.e2e.txt
```
## Update requirements.api.txt
```shell
docker run -it -v $(pwd):/app -w /app chat-widget-qa-task/base:latest poetry export --without-hashes --with api -o requirements.api.txt
```


## Run server
```shell
docker-compose up --build
```
