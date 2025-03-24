import time

def timeToString(specificTime):
    currentTime = time.localtime(specificTime)
    return f"{currentTime[2]}/{currentTime[1]}/{currentTime[0]}:{currentTime[3]}:{currentTime[4]}:{currentTime[5]}"


mytime = str(timeToString(time.time()))
print(mytime)
file = open("camReadTime.txt", "w")
file.write(mytime)