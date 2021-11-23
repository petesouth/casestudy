docker container stop casestudy

docker container rm casestudy 

docker rmi casestudy

docker images -a

docker container list

docker build -t casestudy .

docker run -d -v $(pwd)/.env:/.env -v $(pwd)/.env:/build/.env --publish 8080:8080 --name=casestudy casestudy
