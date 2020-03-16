#Analisando determinado processo do Windows

import psutil as ps 

class checkProc:
    def __init__(self):
        self.process = ' '
        self.pc = ' '
        self.exist = ' '
        super().__init__()

    def checkProcess (self):
        self.process = ("chrome")
        self.pc = (self.process + '.exe')

        qtd_process = []

        for proc in ps.process_iter():
            self.info = proc.as_dict(attrs=['name', 'status'])

            #Setar o dicionario em lowercase
            #self.info = {k.lower(): v.lower() for k, v in self.info.items()}

            #Analisando processos
            for akey in self.info.keys():
                self.exist = self.info[akey]
                
                if self.exist == self.pc:
                    self.true = 1
                    qtd_process.append(self.true)
                else:
                    self.false = 0

        #Atestando se o processo está rodando ou não
        if len(qtd_process) != 0:
            print ("O Processo", self.process, "está ativo")
        if len(qtd_process) == 0:
            print ("O Processo", self.process, "está desligado")


run = checkProc()
run.checkProcess()
