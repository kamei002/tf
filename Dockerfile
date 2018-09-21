FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04
ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y tzdata tk-dev xvfb vim wget git
RUN apt-get install -y python3-pip python3-tk
RUN apt-get install -y doxygen doxygen-gui graphviz
RUN pip3 install numpy matplotlib scipy tensorflow-gpu keras
RUN pip3 install pillow opencv-contrib-python imagehash pydot
