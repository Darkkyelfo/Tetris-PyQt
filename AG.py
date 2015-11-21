import operator
import Agente
import random


class AG(object):
    self.populacao = []
    self.melhorAgente = None
    #executa o AG
    def runAG(self,numPopulacao,PopElite,PopMutante,geracoes,probCruzamento,jogosPorAgente):
        
        geracaoAtual = 0
        #cria a população inicial aleatoria
        for i in range(numPopulacao):
            agente = Agente()
            populacao.append(agente)
        #codição de parada do AG por numero de gerações
        while geracaoAtual <= geracoes:

            #coloca os agentes para jogar(incompleto)
            threadLock = threading.Lock()
            threads = []


            #calcula o desepenho dos agentes com a media de tetrises pela quantidade de jogos
            quantidade = 0
            for agente in self.populacao:
                for tetrises in agente.tetrisesFeitas:
                    quantidade += tetrises;
                agente.desempenho = quantidade/jogosPorAgente
            #ordena a populacao do melhor agente para o pior
            self.populacao.sort(Key=operator.attrgetter('desempenho'),reverse=True)
            #seleciona o melhor agente
            self.melhorAgente = populacao[0]

            Elite = []
            N_Elite = []
            Mutante = []
            #seleciona a populacao elite e a n_elite
            for i in range(numPopulacao):
                if(i < PopElite):
                    Elite[i] = populacao[i]
                else:
                     N_Elite[i] = populacao[i]
            #gera a um populacao de mutantes
            for i in range(PopMutante):
                agente = Agente()
                Mutante.append(agente)
            #adiciona os elites e os mutantes a nova populacao         
            novaPopulacao = []  
            novaPopulacao += Elite            
            novaPopulacao += Mutante
            filhos = []
            #gera o resto da nova populacao atraves do cruzamento de um pai elite e um não elite 
            for i in range(numPopulacao - PopElite - PopMutante):
                paiElite = random.choice(Elite)
                paiNaoElite = random.choice(N_Elite)
                filhos = Agente()
                for i in range(Agente.Agente.qtGenes):
                    if(random.random() < probCruzamento ):
                        filho.genes[i] = paiElite.genes[i]
                    else:
                        filho.genes[i] = paiNaoElite.genes[i]  
                filhos.append(filho)

            novaPopulacao+=filhos
            
            self.populacao = novaPopulacao      
            
            print("geracao: "+geracaoAtual+"\n"+self.melhorAgente.genes)
                  
            geracaoAtual+=1