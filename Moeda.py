import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def abrirBrowser():
    try:
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.bcb.gov.br/conversao');
        return driver
    except:
        return -1

def selecionaLista( driver, nomeBotao, nomeCampo, valor):
    try:
        xPath ="//ul[@id='" + nomeCampo + "']/li/a[contains(text(),'" + valor + "')]"
        print(f'xPath=<{xPath}>')
        botoes = driver.find_elements_by_id(nomeBotao)
        for botao in botoes:
            botao.click()
        moeda = driver.find_element_by_xpath(xPath)
        moeda.click()
        return True
    except:
        return False
    
def Converter( moedaOrigem, moedaDestino, dataConversao, qtd):
    cotacao = -1
    try:
        driver = abrirBrowser()
    except:
        mensagem = 'Erro na abertura do browser'

    print(f'RECEBIDO: Origem {moedaOrigem} Destino {moedaDestino} Qtd {qtd} Data {dataConversao}')

    try:
        mensagem = 'Erro na campo Data'
        driver.find_element_by_name('inputDate').send_keys(dataConversao)

        mensagem = 'Erro na campo de Quantidade de moedas'
        driver.find_element_by_name("valorBRL").send_keys(qtd)

        if not selecionaLista(driver, 'button-converter-de', 'moedaBRL', moedaOrigem):
            mensagem = 'Erro na seleção da Moeda Origem'

        elif not selecionaLista( driver, 'button-converter-para', 'moedaResultado1', moedaDestino):
            mensagem =  'Erro na seleção da Moeda Destino'

        else:
            mensagem = 'Erro no click do botão'
            driver.find_element_by_xpath("//button[@title='Converter']").click()
        
            driver.implicitly_wait(10)  # 10 segundos
            #time.sleep(5)
        
            mensagem = 'Erro na busca do resultado'
            Result1 = driver.find_element_by_class_name('card-body')
            b = re.search('conversão: (.+?\s)Data cotação', Result1.text)
            if b:
                cotacao = float(b.group(1).replace(',','').replace('\n',''))
            mensagem = ''
    except:
        cotacao = -1

    driver.quit()
    print(f'RESULTADO: Cotação {cotacao} Mensagem: {mensagem}')
    return cotacao, mensagem


