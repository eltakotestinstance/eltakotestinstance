import matplotlib.pyplot as plt
import re


def readplotpoints(fileName, firstarray, secondArray, firstcolumn, secondcolumn):
    with open(fileName, 'r') as file:
        content = file.read()

    lines = content.split('\n')

    for line in lines:
        if re.match(r'\d{2}:\d{2}:\d{2}\s+all', line) or re.match(r'\d{2}:\d{2}:\d{2}(\s+\d+)+', line):
            parts = line.split()
            firstarray.append(float(parts[firstcolumn]))
            secondArray.append(float(parts[secondcolumn]))
            #print(f"Time: {parts[0]}, %usr: {parts[2]}, %sys: {parts[4]}")


seconds = list(range(40))


plt.figure(figsize=(10, 6))

"""
CPU Files/Variables

dockerUsr = []
dockerSys = []
k3sUsr = []
k3sSys = []
nativeUsr = []
nativeSys = []
hybridUsr = []
hybridSys = []
aspireUsr = []
aspireSys = []
 
readplotpoints('dockercpu.txt', dockerUsr, dockerSys, 2, 4)
readplotpoints('k3scpu.txt', k3sUsr, k3sSys, 2, 4)
readplotpoints('nativecpu.txt', nativeUsr, nativeSys, 2, 4)
readplotpoints('hybridcpu.txt', hybridUsr, hybridSys, 2, 4)
readplotpoints('aspirecpu.txt', aspireUsr, aspireSys, 2, 4)
"""

"""
All CPU usr graph

plt.plot(seconds, k3sUsr, label='k3s cpu user %')

plt.plot(seconds, nativeUsr, label='native cpu user %')

plt.plot(seconds, dockerUsr, label='docker cpu user %')

plt.plot(seconds, hybridUsr, label='hybrid cpu user %')

plt.plot(seconds, aspireUsr, label='aspire cpu user %')
"""

"""
All CPU Sys graph

plt.plot(seconds, k3sSys, label='k3s cpu system %')

plt.plot(seconds, nativeSys, label='native cpu system %')

plt.plot(seconds, dockerSys, label='docker cpu system %')

plt.plot(seconds, hybridSys, label='hybrid cpu system %')

plt.plot(seconds, aspireSys, label='aspire cpu system %')
"""

"""
Docker Usr/Sys graph

plt.plot(seconds, dockerSys, label='docker cpu system %')

plt.plot(seconds, dockerUsr, label='docker cpu user %')
"""

"""
k3s Usr/Sys graph

plt.plot(seconds, k3sSys, label='k3s cpu system %')

plt.plot(seconds, k3sUsr, label='k3s cpu user %')
"""

"""
native Usr/Sys graph

plt.plot(seconds, nativeSys, label='native cpu system %')

plt.plot(seconds, nativeUsr, label='native cpu user %')
"""

"""
hybrid Usr/Sys graph

plt.plot(seconds, hybridSys, label='hybrid cpu system %')

plt.plot(seconds, hybridUsr, label='hybrid cpu user %')
"""

"""
aspire Usr/Sys graph

plt.plot(seconds, aspireUsr, label='aspire cpu system %')

plt.plot(seconds, aspireSys, label='aspire cpu system %')
"""

"""

END CPU section"""
"""
Memory graph
Files / Variables
"""
dockerUsed = []
dockerReserved = []
k3sUsed = []
k3sReserved = []
nativeUsed = []
nativeReserved = []
hybridUsed = []
hybridReserved = []
aspireUsed = []
aspireReserved = []

dockerNormalUsed = []
dockerNormalReserved = []
dockerWithEmptyUsed = []
dockerWithEmptyReserved = []
k3sNormalUsed = []
k3sNormalReserved = []
k3sWithEmptyUsed = []
k3sWithEmptyReserved = []

readplotpoints('dockermemory.txt', dockerUsed, dockerReserved, 4, 8)
readplotpoints('k3smemory.txt', k3sUsed, k3sReserved, 4, 8)
readplotpoints('nativememory.txt', nativeUsed, nativeReserved, 4, 8)
readplotpoints('hybridmemory.txt', hybridUsed, hybridReserved, 4, 8)
readplotpoints("aspirememory.txt", aspireUsed, aspireReserved, 4, 8)

readplotpoints("dockermemorywith.txt", dockerWithEmptyUsed,dockerWithEmptyReserved, 4, 8)
readplotpoints("dockermemorywithout.txt", dockerNormalUsed, dockerNormalReserved, 4, 8)
readplotpoints("k3smemorywithout.txt", k3sNormalUsed, k3sNormalReserved, 4, 8)
readplotpoints("k3smemorywith.txt", k3sWithEmptyUsed,k3sWithEmptyReserved, 4, 8)

plt.axhline(y=25, color='pink', linestyle='--', label='1 GB Memory')


"""
Memory used All graph

plt.plot(seconds, k3sUsed, label='k3s memory used %')

plt.plot(seconds, nativeUsed, label='native memory used %')

plt.plot(seconds, dockerUsed, label='docker memory used %')

plt.plot(seconds, hybridUsed, label='hybrid memory used %')

plt.plot(seconds, aspireUsed, label='aspire memory used %')
"""

"""
Memory committed All graph

plt.axhline(y=100, color='r', linestyle='--', label='4 GB Memory')

plt.plot(seconds, k3sReserved, label='k3s memory committed %')

plt.plot(seconds, nativeReserved, label='native memory committed %')

plt.plot(seconds, dockerReserved, label='docker memory committed %')

plt.plot(seconds, hybridReserved, label='hybrid memory committed %')

plt.plot(seconds, aspireReserved, label='aspire  memory committed %')
"""

"""
Memory Docker with and without empty Linux container

plt.axhline(y=100, color='r', linestyle='--', label='4 GB Memory')

plt.plot(seconds, dockerNormalUsed, label='docker without emtpy container memory used %')

plt.plot(seconds, dockerNormalReserved, label='docker without emtpy container memory committed %')

plt.plot(seconds, dockerWithEmptyUsed, label='docker with emtpy container memory used %')

plt.plot(seconds, dockerWithEmptyReserved, label='docker with emtpy container memory committed %')
"""

"""
Memory k3s with and without empty Linux container
"""
plt.axhline(y=100, color='r', linestyle='--', label='4 GB Memory')

plt.plot(seconds, k3sWithEmptyUsed, label='k3s with emtpy container memory used %')

plt.plot(seconds, k3sWithEmptyReserved, label='k3s with emtpy container memory committed %')

plt.plot(seconds, k3sNormalUsed, label='k3s without emtpy container memory used %')

plt.plot(seconds, k3sNormalReserved, label='k3s without emtpy container memory committed %')



plt.xlabel('Seconds')
plt.ylabel('Usage')
plt.title('Usage over time')

plt.xticks(rotation=45)

plt.legend()
plt.show()



