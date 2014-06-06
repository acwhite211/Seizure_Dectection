import numpy as np
import scipy.io
import csv

def main():
    print('hi')
    mat = scipy.io.loadmat('sample_clip.mat')
    
    data = mat['data'].tolist()
    freq = mat['freq'].tolist()
    channels = mat['channels'].tolist()
    latency = mat['latency'].tolist()
    #data_length_sec = mat['data_length_sec'].tolist()
    #table = [k for k in mat.keys()]
    
    with open('sample_clip.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(['freq'])
        w.writerow(freq)
        #w.writerow(['data_length_sec'])
        #w.writerow([data_length_sec])
        w.writerow(['latency'])
        w.writerow(latency)
        w.writerow(['channels'])
        w.writerows(channels)
        w.writerow(['data'])
        w.writerows(data)

    
if __name__ == '__main__':
    main()
    print('done')