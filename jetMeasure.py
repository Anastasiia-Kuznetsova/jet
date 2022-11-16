import jetFunctions as jet
import time
try:
    jet.initStepMotorGpio()
    jet.initSpiAdc()

    x0 = 0
    x = [] #шаги в шагах
    measures = [] #данные в отсчётах ацп
    for i in range(140):
        time.sleep(0.05)
        adc = jet.getAdc()
        measures.append(adc)
        x.append(x0)
        jet.stepForward(5)
        x0 += 5
    # for i in range(500):
    #     adc = jet.getAdc()
    #     measures.append(adc)
finally:
    with open("/home/b01-101/Desktop/jet/data/0.txt", "w") as f:
        #f.write("- Jet Lab\n\n")
        #f.write("Date: " +str( time.localtime(time.time()))+ "\n")
        #f.write("Step: 5 motor steps \n\n")
        print(*measures, file=f, sep="\n")
    with open("/home/b01-101/Desktop/jet/data/x.txt", "w") as f:
        print(*x, file=f, sep="\n")
    jet.stepBackward(700)
    jet.deinitStepMotorGpio()
    jet.deinitSpiAdc()

#3.6 сантиметра за 650 шагов
#1мм за 18 шагов примерно