 - Build Docker image
docker build -t hostile-tweets-ex .

- Run Docker container
docker run -d -p 8000:8000 --name hostile-tweets-container hostile-tweets-ex

- Validate
docker ps

- Enter in browser
http://localhost:8000/tweets

