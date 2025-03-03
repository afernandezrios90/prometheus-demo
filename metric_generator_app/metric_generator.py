import random
import time
from prometheus_client import start_http_server, Gauge

# 1. Metric definition
cpu_usage = Gauge("cpu_usage", "CPU usage percentage", ["Server","Datacenter"])

# 2. Label definition
servers = ["machine1", "machine2"]
datacenters = ["C1", "C2"]

# 3. Value creation (for metric itself + for labels)
def generate_values():
    for server in servers:
        for datacenter in datacenters:
            value = round(random.uniform(0, 1), 2)
            cpu_usage.labels(Server=server, Datacenter=datacenter).set(value)

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)
    
    # Infinite loop of value creation
    while True:
        generate_values()
        
        # Sleep for 30 sec
        time.sleep(30)