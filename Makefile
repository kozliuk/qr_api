DIRS := qr_api
PORT ?= 8080

format:
	black $(DIRS)

lint:
	python -m flake8 qr_api --application-import-names qr_api --import-order-style pep8 --max-line-length 80 --isolated

style: format lint

local:
	uvicorn qr_api.app:app --reload --host 0.0.0.0 --port $(PORT)

deploy:
	gunicorn qr_api.app:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$(PORT)