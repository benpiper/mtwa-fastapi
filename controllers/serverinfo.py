from fastapi import APIRouter, Depends, HTTPException, Security
import socket
import os

router = APIRouter()

@router.get("/hostname")
def get_hostname():
    return socket.gethostname()

@router.get("/ip")
def get_ipv4():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock.getsockname()[0]

@router.get("/port")
def get_port():
    return "Not implemented"

@router.get("/environment")
def get_env():
	return(getserverparams())

@router.get("/environment/{key}")
def get_env(key: str):
	return(getserverparam(key))

def getserverparams():
    environmentvars = {}
    for each in os.environ.keys():
        environmentvars[each] = os.environ[each]
        
    return environmentvars


def getserverparam(param_name):

    for each in os.environ.keys():	
		#Uncomment the next line if you want to see all of the values that could be used
        print (each, os.environ[each]), "<br>" #db
        #print each ":each <br>" #db
    
    for each in os.environ.keys():	
	    each_value = os.environ[each]
	    each_value_string = str(each_value)
	    each_string = str(each)

	    if each_string == param_name:			
		    servervalue = each_value_string
		    return servervalue

    return None