 # building a docker image and running it
 
 With Docker installed, create a Dockerfile in a working directory. A sample C++ dev container Dockerfile is shown below:
 ```
 FROM alpine

 RUN apk --update add --no-cache \
    build-base \
    boost boost-dev \
    cmake \
    openssl openssl-dev \
    g++

 ```
 Then run the following at the command line, in a directory containing the Dockerfile:
  
 ``` 
 docker build -t cpp-boost .  
 ```

 When the image is finished building, you can the run the image in a container using the following command:
  
 ```
    docker run -d --name cpp-dev-boost -it cpp-boost
    
 ```
 This will launch the container in detached mode, using the image you provided.
