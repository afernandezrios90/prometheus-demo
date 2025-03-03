# Prometheus Demo

Repository for deploying a simple Prometheus installation along with an application to generate metrics

## Description

This project is a simple Prometheus deploynent


## Installation
1. Clone the repository
```bash
git clone https://github.com/afernandezrios90/prometheus-demo.git
```
2. Adjust the configuration if desired to change the config path, as well as the configuration and rules files
3. Run using Docker compose
```bash
docker-compose up -d
```
4. Open the UI in your browser to check the application (`http://localhost:8080/metrics`).
5. Open the UI in your browser to check the Prometheus (`http://localhost:9090`).
