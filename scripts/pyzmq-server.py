# This script is our server side pyzmq

# import time
import sys
import zmq
import json
import couchdb

couch = couchdb.Server('http://admin:admin@129.114.26.85:30001/')
client_req_count = 0

def main(client_req_count):
	try:
		# first obtain zmq context
		context = zmq.Context()

		# instantiate the server object
		server = context.socket(zmq.REP)
		server.bind("tcp://*:5556")

		# couch db
		while True:
			# client requests read operation
			client_request = server.recv_string()
			print(client_request)
			client_req_count += 1

			# couch db energy
			db = couch['energy-new1']

			# get document id from client_request
			doc_id = client_request

			# get document from the database
			reply = db.get(doc_id)

			# send document back to client
			server.send_pyobj(reply)

		server.close()
		context.term()

	except:
		print("Error: {}".format(sys.exc_info()[0]))
		server.close()
		context.term()
		raise

# entry point
if __name__ == "__main__":
	main(client_req_count)
