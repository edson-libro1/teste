*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}         Chrome
${LOGIN_URL}       https://ledp.inpages.com.br/ebsa/prod/scao/public/ledweb/index.html#/login        
${USUARIO}         vanildo.libro@gmail.com
${SENHA}           pluri123

*** Test Cases ***
Caso de Teste de Login
    Abrir o Navegador
    Acessar a Página de Login
    Preencher o Campo de Usuário
    Preencher o Campo de Senha
    Clicar no Botão de Entrar
    Verificar Login Bem-Sucedido
    Fechar o Navegador
        
*** Keywords ***
Abrir o Navegador
    Open Browser    ${LOGIN_URL}    ${BROWSER}

Acessar a Página de Login
    Go To    ${LOGIN_URL}

Preencher o Campo de Usuário
    Input Text    id:usuario    ${USUARIO}

Preencher o Campo de Senha
    Input Password    id:senha    ${SENHA}

Clicar no Botão de Entrar
    Click Button    id:botao-entrar

Verificar Login Bem-Sucedido
    Wait Until Page Contains Element    id:elemento-de-sucesso    timeout=10s

Fechar o Navegador
    Close Browser
