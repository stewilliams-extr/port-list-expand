#This will expand a port list
portlst = ["1", "1-2", "1-3", "1:1", "1:1-3", "1:1,1:2", "1:1,2:2,2:10-12", "1/1", "1/1-5", "1/10,1/13,2/10-13"]

def lstexpand(ports):
    expandport = []
    portlst = []

    if "," in ports:
        portlst = ports.split(',')
    else:
        portlst.append(ports)

    for oneport in portlst:
        #Check if port using : or not
        if ":" in oneport or "/" in oneport:
            if "/" in oneport:
                delimiter = "/"
                stack = oneport.split("/")
            if ":" in oneport:
                delimiter = ":"
                stack = oneport.split(":")
            slot = stack[0]
            #print ("#{0}#".format(stack[0]))
            port = stack[1]
        else:
            #print ("#{0}#".format(oneport))
            slot = 0
            port = oneport

        #checking to see if a port is a list or not
        if "-" not in port:
            expandport.append(oneport)
            continue
        #Starting to expand list
        portrange = port.split("-")
        portrange[0] = int(portrange[0])
        portrange[1] = int(portrange[1])
        for port in range(portrange[0], portrange[1] + 1):
            if slot == 0:
                expandport.append(port)
            else:
                expandport.append(str(slot) + (delimiter) + str(port))
    return expandport

for ports in portlst:
    print ("port in is {0}, and the list is {1}".format(ports, lstexpand(ports)))
