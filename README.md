# elk-docker-compose
This is a simple project to setup ELK in docker compose. It can provide a playground to test ELK configuration
and data parsing with logstash.

There is a data generator for parsing XML and JSON. The XML requires logstash to pull apart the fields and make
the indexed field names easier to work with or mark only certain fields for indexing. The JSON data is directly
sent to ES using only filebeats.

First install docker and docker-compose.

Second, create the docker images of the data generator.

```shell script
docker build -t test/simulate-data-json -f dockerfile-json .
docker build -t test/simulate-data-xml -f dockerfile-xml .
```

Next, run the compose yml file. The -d flag will not output the console from all of the containers. You run the same
command below again without the flag to see it at anytime. Running the same command will also restart
any containers that are not currently running. It sometimes helps to run two terminal sessions, one 
for logs and another for restarting the failed containers while testing.
 
```shell script
docker-compose -f ./elk.compose.yml up -d
```

It will take a moment for the entire stack to start. Once started, Kibana is available at localhost:5601/kibana-proxy
using the default username and password (elastic/changeme).

Finally, on first run, create an index for Kibana. Go into Management->(Elasticsearch) Index Management and make sure there are
counted documents. Next go to the Kibana section, and select Index Pattern. For our immediate purpose, enter * as the
index pattern and @timestamp as the time filter field name. By default the logs section will only look at one index, 
(filebeat-* for example) but click the gear icon and configure the source for metric and log indices to both be a wildcard '*' 
value. Data should now be displayed. Note that the JSON data does not have a message filed, hence the log data display.

Have fun creating dashboards with visualizations of data!