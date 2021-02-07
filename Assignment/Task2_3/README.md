## DevOps Intern Assignment
### Task 2,3:
- ####  Running a service on any port (except 8080)
- #### Configuring the reverse proxy to access above service in nginx

### Solution:
- In Order to complete both the things we need to `docker` run below commands
```bash
$ docker build -t task2image:v1 .
$ docker run -itd -p 8090:80 task2image:v1
```
***Note***: Make sure Docker daemon is running in system.
#### You can see the effect at http://127.0.0.1
