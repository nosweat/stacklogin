#!/usr/bin/python
"""
INSTALLATION SETUP SCRIPT
"""
import sys, shutil, plistlib, subprocess

class plist:
    
    app_name = '/usr/local/bin/./stacklogin'
    file_name = 'com.stacklogin.osx.login'
    target_plist = ''
    working_plist = ''
    username = ''
    password = ''
    
    def __init__(self):
        self.readFromFile()
        
    def readFromFile(self):
        f = open('config/stack.config', 'r')
    	line_username = f.readline().rstrip()
        line_password = f.readline().rstrip()
        uname = line_username.split('=');
        pwd = line_password.split('=');
        self.username = uname[1]
        self.password = pwd[1]
        
    def create(self):
        pl = dict(
            Label=self.file_name,
            Program=self.app_name,
            ProgramArguments=[self.app_name,"--username", self.username, "--password", self.password],
            KeepAlive=True
        )
        self.target_plist = 'plist/' + self.file_name + '.plist'
        self.working_plist = "~/Library/LaunchAgents/" + self.file_name + ".plist"
        plistlib.writePlist(pl, self.target_plist)
        subprocess.Popen("cp " + self.target_plist + " " + self.working_plist , shell=True)
        
    def install(self):
        subprocess.Popen("chmod +x src/stacklogin", shell=True)
        subprocess.Popen("cp src/stacklogin /usr/local/bin/stacklogin", shell=True)
        subprocess.Popen("launchctl load " + self.working_plist, shell=True)
    
def main():
    print "Setting up stacklogin..."
    p = plist()
    p.create()
    p.install()
    print "Done installation..."
          
if __name__ == "__main__":
   main()