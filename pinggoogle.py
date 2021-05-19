import requests, traceback
from requests import exceptions
import platform
import os
import subprocess
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
from logging import handlers

handler = handlers.TimedRotatingFileHandler("/tmp/seved_connectivity.log", when='midnight')
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def tags_to_prometheus(_tags: dict) -> str:
    output = '{'
    for key, value in _tags.items(): output += key + '="' + value + '", '
    output += '}'
    return output.replace(', }', '}')


def to_prometheus_format(metric_name: str, metric_description: str, _tags: dict, value) -> str:
    response, metric_type = '', 'gauge'
    response += '# HELP {} {}\n'.format(metric_name, metric_description)
    response += '# TYPE {} {}\n'.format(metric_name, metric_type)
    response += metric_name + tags_to_prometheus(_tags) + ' ' + str(value) + '\n'
    return response


def send_metrics(payload, host):
    try:
        r = requests.post('http://172.16.1.37:9091/metrics/job/mns/instance/{}'.format(host), payload.encode(), timeout=10)
        logger.info("Sent Metrics to Grafana: {}".format(r.status_code))
    except:
        logger.info('Failed to push metrics to mns-log, reason: {]'.format(traceback.format_exc()))


def ping_google():
    try:
        file_name="temp_ping.txt"
        command = "ping -n 1 8.8.8.8  > " + file_name
        command1 = "ping -n 1 8.8.8.8"
        print("Running command: " + command)
        os.system(command)
        file = open(file_name, "r")
        result = file.readlines()
        data = result[5]
        if "Lost = 0" in data:
            try:
                #data = response.split('time=')[1].split('ms')[0].strip()
                data = result[-1].split(",")[-1].split("=")[-1].split("ms")[0].lstrip().rstrip()
                data = float(data)
                print(data)
                return data
            except:
                logger.info(traceback.format_exc())
                return 0
        else:
            logger.info('got packet loss or could not parse the ping output:\n{}'.format(response))
            return 0
    except:
        logger.info('unexpected error: {}'.format(traceback.format_exc()))
        return 0

if __name__ == "__main__":
    try:
        response = ""
        device_id = platform.node()
        host = device_id
        host = host.lower()
        region = 'se'
        tags = {"region": region, "type": 'seved'}
        logger.info("Pingning Google....")
        ping_result = ping_google()
        response += to_prometheus_format('seved_device_ping_google_status', 'Status of connection', tags, ping_result)
        logger.info("Sending metrics....")
        send_metrics(response, device_id)
    except:
        logger.info('unexpected error: {}'.format(traceback.format_exc()))