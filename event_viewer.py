import win32evtlog
server = 'localhost'
logtype = 'System'
hand = win32evtlog.OpenEventLog(server, logtype)
total = win32evtlog.GetNumberOfEventLogRecords(hand)
print("Scanning through {} events on {} in {}".format(total, server, logtype))
flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ
print("flags: "+str(flags))
gathered_events = []
event_count = 0
events = 1
while events:
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    for event in events:
        event_count += 1
        gathered_events.append(event)
print(len(gathered_events))
gathered_events = gathered_events[:len(songs)]
print(len(gathered_events))
print('gatherd_events: ' + str(len(gathered_events)))
count_of_songs=len(songs)-1
mylist = []
for i in range(len(gathered_events)):
    data = gathered_events[i].StringInserts
    for msg in data:
        msg_list = msg.split(',')
        mylist.append(
            songs[count_of_songs - i] + '  ---> ' + msg_list[0] + ", " + msg_list[1] + ", " +
           msg_list[6] + ", " + msg_list[7] + ", " + msg_list[10])

execution_time = int(time.time() - start)
print('It took', execution_time, 'seconds.')

with open(r'C:\Users\Sree\Desktop\Lakshma\my_file.txt', 'w') as f:
    f.write("GROOVE PLAYER OUTPUT : \n\n")
    f.write('It took  ' +str(execution_time)+ '  seconds. \n\n')
    for item in mylist:
        f.write("%s\n" % item)

f = os.startfile(r'C:\Users\Sree\Desktop\Lakshma\my_file.txt')


