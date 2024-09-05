# OTUS_AQA


PS C:\Users\mx\Downloads\drivers> .\cm_windows_amd64 selenoid status

docker run --rm -it --privileged selenoid/chrome:latest


при запуске контейнера с тестами указать опцию --network=selenoid --launch_mode=remote

docker  inspect selenoid   посмотреть в какой сети запущен selenoid и какой IP адрес ему назначен

при запуске в несколько потоков -n 2

# Dockerfile

docker build -t tests:0.2 . 

docker run -it --rm --name myapp tests:0.2 --headless --browser firefox

docker stop

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


