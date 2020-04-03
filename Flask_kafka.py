from flask import Flask, Response,request
import json
from kafka import KafkaConsumer,KafkaProducer

app = Flask(__name__)


class Controller:
	@app.route('/',methods=['POST','GET'])
	def index():
		if request.method == 'POST':
			user = request.args.get('user')
			test = request.args.get('test')
			status = request.json
			events = status['data']
			producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
			producer.send('test',json.dumps(user).encode('utf-8'))
			producer.send('test',json.dumps(test).encode('utf-8'))
			producer.send('test',json.dumps(events).encode('utf-8'))
		return 'Data sent'
 

if __name__=='__main__':
	app.run(debug=True,port=9091)
	controller = Controller()
	controller.index()

