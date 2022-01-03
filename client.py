from tkinter import*
import socket
from threading import Thread
root=Tk()
root.title('Chat Room')

'''Login Page'''
login_frame=Frame(root)
login_frame.pack()
host_name = socket.gethostname()
host='192.168.7.42'
print(host)
port=5050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def login():
    username=entry.get()
    s.sendall(username.encode())
    login_frame.pack_forget()
    chat_frame.pack()

info=Label(login_frame,text='Enter your Username')
info.grid(row=1,column=1)
entry=Entry(login_frame)
entry.grid(row=2,column=1)
login=Button(login_frame, text='Login',command=login)
login.grid(row=3,column=1)

'''Chat page'''
chat_frame=Frame(root)
display=Label(chat_frame,text='',width=40, height=10)

# Sends message/data to Server
def send():
    global s
    content=chat_entry.get()
    s.sendall(content.encode())
    chat_entry.delete(0, END)

#Reieves the message/data that has been sent by the server and displays is it on the tk ui
def receive():
    while True:
        data=s.recv(1024)
        print(data.decode())
        display['text']= display['text']+'\n'+data.decode()
        display.grid(row=1,column=1)


#Each client is always listening to the server and waiting for messages to be routed through
recp=Thread(target=receive)
recp.start()



chat_entry=Entry(chat_frame)
chat_entry.grid(row=2,column=1)
send=Button(chat_frame, text='Send',command=send)
send.grid(row=3,column=1)


root.mainloop()
