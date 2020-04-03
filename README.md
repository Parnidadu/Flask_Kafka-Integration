# Flask_Kafka-Integration
This project is for Kafka integration with python flask.

This repository will lead you to build a service which takes data from some API(undisclosed) and then send it to the kafka stream via Flask.

# Setting Up kafka server on your machine

visit this sight and click the first link to download kafka https://kafka.apache.org/quickstart
now I am simply following the same steps as were told in the documentation itself.

Unzip the tar file on your system,
Also we need multiple terminal for this purpose.
```
tar -xzf kafka_2.12-2.4.1.tgz
cd kafka_2.12-2.4.1
```
# Installing Flask and Kafka
write this command to install Flask and Kafka on your machine.

```
pip install flask
pip install kafka
```
that's it

# start the server zookeper and Kafka

To start the kafka server we first need to run zookeeper , if you are unaware of what zookeeper is and how it help kafka then visit this link https://zookeeper.apache.org/ . Now a zookeeper is basically responsible for managing kafka cluster .
I will separately make a video on youtube about it, and sooner I will share the link here.
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```


This zookeeper will run on one of the terminal.
now move to the second terminal and with the same location as that of where zookeeper is running.
which is 
```
cd kafka_2.12-2.4.1
```
Starting kafka server .
```
bin/kafka-server-start.sh config/server.properties
```
# Creating Topics

create a topic named "test" with a single partition and only one replica:
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```
Try to understand this command , 
here we are running a bash file with some arguments which creates a topics with name 'test' number of partition is 1 and the replication factor meaning duplicacy is 1.
I  will let you guys know more about dupliaccy and why it is used in the video itself , for now just remember this as mirror file or dupliacte file for the data stream which sustain even if one data stream get corrupted or even get lost.

# Start a Consumer 

here we don't need the producer because we will be sending data from our flask machine.
first let create some duplicate server for this purpose.

```
cp config/server.properties config/server-1.properties
cp config/server.properties config/server-2.properties

```

```
bin/kafka-server-start.sh config/server-1.properties &
```

# running flask 

for starting the flask machine 
initiate this command.

```
python Flask_kafka.py
```
send some events from POSTMAN with value 'name','test' and also a json file for this code to work.
I have wriiten this code for this purpose only is any thing goess incorrect the program will not execute correctly.
