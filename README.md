# Prometheus Demo

Repository for deploying a simple Prometheus installation along with an application to generate metrics

## Description

> [!TIP]  
> You are in the `main` branch. Other active branches with slightly different funcionality are:
> - `standalone` --> Prometheus desployment without metric generating app 
> - `virtual-store` --> Prometheus deployment pre-configured to monitor the Virtual Store app (Please check: https://github.com/afernandezrios90/virtual-store)

This project is a simple Prometheus deployment. Its main purpose is to test basic funcionality, such as practice queries, create metric rules or alert rules, etc.
"Metric Generator App" is a python application that creates some values simulating a real metrics:
```
# HELP cpu_usage CPU usage percentage
# TYPE cpu_usage gauge
cpu_usage{Datacenter="C1",Server="machine1"} 0.63
cpu_usage{Datacenter="C2",Server="machine1"} 0.81
cpu_usage{Datacenter="C1",Server="machine2"} 0.48
cpu_usage{Datacenter="C2",Server="machine2"} 0.16
```

The code is ready to be deployed with Docker with no extra configuration. If no further config is done what is expected is:
- Prometheus instance running on `http://localhost:9090`, collecting data from:
	- Itself (`http://localhost:9090/metrics`)
	- The "Metric Generator App" (`http://localhost:8000/metrics`)
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
4. (Optional) Adjust the configuration:
	a. Prometheus configuration: Adjust `prometheus.yaml`, `alert_rules.yml` and `recording_rules.yml` as desired. Or even create new files if you want.
	b. Metric Generator configuration: Adjust `metric_generator.py` to include more metrics, metric types and more value randomness. Imagination is the limit.

5. Run using Docker compose (if you change something in the Metric Generator app after the first deployment make sure to include the `--build` option os that image is rebuilt)
```bash
docker-compose up -d
```
6. Open the UI in your browser to check the application metrics (`http://localhost:8000/metrics`).
7. Open the UI in your browser to check the Prometheus (`http://localhost:9090`).
8. Enjoy navigating and testing.