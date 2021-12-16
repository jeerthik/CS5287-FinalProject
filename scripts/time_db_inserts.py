import couchdb
import time
import asyncio
import argparse

def parseCmdLineArgs():
    parser = argparse.ArgumentParser()
    
    # add optional arguments
    parser.add_argument ("-i", "--iters", type=int, default=10, help="Number of outer iterations, default 10")
    
    # add positional arguments in that order
    parser.add_argument ("results_file", help="output file to store results")

    # parse the args
    args = parser.parse_args ()

    return args

def save_to_db(all_test_data):
    count = 0
    for test_data in all_test_data:
        
        json_entry = {}
        json_entry['Timestamp'] = time.ctime()
        json_entry['Data'] = test_data

        # print(f"send entry {count}: {json_entry}")
        doc_id, doc_rev = db.save(json_entry)
        
        count += 1



if __name__ == "__main__":
    
    # Contains insertion time per iteration
    insert_times = []

    couch = couchdb.Server('http://admin:admin@129.114.26.85:30001/')
    if "energy-new" in couch:
        db = couch['energy-new']
    else:
        db = couch.create('energy-new')

    parsed_args = parseCmdLineArgs()
    results_file = open(parsed_args.results_file, "w")

    # Run insertion loop and get completion time per iteration
    for i in range(parsed_args.iters):

        all_test_data = [
            [{"json_id": i * 10, "val": i * 10} for i in range(10)] for _ in range(100)
        ]

        s = time.perf_counter()
        # asyncio.run(invoke_save_to_db(all_test_data))
        save_to_db(all_test_data)
        elapsed = time.perf_counter() - s
        print(f"Iteration {i}: Executed in {elapsed:0.2f} seconds")
        insert_times.append(elapsed)

    print(insert_times)
    # write the results to our file
    for i in range(len(insert_times)):
        results_file.write(f"Iteration {i}: {str(insert_times[i])}" + "\n")
    # find avg. insert time using all of our iterations
    avg_insert_time = sum(insert_times) / len(insert_times)
    # write the average to our file
    results_file.write("Avg. insert time: {}\n".format(avg_insert_time))
    # print the average at the end
    print("Avg. insert time: {}".format(avg_insert_time))
    # close results file
    results_file.close()
