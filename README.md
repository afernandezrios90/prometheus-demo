# Prometheus Demo

Repository for deploying a simple Prometheus installation along with an application to generate metrics

## Description

> [!TIP]  
> You are in the `virtual-store` branch. Other active branches with slightly different funcionality are:
> - `main` --> Prometheus deployment with a basic metric generator app
> - `standalone` --> Prometheus desployment without metric generating app 

This project is a simple Prometheus deployment. Its main purpose is to gather metrics from the virtual store (See: https://github.com/afernandezrios90/virtual-store)

The code is ready to be deployed with Docker with no extra configuration. If no further config is done what is expected is:
- Prometheus instance running on `http://localhost:9090`, collecting data from:
	- Itself (`http://localhost:9090/metrics`)
	- The "Virtual Store App" (`http://localhost:5000/metrics`)
- Data persistence on disk mapped in `/data` directory
- No recording rules or alert rules

## Installation

> [!IMPORTANT]  
> This repo integrates in a larger demo ecosystem; that's why the container are using an existing external network called "grafana-network". Please adapt the container networking section as needed.

1. Clone the repository
```bash
git clone https://github.com/afernandezrios90/prometheus-demo.git
```
3. Adapt container network
4. (Optional) Adjust the configuration: Adjust `prometheus.yaml`, `alert_rules.yml` and `recording_rules.yml` as desired. Or even create new files if you want.
5. Run using Docker compose (if you change something in the Metric Generator app after the first deployment make sure to include the `--build` option os that image is rebuilt)
```bash
docker-compose up -d
```
6. Open the UI in your browser to check the Virtual Store metrics (`http://localhost:5000/metrics`).
7. Open the UI in your browser to check the Prometheus (`http://localhost:9090`).
8. Enjoy navigating and testing.