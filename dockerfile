FROM python:3.11-alpine
ADD metric_generator_app /metric_generator_app
RUN pip install -r /metric_generator_app/requirements.txt
CMD ["python", "metric_generator_app/metric_generator.py"]