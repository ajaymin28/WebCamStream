# WebCamStream
WebCamStream using socket connection.


# Docker Build Status for requirements file

[![Building Docker Image](https://github.com/ajaymin28/WebCamStream/actions/workflows/build-docker-image.yml/badge.svg)](https://github.com/ajaymin28/WebCamStream/actions/workflows/build-docker-image.yml)


# Introduction

OpenCV based streaming of webcam from one machine to another in a local network.

1. StartWebCamStream.py

This file will use your webcam default to index 0 and start streaming with socket connection.

2. ReadWebCamStream.py

This file should be used to access the webcam which is started with StartWebCamStream.py file. 
Don't forget to change the IP if you are using server on different computer.
