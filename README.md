ob1. Установите виртуальное окружение sudo apt install python3-venv
2. Активируйте виртуальное окружение source myenv/bin/activate
2. Скачать проект в папку на своем ПК git clone https://github.com/obeginin/Base.git
3. установить docker и docker-compose для запуска
sudo apt update
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $USER ( $USER поменять на своего)
собрать и запустить проект docker-compose up --build


