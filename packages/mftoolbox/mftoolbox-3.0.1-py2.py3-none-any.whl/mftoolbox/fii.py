from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append('C:\\Users\\coliveira\\OneDrive\\Coding\\Python\\MFToolbox\\mftoolbox')
import funcs
import datetime
#from multiprocessing import Pool, cpu_count
import requests
from tqdm import tqdm
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

test_partial = 0


caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"

STR_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/39.0.2171.95 Safari/537.36',
                      'Cache-Control': 'no-cache'}

def parse_parent_content(_content, _exclude):

    _text = ''

    for i in _content:
        _temp = ''
        if i == '\n':
            continue
        elif i is None:
            continue
        elif i.find(_exclude) != -1:
            continue
        #elif i.find('<span class="value">') is not None:
        if _exclude == 'NOTAS:':
            pass
        if i.string is not None:
            _temp = i.string
            if _text.find(_temp) == -1:
                _text = _text + _temp + ' '

    return _text

def preferencial(_preferencial, _alternativo):

# compara os dois valores e dá a preferência ao primeiro

    if _preferencial == '' or _preferencial is None:
        return _alternativo
    else:
        # elif_alternativo == '' or _alternativo is None or _preferencial != _alternativo:
        return _preferencial

def initializer():
#    global instance_name
    instance_name = 'mp_fii'

def generate_urls(_array, _lista_fiis):
    for codigo_ativo in _lista_fiis:
        _array.append('https://fiis.com.br/' + codigo_ativo)

def scrape(url):
    rqt_site = requests.get(url, headers=STR_HEADER)
    html_soup = BeautifulSoup(rqt_site.text, 'lxml')
    prs_data_detalhes_fiis = html_soup.find_all('td')
    print(url)
    # print(url.replace('http://www.fundamentus.com.br/detalhes.php?papel=',''),len(prs_data_detalhes_ativos))

class ativo():

    def __init__(self):
        ativo.administrador = ''
        ativo.administrador_cnpj = ''
        ativo.administrador_fone = ''
        ativo.adminstrador_email = ''
        ativo.adminstrador_site = ''
        ativo.cnpj = ''
        ativo.codigo = ''
        ativo.cotacao_sobre_vp = ''
        ativo.cotas_emitidas = ''
        ativo.data_base = ''
        ativo.data_base_str = ''
        ativo.data_constituicao = ''
        ativo.data_pagamento = ''
        ativo.data_pagamento_str = ''
        ativo.data_registro_cvm = ''
        ativo.dy = ''
        ativo.dy_acum_12m = ''
        ativo.dy_acum_3m = ''
        ativo.dy_acum_6m = ''
        ativo.dy_ano = ''
        ativo.dy_med_12m = ''
        ativo.dy_med_3m = ''
        ativo.dy_med_6m = ''
        ativo.dy_patrimonial = ''
        ativo.faltou_funds_explorer = False
        ativo.faltou_lupa_fiis = False
        ativo.liquidez_diaria = ''
        ativo.mandato = ''
        ativo.max_52_semanas = ''
        ativo.min_52_semanas = ''
        ativo.nome = ''
        ativo.nome_pregao = ''
        ativo.notas = ''
        ativo.numero_cotas = ''
        ativo.numero_cotistas = ''
        ativo.numero_estados = ''
        ativo.numero_negocios_mes = ''
        ativo.participacao_ifix = ''
        ativo.patrimonio = ''
        ativo.patrimonio_inicial = ''
        ativo.patrimonio_txt = ''
        ativo.prazo = ''
        ativo.publico_alvo = ''
        ativo.quantidade_ativos = ''
        ativo.razao_social = ''
        ativo.rendimento_medio_12m_brl = ''
        ativo.rendimento_medio_12m_perc = ''
        ativo.rentabilidade_acum = ''
        ativo.rentabilidade_patrimonio_acum = ''
        ativo.rentabilidade_patrimonio_periodo = ''
        ativo.rentabilidade_periodo = ''
        ativo.segmento = ''
        ativo.seguidores_fiis_com_br = ''
        ativo.taxa_administracao = ''
        ativo.taxa_consultoria = ''
        ativo.taxa_gerenciamento = ''
        ativo.taxa_gestao = ''
        ativo.taxa_performance = ''
        ativo.taxas = ''
        ativo.ticker = ''
        ativo.tipo = ''
        ativo.tipo2 = ''
        ativo.tipo_anbima = ''
        ativo.tipo_gestao = ''
        ativo.ultima_valorizacao = ''
        ativo.ultimo_preco = ''
        ativo.ultimo_rendimento_brl = ''
        ativo.ultimo_rendimento_perc = ''
        ativo.vacancia_financeira = ''
        ativo.vacancia_fisica = ''
        ativo.valor_inicial = ''
        ativo.valor_patrimonial = ''
        ativo.variacao_12_meses = ''
        ativo.variacao_mes = ''
        ativo.variacao_patrimonial = ''
        ativo.variacao_preco = ''
        ativo.execucao_curta = False


class fii:
    """
    Carrega os dados relevenates dos FIIs
    24/11/19: inicio
    """
    def __init__(self, _array, _registros):


        url = "https://fiis.com.br/lupa-de-fiis/"
        # Chrome opened in silent mode -------------
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        # ------------------------------------------
        '''
        try:
            browser = webdriver.Chrome(chrome_options=options,  service_args=['--silent'])
        except Exception as e:
            browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options,service_args=['--silent'])
        '''
        browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps)
        browser.get(url)
        time.sleep(3)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        temp_array = []
        for id, table in enumerate(soup.find_all("table")):
            if id == 1:
                soup = BeautifulSoup(str(table.contents), "lxml")
                estrutura = [[]]
                dic_estrutura = {}
                for td in soup.find_all('td'):
                    # print(td.__str__())
                    estrutura.append(td.string)
                int_contador_itens = 1
                pbar = tqdm(total=len(estrutura)+1, unit=' ativo')
                while int_contador_itens < len(estrutura):
                    # tem que criar uma nova instância da variável a cada passada
                    # de outro modo, quando faz o append na lista, ao invés de copiar os dados, copia apenas a
                    # referência da variável. quando muda a variável, todos os membros da lista são alterados também,
                    # já que todos os elementos da lista contém referência à variável e não uma cópia dos dados de
                    # cada passada
                    _ativo = ativo()
                    _ativo.ticker = estrutura[int_contador_itens + 0].strip()  # primeira fonte
                    pbar.set_description('Carregando https://fiis.com.br/lupa-de-fiis - ' + _ativo.ticker)
                    dic_estrutura[_ativo.ticker] = len(dic_estrutura)
                    _ativo.codigo = ''.join(i for i in _ativo.ticker if not i.isdigit())
                    _ativo.publico_alvo = estrutura[int_contador_itens + 1]
                    str_tipo = estrutura[int_contador_itens + 2]
                    _ativo.tipo = str_tipo[:str_tipo.find(':')]
                    _ativo.segmento = str_tipo[(str_tipo.find(':')+2):]
                    _ativo.administrador = estrutura[int_contador_itens + 3]  # primeira fonte
                    _ativo.ultimo_rendimento_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 4])
                    _ativo.ultimo_rendimento_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 5])
                    _ativo.data_pagamento_str = estrutura[int_contador_itens + 6]
                    try:
                        _ativo.data_pagamento = datetime.datetime.strptime(_ativo.data_pagamento_str,'%d/%m/%y')
                    except ValueError:
                        _ativo.data_pagamento = None
                    _ativo.data_base_str = estrutura[int_contador_itens + 7]
                    try:
                        _ativo.data_base = datetime.datetime.strptime(_ativo.data_base_str,'%d/%m/%y')
                    except ValueError:
                        _ativo.data_base = None
                    _ativo.rendimento_medio_12m_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 8])
                    _ativo.rendimento_medio_12m_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 9])
                    _ativo.valor_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 10])
                    _ativo.cotacao_sobre_vp = funcs.num_ptb2us(estrutura[int_contador_itens + 11])
                    _ativo.numero_negocios_mes = funcs.num_ptb2us(estrutura[int_contador_itens + 12])
                    _ativo.participacao_ifix = funcs.num_ptb2us(estrutura[int_contador_itens + 13])
                    _ativo.numero_cotistas = funcs.num_ptb2us(estrutura[int_contador_itens + 14])
                    _ativo.patrimonio = funcs.num_ptb2us(estrutura[int_contador_itens + 15])

                    int_contador_itens = int_contador_itens + 16
                    #print(int_contador_itens)
                    temp_array.append(_ativo)
                    del _ativo
                    pbar.update(16)
                pbar.close()

        browser.close()
        browser.quit()

        url = "https://www.fundsexplorer.com.br/ranking"
        # Chrome opened in silent mode -------------
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        # ------------------------------------------
        # browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps)
        browser.get(url)
        #time.sleep(3)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")

        for id, table in enumerate(soup.find_all("table")):
            if id == 0:
                soup = BeautifulSoup(str(table.contents), "lxml")
                estrutura = [[]]
                for td in soup.find_all('td'):
                    # print(td.__str__())
                    estrutura.append(td.string)
                int_contador_itens = 1
                pbar = tqdm(total=len(estrutura) + 1, unit=' ativo')
                while int_contador_itens < len(estrutura):
                    try:
                        int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 0].strip())
                        pbar.set_description('Carregando https://www.fundsexplorer.com.br/ranking - ' + estrutura[int_contador_itens + 0].strip())
                        temp_array[int_pointer].tipo2 = estrutura[int_contador_itens + 1].strip() # primeira fonte
                        temp_array[int_pointer].ultimo_preco = funcs.num_ptb2us([int_contador_itens + 2]) # primeira fonte
                        temp_array[int_pointer].liquidez_diaria = funcs.num_ptb2us(estrutura[int_contador_itens + 3]) # primeira fonte
                        temp_array[int_pointer].dy_acum_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 6])  # primeira fonte
                        temp_array[int_pointer].dy_acum_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 7]) # primeira fonte
                        temp_array[int_pointer].dy_acum_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 8]) # primeira fonte
                        temp_array[int_pointer].dy_med_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 9]) # primeira fonte
                        temp_array[int_pointer].dy_med_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 10]) # primeira fonte
                        temp_array[int_pointer].dy_med_12m =funcs.num_ptb2us( estrutura[int_contador_itens + 11]) # primeira fonte
                        temp_array[int_pointer].dy_ano = funcs.num_ptb2us(estrutura[int_contador_itens + 12]) # primeira fonte
                        temp_array[int_pointer].variacao_preco = funcs.num_ptb2us(estrutura[int_contador_itens + 13]) # primeira fonte
                        temp_array[int_pointer].rentabilidade_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 14]) # primeira fonte
                        temp_array[int_pointer].rentabilidade_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 15]) # primeira fonte
                        temp_array[int_pointer].dy_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 19]) # primeira fonte
                        temp_array[int_pointer].variacao_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 20]) # primeira fonte
                        temp_array[int_pointer].rentabilidade_patrimonio_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 21]) # primeira fonte
                        temp_array[int_pointer].rentabilidade_patrimonio_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 22]) # primeira fonte
                        try:
                            temp_array[int_pointer].vacancia_fisica = funcs.num_ptb2us(estrutura[int_contador_itens + 23]) # primeira fonte
                        except:
                            pass
                        try:
                            temp_array[int_pointer].vacancia_financeira = funcs.num_ptb2us(estrutura[int_contador_itens + 24]) # primeira fonte
                        except:
                            pass
                        temp_array[int_pointer].quantidade_ativos = estrutura[int_contador_itens + 25].strip() # primeira fonte
                        temp_array[int_pointer].faltou_funds_explorer = False
                    except:
                        _ativo = ativo()
                        _ativo.ticker = estrutura[int_contador_itens + 0].strip()
                        pbar.set_description('Carregando https://www.fundsexplorer.com.br/ranking - ' + _ativo.ticker)
                        _ativo.codigo = ''.join(i for i in _ativo.ticker if not i.isdigit())
                        dic_estrutura[_ativo.ticker] = len(dic_estrutura)
                        _ativo.faltou_faltou_lupa_fiis = True
                        _ativo.tipo2 = estrutura[int_contador_itens + 1].strip()
                        _ativo.ultimo_preco = funcs.num_ptb2us([int_contador_itens + 2])
                        _ativo.liquidez_diaria = funcs.num_ptb2us(estrutura[int_contador_itens + 3])
                        _ativo.ultimo_rendimento_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 4])
                        _ativo.ultimo_rendimento_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 5])
                        _ativo.dy_acum_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 6])
                        _ativo.dy_acum_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 7])
                        _ativo.dy_acum_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 8])
                        _ativo.dy_med_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 9])
                        _ativo.dy_med_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 10])
                        _ativo.dy_med_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 11])
                        _ativo.dy_ano = funcs.num_ptb2us(estrutura[int_contador_itens + 12])
                        _ativo.variacao_preco = funcs.num_ptb2us(estrutura[int_contador_itens + 13])
                        _ativo.rentabilidade_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 14])
                        _ativo.rentabilidade_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 15])
                        _ativo.patrimonio = funcs.num_ptb2us(estrutura[int_contador_itens + 16])
                        _ativo.valor_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 17])
                        _ativo.cotacao_sobre_vp = funcs.num_ptb2us(estrutura[int_contador_itens + 18])
                        _ativo.dy_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 19])
                        _ativo.variacao_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 20])
                        _ativo.rentabilidade_patrimonio_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 21])
                        _ativo.rentabilidade_patrimonio_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 22])
                        try:
                            _ativo.vacancia_fisica = funcs.num_ptb2us(estrutura[int_contador_itens + 23])
                        except:
                            pass
                        try:
                            _ativo.vacancia_financeira = funcs.num_ptb2us(estrutura[int_contador_itens + 24])
                        except:
                            pass
                        _ativo.quantidade_ativos = funcs.num_ptb2us(estrutura[int_contador_itens + 25])
                        temp_array.append(_ativo)

                    int_contador_itens = int_contador_itens + 26
                    pbar.update(26)
                pbar.close()

        browser.close()
        browser.quit()
        if _registros is None:
            _registros = len(dic_estrutura)

        if test_partial <= 1:
            start = datetime.datetime.now()
            lap = datetime.datetime.now()
            pbar = tqdm(total=_registros, unit=' ativo')

            #for ticker in take(_registros, dic_estrutura.keys()):
            for ticker in {k: dic_estrutura[k] for k in list(dic_estrutura)[:_registros]}:
                url = 'https://fiis.com.br/' + ticker
                pbar.set_description(url)
                #url = 'file:///C:/Users/coliveira/OneDrive/Coding/Python/FII/ANCR11B%20-%20Ancar%20IC%20-%20Fundo%20de%20Investimento%20Imobili%C3%A1rio.html'

                ''' 
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                # ------------------------------------------
                try:
                    browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'])
                except Exception as e:
                    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_args=['--silent'])
    
                browser.get(url)
                time.sleep(3)
                html = browser.page_source
                '''
                browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps)
                browser.get(url)
                html = browser.page_source
                #time.sleep(3)
                # r = requests.get(url, headers=STR_HEADER)
                soup = BeautifulSoup(html, 'lxml')
                estrutura = [[]]
                for td in soup.find_all('span'):
                    # print(td.__str__())
                    try:
                        _temp = parse_parent_content(td.parent.contents, td.string)
                    except Exception as e:
                        print(e)
                    if _temp == '':
                        estrutura.append(td.string)
                    else:
                        estrutura.append(_temp.replace('\n', '').strip())
                    # print(td.string, 'len parent contents = ', len(td.parent.contents), 'parent contents= ', td.parent.contents)

                int_contador_itens = 1
                #while int_contador_itens < len(estrutura):
                #int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 5].strip())
                int_pointer = dic_estrutura.get(ticker)


                temp_array[int_pointer].seguidores_fiis_com_br = funcs.num_ptb2us(estrutura[int_contador_itens + 4]) # primeira fonte
                temp_array[int_pointer].nome = estrutura[int_contador_itens + 6].strip() # primeira fonte
                temp_array[int_pointer].administrador = preferencial(temp_array[int_pointer].administrador,estrutura[int_contador_itens + 8].strip())
                temp_array[int_pointer].administrador_cnpj = estrutura[int_contador_itens + 9]
                temp_array[int_pointer].administrador_fone  = estrutura[int_contador_itens + 11]
                temp_array[int_pointer].adminstrador_email  = estrutura[int_contador_itens + 13]
                temp_array[int_pointer].adminstrador_site  = estrutura[int_contador_itens + 15]
                temp_array[int_pointer].nome_pregao  = estrutura[int_contador_itens + 18] # primeira fonte
                str_tipo = estrutura[int_contador_itens + 20]
                temp_array[int_pointer].tipo = preferencial(temp_array[int_pointer].tipo ,str_tipo[:str_tipo.find(':')])
                temp_array[int_pointer].segmento = preferencial(temp_array[int_pointer].segmento, str_tipo[(str_tipo.find(':') + 2):])
                temp_array[int_pointer].tipo_anbima  = estrutura[int_contador_itens + 22]
                temp_array[int_pointer].data_registro_cvm  = estrutura[int_contador_itens + 24]
                temp_array[int_pointer].numero_cotas  = funcs.num_ptb2us(estrutura[int_contador_itens + 26])
                temp_array[int_pointer].numero_cotistas  = preferencial(temp_array[int_pointer].numero_cotistas,funcs.num_ptb2us(estrutura[int_contador_itens + 28]))
                temp_array[int_pointer].cnpj  = estrutura[int_contador_itens + 30]
                temp_array[int_pointer].notas  = estrutura[int_contador_itens + 31]
                temp_array[int_pointer].taxas = estrutura[int_contador_itens + 32]
                temp_array[int_pointer].dy = funcs.num_ptb2us(estrutura[int_contador_itens + 34])
                temp_array[int_pointer].ultimo_rendimento_brl  = preferencial(temp_array[int_pointer].ultimo_rendimento_brl,funcs.num_ptb2us(estrutura[int_contador_itens + 37]))
                temp_array[int_pointer].patrimonio_txt  = estrutura[int_contador_itens + 40]
                temp_array[int_pointer].valor_patrimonial  = preferencial(temp_array[int_pointer].valor_patrimonial,funcs.num_ptb2us(estrutura[int_contador_itens + 43]))
                temp_array[int_pointer].ultimo_preco  = preferencial(temp_array[int_pointer].ultimo_preco, funcs.num_ptb2us(estrutura[int_contador_itens + 47]))
                temp_array[int_pointer].ultima_valorizacao  = funcs.num_ptb2us(estrutura[int_contador_itens + 48])
                temp_array[int_pointer].min_52_semanas  = funcs.num_ptb2us(estrutura[int_contador_itens + 51])
                temp_array[int_pointer].max_52_semanas  = funcs.num_ptb2us(estrutura[int_contador_itens + 54])
                temp_array[int_pointer].variacao_12_meses  = funcs.num_ptb2us(estrutura[int_contador_itens + 57])
                temp_array[int_pointer].execucao_curta = True

                # print('Ativo: %s, Lap: %s, Total: %s' % (temp_array[int_pointer].ticker, str(datetime.datetime.now()-lap), str(datetime.datetime.now()-start)))
                browser.close()
                browser.quit()
                lap = datetime.datetime.now()
                pbar.update(1)
            pbar.close()

        if test_partial <=2:
            start = datetime.datetime.now()
            lap = datetime.datetime.now()
            pbar = tqdm(total=_registros, unit=' ativo')
            #for ticker in take(_registros, dic_estrutura.keys()):
            for ticker in {k: dic_estrutura[k] for k in list(dic_estrutura)[:_registros]}:
                url = 'https://www.fundsexplorer.com.br/funds/' + ticker
                pbar.set_description(url)
                # url = 'file:///C:/Users/coliveira/OneDrive/Coding/Python/FII/ANCR11B%20-%20Ancar%20IC%20-%20Fundo%20de%20Investimento%20Imobili%C3%A1rio.html'

                ''' 
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                # ------------------------------------------
                try:
                    browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'])
                except Exception as e:
                    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_args=['--silent'])
    
                browser.get(url)
                time.sleep(3)
                html = browser.page_source
                '''
                browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps)
                browser.get(url)
                html = browser.page_source
                # time.sleep(3)
                # r = requests.get(url, headers=STR_HEADER)
                soup = BeautifulSoup(html, 'lxml')
                estrutura = [[]]
                for td in soup.find_all('span'):
                    # print(td.__str__())
                    try:
                        _temp = parse_parent_content(td.parent.contents, td.string)
                    except Exception as e:
                        print(e)
                    if _temp == '':
                        estrutura.append(td.string)
                    else:
                        estrutura.append(_temp.replace('\n', '').strip())
                    # print(td.string, 'len parent contents = ', len(td.parent.contents), 'parent contents= ', td.parent.contents)

                int_contador_itens = 1
                # while int_contador_itens < len(estrutura):
                # int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 5].strip())
                int_pointer = dic_estrutura.get(ticker)
                if ticker == 'ATSA11':
                    ticker = ticker
                    # print(ticker)
                if estrutura[1] != 'Ops! Algo está errado...':
                    __posição = 29; temp_array[int_pointer].ultimo_preco = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].ultimo_preco)
                    __posição = 30; temp_array[int_pointer].ultima_valorizacao = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].ultima_valorizacao)
                    __posição = 33; temp_array[int_pointer].liquidez_diaria = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].liquidez_diaria)
                    __posição = 35; temp_array[int_pointer].ultimo_rendimento_brl = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].ultimo_rendimento_brl)
                    __posição = 37; temp_array[int_pointer].dy = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].dy)
                    __posição = 39; temp_array[int_pointer].patrimonio_txt = preferencial(estrutura[int_contador_itens + __posição], temp_array[int_pointer].patrimonio_txt)
                    __posição = 41; temp_array[int_pointer].valor_patrimonial = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].valor_patrimonial)
                    __posição = 43; temp_array[int_pointer].variacao_mes = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].variacao_mes)
                    __posição = 45; temp_array[int_pointer].cotacao_sobre_vp = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].cotacao_sobre_vp)
                    __posição = 52; temp_array[int_pointer].razao_social = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].razao_social)
                    __posição = 54; temp_array[int_pointer].data_constituicao = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].data_constituicao)
                    __posição = 56; temp_array[int_pointer].cotas_emitidas = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].cotas_emitidas)
                    __posição = 58; temp_array[int_pointer].patrimonio_inicial = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].patrimonio_inicial)
                    __posição = 60; temp_array[int_pointer].valor_inicial = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].valor_inicial)
                    __posição = 62; temp_array[int_pointer].tipo_gestao = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].tipo_gestao)
                    __posição = 64; temp_array[int_pointer].taxa_performance = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].taxa_performance)
                    __posição = 66; temp_array[int_pointer].taxa_gestao = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].taxa_gestao)
                    __posição = 68; temp_array[int_pointer].cnpj = preferencial(estrutura[int_contador_itens + __posição], temp_array[int_pointer].cnpj)
                    __posição = 70; temp_array[int_pointer].publico_alvo = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].publico_alvo)
                    __posição = 72; temp_array[int_pointer].mandato = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].mandato)
                    __posição = 74; temp_array[int_pointer].segmento = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].segmento)
                    __posição = 76; temp_array[int_pointer].prazo = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].prazo)
                    __posição = 78; temp_array[int_pointer].taxa_administracao = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].taxa_administracao)
                    __posição = 80; temp_array[int_pointer].taxa_gerenciamento = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].taxa_gerenciamento)
                    __posição = 82; temp_array[int_pointer].taxa_consultoria = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].taxa_consultoria)
                    __posição = 106; temp_array[int_pointer].numero_estados = preferencial(funcs.num_ptb2us(estrutura[int_contador_itens + __posição]), temp_array[int_pointer].numero_estados)
                    temp_array[int_pointer].execucao_curta = True
                '''  
                print('2 passada, Ativo: %s, Lap: %s, Total: %s' % (
                temp_array[int_pointer].ticker, str(datetime.datetime.now() - lap), str(datetime.datetime.now() - start)))
                '''
                browser.close()
                browser.quit()
                lap = datetime.datetime.now()
                pbar.update(1)
            pbar.close()




        '''
        all_urls = list()

        generate_urls(all_urls, dic_estrutura.keys())

        #start_time = datetime.now()
        # for url in tqdm(all_urls):
        #    scrape(url)
        # print('In Line: '+str((datetime.now()-start_time)))
        # exit()

        cpus = cpu_count()
        # pbar = tqdm(all_urls)
        #if __name__ == '__main__':
        global instance_name
        if instance_name == 'fii':
            # print('Starting parallel processing')
            p = Pool(cpus,initializer=initializer())
            try:
                p.map(scrape, tqdm(all_urls, desc='Processamento paralelo', leave=True))
            except Exception as e:
                print(e)
            p.terminate()
            p.join()
            #print('Tempo total: ' + str((datetime.now() - start_time)))

        '''



        for item in temp_array:
            if item.execucao_curta == True:
                _array.append(item)


        #_array.append(temp_array)
