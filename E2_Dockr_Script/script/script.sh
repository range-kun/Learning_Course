#!/bin/sh
echo "Скачиваю иконку для сайта $1"
wget -P /home/favicon http://favicon.yandex.net/favicon/${1}
