__version__ = 0 
__authors__ = 'curlyz'

"""
	This library provide a low accuracy timer for user . 
	The accuracy fits only tasked function , with the minimal period is 100us
	
	Function :
		AddTask ( 
			name = "yourtimername" (optional)
			mode = "repeat" or "once" or a number of times that need to be run 
			period = times between each time the function is called ( optional)
			function = define a function first and put the name here
			priority : task with higher priority is done first ( default is 10 ) ( optional)
		)
		
		DeleteTask (
			name = "yourtimername"
		)
		
		PauseTask ( 
			name = "yourtimername"
		)
		
		ResumeTask (
			name  = "yourtimername"
		)
		
		PauseAllTask(priority=1)
		DeleteAllTask(priority=1)
		*SystemTask has highest priority = 1 , these function only affect task with higher priority than specified .
		
	Global :
		TimerStack : list of all active timer 
	Timer :
		This one use Micropython Timer 0
	Example :
		def helloworld():
			print("HelloWorld")
		AddTask( name = "helloworld" , mode = "repeat" , period = "1 second" , function = helloworld , priority = 10 )
		Delete
		
"""
from utime import ticks_diff , ticks_us 
#Timer = [ priority , nexttime , function , name , period , mode ]
TimerStack = [] 
TimerLastInterrupt = 0
def TimerHandler ( source ):
	global TimerLastInterrupt
	TimerLastInterrupt = ticks_us ()
	for i in range(len(TimerStack)):
		if TimerStack[i-1][1] < TimerLastInterrupt and TimerStack[i-1][1] !=0 : #not paused
			TimerStack[i-1][1]=TimerStack[i-1][1]+TimerStack[i-1][4]
			try :
				TimerStack[i-1][2]()
			except Exception as err:
				print(err)
				pass 
			
			if TimerStack[i-1][5] > 0 :
				TimerStack[i-1][5] -=1 
				if TimerStack[i-1][5] == 0:
					TimerStack.pop(i-1)

def AddTask (function,name=None,mode='repeat',period=100,priority=10):
	# Create Object 
	if not callable(function) :
		return "[AddTask]>>>Function can't be called"
	#Search for duplicate 
	for i in range(len(TimerStack)) :
		if TimerStack[i-1][3] == name and TimerStack[i-1][3] != None:
			return "[AddTask]>>>Function already exist"
	# Everything is OK , let clarify 
	if mode == 'repeat' :
		mode = 0 
	elif mode == 'once' :
		mode == 1 
	else :
		if type( mode ) != int :
			return "[AddTask]>>>Mode Undetected"
	if type(period) == str:
		return "[AddTask]>>>Not Implemented"
	Task = [priority,ticks_us()+period,function,name,period,mode]
	TimerStack.append(Task)
	TimerStack.sort()

	
def DeleteTask(name=None):
	for i in range(len(TimerStack)):
		if TimerStack[i-1][3]==name :
			TimerStack.pop(i-1)
			break
			
def PauseTask(name=None):
	for i in range(len(TimerStack)):
		if TimerStack[i-1][3]==name:
			TimerStack[i-1][1]=0 # nextime = 0 mean paused
			break
			
def ResumeTask(name=None):
	for i in range(len(TimerStack)):
		if TimerStack[i-1][3]==name:
			TimerStack[i-1][1] = ticks_us() 
			break 
			
def PauseAllTask(priority = 1):
	for i in range ( len( TimerStack)):
		if TimerStack[i-1][0] > priority:
			TimerStack[i-1][1] = 0
			
def ResumeAllTask(priority = 10):
	for i in range ( len( TimerStack)):
		if TimerStack[i-1][0] < priority:
			TimerStack[i-1][1] = ticks_us()
			
def DeleteAllTask(priority=1):
	return NotImplementedError
			
#Start Timer 

  
