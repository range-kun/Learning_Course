docker build -t fav_ico:test ./  
docker run --env SOURCE="{site.com}" -v /home/range/docker/favicon:/home/favicon fav_ico:test  
i.e:  
docker run --env SOURCE="wikipedia.org" -v /home/range/docker/favicon:/home/favicon fav_ico:test  
