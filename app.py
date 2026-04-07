import streamlit as st 

st.set_page_config(page_title="Analisador de Senhas", page_icon="🛡️")

st.title("🛡️ Analisador de Segurança", anchor=False)
st.subheader("Estágio de Desenvolvimento: Portfólio TI", anchor=False)
senha = st.text_input("Digite sua senha:", type="password"  )

#Listas Vazias
numeros = []
especiais = []
maiu = []
minu = []

#Lógica de processamento
if senha:
    quantidade = len(senha)
    for char in senha:
        if char.isupper():
            maiu.append(char)
        elif char.islower():
            minu.append(char)
        elif char.isnumeric():
            numeros.append(char)
        else:
            especiais.append(char)

    #Cálculo da pontuação
    comprimento = min(quantidade * 5, 40)
    num = min(len(numeros) * 15, 15)
    simbolos = min(len(especiais) * 25, 25)
    if maiu and minu:
        diversidade = 20
    else:
        diversidade = 0
    nota = comprimento + diversidade + num + simbolos

    #Lógica do status
    if comprimento > 0 and diversidade > 0 and num > 0 and simbolos > 0:
        status = 'Status: SENHA APROVADA'
        cor_status = st.success
    else:
        status = 'Status: SENHA REPROVADA'
        cor_status = st.error

    st.divider()
    #Mensagens de retorno
    if 0 <= quantidade <= 4:
        st.info('Sua senha é muito fraca! Pontuação da senha:')
    elif 5 <= quantidade <= 7:
        if maiu and minu and numeros and especiais:
            st.info('Sua senha tem variedade mas é curta! Pontuação da senha:')
        else:
            st.info('Sua senha é fraca! Pontuação da senha:')
    elif 8 <= quantidade <= 9:
        if maiu and minu and numeros and especiais:
            st.info('Sua senha é boa, mas pode ter mais caracteres para ficar melhor! Pontuação da senha:')
        else:
            st.info('Sua senha é boa, mas tem que melhorar a varidedade! Pontuação da senha:')
    elif quantidade >= 10:
        if maiu and minu and numeros and especiais:
            st.info('Sua senha é segura! Pontuação da senha:')
        elif maiu and minu and numeros:
            st.info('Sua senha é grande, mas pode ter caracteres especiais para melhorar ainda mais! Pontuação da senha:')
        else:
            st.info('Sua senha é longa, mas não é forte, falta caracteres especiais, números e diferença entre letras maiúsculas e minúsculas! Pontuação da senha:')

    #Dashboard de resultados
    col1, col2, col3 = st.columns(3)
    with col1:
            st.metric(label="Score Final", value=f"{nota}%")
    with col2:
            st.metric(label="Caracteres", value=quantidade)
    with col3:
            st.metric(label="Tipo", value="Forte" if nota > 80 else "Fraca/Média")

    st.write(f"**Progresso da Segurança:**")
    st.progress(nota)
        
        # Exibe o status final (Verde se aprovado, Vermelho se reprovado)
    cor_status(f"### {status}")
        
    if status == 'SENHA REPROVADA':
        st.write("Critérios faltantes: " + 
            ("❌ Letras " if not (maiu or minu) else "") +
            ("❌ Números " if not numeros else "") +
            ("❌ Símbolos " if not especiais else "") +
            ("❌ Mistura Maiúsc/Minúsc" if not diversidade else ""))

else:
    st.info("Aguardando digitação para iniciar análise...")