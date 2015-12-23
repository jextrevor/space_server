from module import Module
class SocketModule(Module):
	def __init__(self,socketio,namespace,room=None):
		Module.__init__(self)
		self.socketio = socketio
		self.namespace = namespace
		self.room = room
	def receive(self,event,json):
		r = self.checkout("receiver")
		if r == False:
			return False
		r.receive(event,json)
	def send(self,event,json):
		if self.room == None:
			self.socketio.emit(event,json,namespace=self.namespace)
		else:
			self.socketio.emit(event,json,namespace=self.namespace,room=self.room)