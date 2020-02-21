import logging
import time
import configparser
import logging.handlers


def main():
    loop = True
    print("Starting program...")
    config = configparser.ConfigParser()
    config.read('./load-xml-data.config')

    backup_count = config.getint('Data', 'BackupCount')
    hourly_interval = config.getint('Data', 'HourlyInterval')
    output_file = config['Data']['WriteDirectory'] + '/' + config['Data']['WriteFile']
    sleep_in_seconds = config.getint('Data', 'SleepInSeconds')

    # format the log entries, making use of the log rotation functions already written in python
    formatter = logging.Formatter('%(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(
        output_file, when='H', interval=hourly_interval, backupCount=backup_count)
    handler.setFormatter(formatter)

    s1 = open("sample_1.xml", "r")
    s2 = open("sample_2.xml", "r")
    s3 = open("sample_3.xml", "r")

    s1_message = s1.read()
    s1.close()

    s2_message = s2.read()
    s2.close()

    s3_message = s3.read()
    s3.close()

    logger = logging.getLogger("data")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    i = 1
    while loop:
        time.sleep(sleep_in_seconds)
        if i == 1:
            logger.info(s1_message)
        elif i == 2:
            logger.info(s2_message)
        elif i == 3:
            logger.info(s3_message)

        handler.flush()
        if i == 3:
            i = 1
        else:
            i += 1

        print('wrote data to disc')


if __name__ == "__main__":
    main()
