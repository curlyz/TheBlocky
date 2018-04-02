def update ( file_name ):
  import urequests ,os,machine
  url = 'https://raw.githubusercontent.com/curlyz/TheBlocky/master/src/' + file_name + '.py'
  response = urequests.get(url)
  print( 'Received',len( response.content))
  f = open(file_name + '.py', 'w')
  f.write(response.content)
  f.close()
  print('[DEBUGGER]>>>File' + file_name + 'UPDATED' )
  try :
    import file_name
    machine.reset()
  except:
    for i in range(10):
      print("DeleteUserCode") #TODO
  
