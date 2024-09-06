# OTUS_AQA Docker compose


поменять порт по-умолчанию для контейнера selenoid-ui, запустить контейнер следующей командой:

`docker run -d --name selenoid-ui --network selenoid -p 8090:8080 aerokube/selenoid-ui:1.10.11 --selenoid-uri http://selenoid:4444`


# OTUS_AQA Dockerfile

запуск локально (default):

`pytest  --launch_mode local` 

запуск удаленно (default):

`pytest`

запуск через docker (default):

`docker run -it --rm --network selenoid --name myapp  tests:0.2 --executor 172.19.0.3 tests`

запуск через docker (firefox):

`docker run -it --rm --network selenoid --name myapp  tests:0.2 --executor 172.19.0.3 --browser firefox tests`

при запуске в несколько потоков -n 2


PS C:\Users\mx\Downloads\drivers> .\cm_windows_amd64 selenoid status/start

скачать браузер:

docker run --rm -it --privileged selenoid/chrome:127.0


# Dockerfile

собрать: docker build -t tests:0.2 . 

запустить: docker run -it --rm --name myapp tests:0.2 --headless --browser firefox

остановить: docker stop

docker ps - информация o Containers

docker images - информация o Images

docker system df  - информация обо всех объектах Images Containers Local_Volumes Build Cache

docker system prune

docker system info


# OPENCART:

docker-compose up -d - запустить сборку приложения

docker ps - посмотреть запущенные контейнеры

docker ps -a - посмотреть все контейнеры (включая потушенные)

docker-compose down - потушить все контейнеры из docker-compose файла

docker images - показать все сборки

docker system prune -a - удалить все образы

docker volume prune -a  - очистить кеш



