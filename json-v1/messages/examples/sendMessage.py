import sys
import paho.mqtt.publish as publish
import json 

def get_msg(name):
    f = open(name)
    msg = json.loads(f.read())
    f.close()
    return msg 



if len(sys.argv) == 1:
    print " First argument is - topic , second is - message file name  "
    print "Topic examples: "
    print "     pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:1"
    print "     pt:j1/mt:evt/rt:ad/rn:zw/ad:1" 
    sys.exit()


topic = sys.argv[1] 
msgFile = sys.argv[2]

jmsg = None 
jmsg = get_msg(msgFile)

if jmsg :        
    publish.single(topic, json.dumps(jmsg), hostname="localhost")
else :
    print "Something went wrong "    