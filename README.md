# API server for generation QR codes
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/qr' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "<YOUR_TEXT_OR_LINK>"
}'
```

## To run
```bash
docker-compose build 
docker-compose up dev
# or
docker-compose up prod
```

## To format && lint
```bash
docker-compose run style
```