import json
import logging
import random
import time
import configparser
import logging.handlers
from datetime import datetime, timezone

sample_data = {
    "timestamp": "", # ISO Zulu date format
    "equip_name": "X-Machine",
    "feed_rate": 0.0,
    "shaft_speed": 0,
    "oil_temperature": 0.0,
    "voltage": 0
}


def main():
    loop = True
    print("Starting program...")
    config = configparser.ConfigParser()
    config.read('./load-json-data.config')

    backup_count = config.getint('Data', 'BackupCount')
    hourly_interval = config.getint('Data', 'HourlyInterval')
    output_file = config['Data']['WriteDirectory'] + '/' + config['Data']['WriteFile']
    sleep_in_seconds = config.getint('Data', 'SleepInSeconds')

    # format the log entries, making use of the log rotation functions already written in python
    formatter = logging.Formatter('%(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(
        output_file, when='H', interval=hourly_interval, backupCount=backup_count)
    handler.setFormatter(formatter)

    logger = logging.getLogger("data")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    while loop:
        time.sleep(sleep_in_seconds)
        sample_data['timestamp'] = datetime.now(timezone.utc).isoformat()
        sample_data['feed_rate'] = float(random.randint(2000, 3000))/100
        sample_data['shaft_speed'] = random.randint(20, 30)
        sample_data['oil_temperature'] = float(random.randint(1000, 1200))/100
        sample_data['voltage'] = random.randint(425, 430)
        logger.info(json.dumps(sample_data))
        print('wrote data to disc')


if __name__ == "__main__":
    main()
