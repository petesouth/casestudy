## Pull the mysql:5.7 image
FROM mysql:5.7

## The maintainer name and email
MAINTAINER Your Name pete@issarainstitute.org

# database = test and password for root = password
ENV MYSQL_DATABASE=root \
    MYSQL_ROOT_PASSWORD=password


# when container will be started, we'll have `test` database created with this schema
COPY  [--chown=mysql:mysql] ./case_db.sql /docker-entrypoint-initdb.d/
COPY  [--chown=mysql:mysql] ./my.cnf /etc/mysql/my.cnf

RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/
