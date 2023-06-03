build:
	docker build -f Dockerfile -t fastapi_test_app .

run:
	docker run --rm -p 8888:8888 fastapi_test_app
