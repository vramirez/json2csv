import json
import os
import io
import configparser
import sys

def filename_tocsv(filename):
    return filename_toxxx(filename,'csv')



def filename_toxxx(file_name, extension_name):
    if len(file_name.split('.')) > 0:
        return '.'.join(file_name.split('.')[0:-1])+'.'+extension_name
    else:
        return file_name+'.'+extension_name

def write_object_file(obj, vec,filename,sep=','):    
    
    with open(filename_out, 'a') as outfile:
        for col in vec:
            key = col.split('.')
            if len(key) > 1:
                outfile.write(strip_all(str(obj[key[0]][key[1]])))
            else:
                outfile.write(strip_all(str(obj[col])))
            outfile.write(sep)
        outfile.write('\n')

def strip_all(str1):
    return str1.replace('\n','').replace('\t','').replace('\r','')

if  __name__ == "__main__":  
    if len(sys.argv)  == 2 :
        filename_in= sys.argv[1]
        filename_out= filename_tocsv(filename_in)
        config = configparser.RawConfigParser()
        config.read('j2c.properties')
        vec = config.get('main','columns')
        separator = config.get('main','separator')
        vec=vec.split(',')
        print("Converting. Please wait...")
        with open(filename_in, 'r',encoding='utf-8') as myfile:
            for line in myfile: 
                obj = json.loads(line)
                write_object_file(obj,vec,filename_out,sep=separator)
        print("File {} converted to {} ".format(filename_in,filename_out))
        
    else:
        print("Correct usage: python {} filename.json".format(sys.argv[0]))            


