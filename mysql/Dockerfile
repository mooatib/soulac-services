FROM mysql:5.7.38

WORKDIR /mysql

COPY ./scripts/structure.sql /docker-entrypoint-initdb.d/1.sql

EXPOSE 3306