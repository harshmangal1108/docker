# Docker
## Working with Docker
# Commands
`docker run ubuntu`
### Used to run a container from an image. if image doesn't exits it will go to docker hub and pull it down.
`docker ps`
### `ps` command lists all the running containers and some info. regarding them such as (ID,image name,current status and assigned name)
 `docker ps -a` 
### This -a --> lists all running as well as dead containers.
 `docker stop container_id`
### Stop command stops the running docker container, ID/Assigned_name should be specified on success it will output the name.
 `docker rm container_id`
### When conatiner is stoped it is still uses disk space to get rid of that use `rm` command specify name or id and it will remove that dead conatiner.
 `dokcer images`
### List all the images pulled/available from docker hub
 `docker rmi ubuntu`
### `rmi` removes the image where as `rm` removes the container. you must stop all the container of that image before deleting it.
 `docker pull image_name`
### It will pull image and save it. 
 `docker run ubuntu date`
### It is example for printing date from ubuntu image via a container.










 
