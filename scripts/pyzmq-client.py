#!/bin/python
import sys
import time
import json
import zmq
import couchdb
import numpy as np


import argparse

def parseCmdLineArgs():
    parser = argparse.ArgumentParser()
    # add optional arguments
    parser.add_argument ("-a", "--addr", default="129.114.25.68:30002", help="IP address and port to reach the server, default localhost:5556")
    
    # add optional arguments
    parser.add_argument ("-j", "--outer_iters", type=int, default=10, help="Number of outer iterations, default 10")
    parser.add_argument ("-i", "--inner_iters", type=int, default=305, help="Number of iterations, default 20")
    
    # add positional arguments in that order
    parser.add_argument ("results_file", help="output file to store results")

    # parse the args
    args = parser.parse_args ()

    return args


def send_request(server, outer_iters, inner_iters, results_file, all_ids):
    try:
        all_resp_times = np.zeros(outer_iters * inner_iters)
        for j in range(outer_iters):
            for i in range(inner_iters):
                print(f"Sending request number {i}")
                
                start_time = time.time()
                print("num of ids: ", len(all_ids))

                server.send_string(all_ids[i])

                # wait for reply
                print("Waiting to receive reply")
                reply = server.recv_pyobj()
                # num_json_objs = reply['num_json']

                end_time = time.time()
                resp_time = end_time - start_time
                all_resp_times[j * inner_iters + i] = resp_time
                #all_resp_times[j * i + i] = resp_time
                # np.insert(all_resp_times, j*i+i, [resp_time])
                # total_resp_time[0] += resp_time
                print(f"Iteration {j}-{i}, Round trip time = {resp_time}")

                # insert result in file
                print("Write results into file")
                results_file.write(f"{j}-{i}, resp_time: {resp_time}\n")
        return all_resp_times
            
    except:
        print(f"Error: {sys.exc_info()[0]}")


def main():
    all_ids = []
    # all_resp_times = np.array([])
    # total_resp_time = [0]
    

    couch = couchdb.Server('http://admin:admin@129.114.25.5:30001/')
    db = couch['energy-new']
    rows = db.view('_all_docs', include_docs=True)

    data = []
    for item in rows:
        all_ids.append(item.id)
    
    try:
        print("Parse the command line")
        parsed_args = parseCmdLineArgs()

        print(f"Server: {parsed_args.addr}, total iterations: {parsed_args.outer_iters * parsed_args.outer_iters}, log file: {parsed_args.results_file}")

        print("Obtain ZMQ context")
        context = zmq.Context()

        # create a handle to the server
        print("Connecting to server...")
        server = context.socket(zmq.REQ)
        server.connect("tcp://" + parsed_args.addr)

        # open the log file for saving results
        print("Open results file for writing")
        results_file = open(parsed_args.results_file, "w")

        # send the request to the server and wait for results
        print("Making a request on the server")
        all_resp_times = send_request(server, parsed_args.outer_iters, parsed_args.inner_iters, results_file, all_ids)
        
        total_resp_time = np.sum(all_resp_times)
        avg_resp_time = np.average(all_resp_times)
        std_resp_time = np.std(all_resp_times)
        results_file.write(f"Total Number of Iterations: {parsed_args.inner_iters * parsed_args.outer_iters},\n Total Response Time: {total_resp_time},\n Mean Response Time: {avg_resp_time},\n STD DEV Response Time: {std_resp_time}")
        print(f"Total Number of Iterations: {parsed_args.inner_iters * parsed_args.outer_iters},\n Total Response Time: {total_resp_time},\n Avg. Response Time: {avg_resp_time},\n STD DEV Response Time: {std_resp_time}")

        # close the file 
        print("close the results file")
        results_file.close()

        # close connection to server
        print("Close connection to server")
        server.close()
    
    except:
        print(f"Error: {sys.exc_info()[0]}")
        raise

if __name__ == "__main__":
    main()




