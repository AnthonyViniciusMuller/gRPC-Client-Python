import grpc
import threading
import os
import protos.messenger_pb2 as pb2
import protos.messenger_pb2_grpc as pb2_grpc

def receive_messages(stub):
	while True:
		stream = stub.GetMessages(pb2.Void())

		for message in stream:
			print(f'\n\n{message.User}: {message.Message}\n\n> ', end = '')

def send_message(stub):
	user_name = input('Qual é o seu usuário: ')
	print('> ', end = '')

	while True:
		message = input()

		stub.SendMessage(
			pb2.Message(
				Message = message, 
				User = user_name
			)
		)

if __name__ == "__main__":
	os.system('cls||clear')

	print('Python Client \n\n')

	channel = grpc.insecure_channel('localhost:4444')
	stub = pb2_grpc.ChatStub(channel)

	try:
		thread = threading.Thread(target=receive_messages, args=(stub,))
		thread.start()
	except:
		print("Error: cannot receive messages")

	try:
		thread = threading.Thread(target=send_message, args=(stub,))
		thread.start() 
	except:
		print("Error: cannot send messages")
	