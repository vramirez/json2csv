import json
import os
import io

def filename_tocsv(filename):
    return filename_toxxx(filename,'csv')



def filename_toxxx(file_name, extension_name):
    if len(file_name.split('.')) > 0:
        return '.'.join(file_name.split('.')[0:-1])+'.'+extension_name
    else:
        return file_name+'.'+extension_name

def write_object_file(obj, vec,filename):    
    
    with open(filename_out, 'a') as outfile:
        for col in vec:
            key = col.split('.')
            if len(key) > 1:
                outfile.write(strip_all(str(obj[key[0]][key[1]])))
            else:
                outfile.write(strip_all(str(obj[col])))
            outfile.write(',')
        outfile.write('\n')

def strip_all(str1):
    return str1.replace('\n','').replace('\t','').replace('\r','')

if  __name__ == "__main__":    
    filename_in= 'covid_20200831.json'
    filename_out= filename_tocsv(filename_in)
    vec=['id','created_at','text','user.created_at','user.screen_name','user.name']
    with open(filename_in, 'r',encoding='utf-8') as myfile:
        for line in myfile: 
            obj = json.loads(line)
            write_object_file(obj,vec,filename_out)
            


