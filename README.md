# Prometheus Demo

Repository for deploying a simple Prometheus installation along with an application to generate metrics

## Description

> [!TIP]  
> You are in the `standalone` branch. Other active branches with slightly different funcionality are:
> - `main` --> Prometheus desployment along with a metric generating app 
> - `virtual-store` --> Prometheus deployment pre-configured to monitor the Virtual Store app (Please check: https://github.com/afernandezrios90/virtual-store)

This project is a simple Prometheus deployment. Its main purpose is to test basic funcionality, such as practice queries, create metric rules or alert rules, etc. It only has (as it is configured) its own internal metrics, nothing else. Feel free to add scraping targets.

The code is ready to be deployed with Docker with no extra configuration. If no further config is done what is expected is:
- Prometheus instance running on `http://localhost:9090`, collecting data from itself (`http://localhost:9090/metrics`)
- Data persistence on disk mapped in `/data` directory
- No recording rules or alert rules

## Installation

1. Clone the repository
```bash
git clone https://github.com/afernandezrios90/prometheus-demo.git
```
2. Switch to desired branch
3. Adapt container network to be able to connect to other docker targets (if needed)
4. (Optional) Adjust the configuration:
	a. Prometheus configuration: Adjust `prometheus.yaml`, `alert_rules.yml` and `recording_rules.yml` as desired. Or even create new files if you want.
5. Run using Docker compose (if you change something in the Metric Generator app after the first deployment make sure to include the `--build` option os that image is rebuilt)
```bash
docker-compose up -d
```
6. Open the UI in your browser to check the Prometheus (`http://localhost:9090`).
7. Enjoy navigating and testing.