
import glob

print ('Named explicitly:')
for name in glob.glob('D:/GitHub Project/Telegrambot/sartools/*'):
    print ('\t', name)

print ('Named with wildcard:')
for name in glob.glob('D:/GitHub Project/Telegrambot/*/*'):
    print ('\t', name)