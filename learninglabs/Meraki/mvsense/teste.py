import time

end_time = time.time() + 20
countTimer = 0
sleepTime = 1.000
while time.time() < end_time:
    time.sleep(sleepTime)
    countTimer += sleepTime
    print('hello, ja passaram {} secs'.format(countTimer))

    if countTimer == 5.0:
        print ("Rodando o Codigo Novamente")