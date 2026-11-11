# Cria a lista com o nodo sigla, nomeEstado e um ponteiro
class ElementoDaListaSimples:
    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    # Inserção no início da lista
    def inserirNoInicio(self, sigla, nomeEstado):
        nodo = ElementoDaListaSimples(sigla, nomeEstado)
        if  self.head is None:
            self.head = nodo
            return 0
        else:
            nodo.proximo = self.head
            self.head = nodo
            return 0

    # Formatação do texto
    def imprimir(self):
        temp = self.head
        while temp:
            print(f'{temp.sigla}->', end='')
            temp = temp.proximo
        print('None')

# Cria a TabelaHash com 10 posições e valor inicial None
class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.h = [None] * self.tam

    # Retorna DF na posição 7
    def hashFunc(self, k):
        if k == 'DF':
            return 7

        k = list(k)
        return (ord(k[0]) + ord(k[1])) % self.tam


    def inserir(self, sigla, nomeEstado):
        pos = self.hashFunc(sigla)
        if self.h[pos] is None:
            self.h[pos] = ListaEncadeadaSimples()
        add = self.h[pos].inserirNoInicio(sigla, nomeEstado)

    def imprimir(self):
        for i in range(self.tam):

            print(f'{i}: ', end='')
            if self.h[i] is None:
                print('None')
            else:
                self.h[i].imprimir()



# Programa principal
Teste = TabelaHash()

#Impressão da tabela hash vazia
print('TABELA HASH VAZIA')
Teste.imprimir()
print('\n')


# Lista que armazena os estados
estados_brasil = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goias'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]

#Impressão com os 26 estados + DF
for sigla, nomeEstado in estados_brasil:
    Teste.inserir(sigla, nomeEstado)
print('TABELA COM OS 26 ESTADOS + DF')
Teste.imprimir()
print('\n')

#Impressão com o estado fictício(nome do aluno)
Teste.inserir('RR', 'RUAN DE AQUINO ROSA')
print('TABELA COMPLETA COM ESTADO FICTÍCIO')
Teste.imprimir()
