## compute_input.py

import sys, json, numpy as np

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()
    print json.dumps(lines)
    return
    m = [{
          "header": 'statistic1',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          "header": 'statistic2',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          "header": 'statistic3',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        }
    ]

    #return the sum to the output stream
    print json.dumps(m)


#start process
if __name__ == '__main__':
    main()
