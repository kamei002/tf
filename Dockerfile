FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04
ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y tzdata tk-dev xvfb vim wget
RUN apt install -y python3-pip python3-tk
RUN pip3 install numpy matplotlib scipy tensorflow-gpu keras pillow opencv-contrib-python imagehash
RUN apt install -y git
