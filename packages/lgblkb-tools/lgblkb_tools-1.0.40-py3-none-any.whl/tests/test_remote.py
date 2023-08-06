from invoke import Responder

from lgblkb_tools import logger,Folder
from fabric import Connection

def main():
	conn=Connection(host='10.1.143.179',user='ubuntu')
	sudopass=Responder(
		pattern=r'\[sudo\] password:',
		response='mypassword\n',)
	conn.run('sudo whoami',pty=True,watchers=[sudopass])
	
	pass

if __name__=='__main__':
	main()
