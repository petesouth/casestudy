docker container stop case_db

sleep 5

docker system prune

docker rmi case_db


docker build -t case_db .


docker run  -d \
--publish 3306:3306 \
--name=case_db case_db 
