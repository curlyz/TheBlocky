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

