FROM java
maintainer harsh.mangal1108@gmail.com
env classname=hello
### optional and will be using for future
run mkdir /codes
add hello.java /codes/hello.java
## a step to compile code -- byte code creation
workdir /codes/
## compile
RUN javac hello.java
## run java code
CMD java hello
