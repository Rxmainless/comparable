import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Título da aplicação
st.title("Comparativo de Cargos: Comercial Administrativo vs Auxiliar Administrativo")

# Barra lateral para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Escolha uma página:", ("Comparativo de Cargos", "Motivos para Troca de Setor", "Análise SWOT"))

# ---- Página de Comparativo de Cargos ----
if page == "Comparativo de Cargos":
    # Introdução
    st.write("""
    Este comparativo analisa as funções de **Comercial Administrativo** e **Auxiliar Administrativo** em uma corretora de seguros. 
    O objetivo é explorar as responsabilidades, habilidades necessárias e o impacto de cada cargo nas operações da empresa.
    """)

    # Seletor de cargo
    selected_role = st.radio(
        "Escolha o cargo para ver os detalhes:",
        ('Comercial Administrativo', 'Auxiliar Administrativo')
    )

    # Dados comparativos
    comercial_tarefas = [
        "Suporte ao time de vendas (preparação de propostas, apresentações)",
        "Atendimento ao cliente (comercial)",
        "Acompanhamento de propostas e follow-ups",
        "Renovação de apólices",
        "Captação e prospecção de clientes (em alguns casos)"
    ]

    auxiliar_tarefas = [
        "Organização de documentos e apólices",
        "Acompanhamento de sinistros",
        "Atualização de cadastros e sistemas",
        "Controle de pagamentos e emissão de boletos",
        "Elaboração de relatórios administrativos"
    ]

    # Descrições
    comercial_descricao = """
    - **Foco Principal**: Apoio ao time de vendas com foco em resultados.
    - **Pressão**: Pode haver pressão indireta por resultados comerciais.
    - **Habilidades**: Boa comunicação, multitarefa e conhecimento comercial são necessários.
    """

    auxiliar_descricao = """
    - **Foco Principal**: Trabalho focado em organização e processos internos.
    - **Pressão**: Menos pressão, com foco em prazos e organização de processos.
    - **Habilidades**: Organização, atenção a detalhes e habilidades operacionais.
    """

    # Mostrando os detalhes conforme a escolha do usuário
    if selected_role == 'Comercial Administrativo':
        st.subheader("Comercial Administrativo")
        st.write(comercial_descricao)
        st.subheader("Tarefas Típicas")
        st.table(pd.DataFrame(comercial_tarefas, columns=["Tarefas Típicas"]))

    else:
        st.subheader("Auxiliar Administrativo")
        st.write(auxiliar_descricao)
        st.subheader("Tarefas Típicas")
        st.table(pd.DataFrame(auxiliar_tarefas, columns=["Tarefas Típicas"]))

    # Comparação em Tabela
    st.subheader("Comparação entre Comercial Administrativo e Auxiliar Administrativo")

    data = {
        "Critério": ["Foco Principal", "Envolvimento com Vendas", "Pressão", "Habilidades Necessárias"],
        "Comercial Administrativo": ["Suporte a vendas", "Indireto", "Pressão por resultados",
                                     "Comunicação, multitarefa"],
        "Auxiliar Administrativo": ["Organização", "Nenhum", "Menos pressão", "Organização, atenção a detalhes"]
    }

    df = pd.DataFrame(data)
    st.table(df)

    # Gráfico de Barras
    habilidades = ['Comunicação', 'Organização', 'Multitarefa', 'Atenção a Detalhes']
    comercial_habilidades = [5, 4, 5, 2]
    auxiliar_habilidades = [3, 5, 2, 4]

    habilidade_data = pd.DataFrame({
        'Habilidade': habilidades,
        'Comercial Administrativo': comercial_habilidades,
        'Auxiliar Administrativo': auxiliar_habilidades
    })

    st.subheader("Comparação de Habilidades Necessárias")
    fig, ax = plt.subplots()
    habilidade_data.set_index('Habilidade').plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'])
    plt.title('Comparação de Habilidades entre Cargos')
    plt.ylabel('Nível de Importância (1 a 5)')
    plt.xlabel('Habilidades')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Conclusão ou Chamado à Ação
    st.write("""
    ### Conclusão
    Com base na análise acima, o cargo de **Auxiliar Administrativo** parece se alinhar mais com minhas preferências e habilidades, permitindo-me contribuir de maneira mais eficaz para a equipe.
    """)

# ---- Página de Motivos para Troca de Setor ----
elif page == "Motivos para Troca de Setor":
    st.header("Motivos para Troca de Setor")

    st.write("""
    A decisão de migrar do cargo de **Comercial Administrativo** para **Auxiliar Administrativo** baseia-se em várias considerações importantes:
    """)

    st.subheader("1. Alinhamento com Habilidades e Interesses")
    st.write("""
    O cargo de Auxiliar Administrativo está mais alinhado com minhas habilidades organizacionais e preferências profissionais. 
    Enquanto o trabalho comercial envolve pressão e foco em resultados de vendas, o papel administrativo permite um ambiente mais estruturado, onde posso usar minhas habilidades para contribuir para a eficiência da equipe.
    """)

    st.subheader("2. Menor Pressão e Estresse")
    st.write("""
    O ambiente de vendas pode ser altamente estressante, com metas agressivas e a necessidade de fechamento constante de negócios. 
    A migração para o Auxiliar Administrativo reduzirá a pressão, permitindo-me trabalhar em um ritmo mais sustentável e saudável.
    """)

    st.subheader("3. Oportunidade de Crescimento Profissional")
    st.write("""
    O cargo de Auxiliar Administrativo oferece oportunidades de aprendizado e desenvolvimento em áreas administrativas, que considero valiosas para minha carreira a longo prazo. 
    Isso me permitirá adquirir novas habilidades que podem ser aplicadas em diversas áreas dentro da corretora.
    """)

    st.subheader("4. Contribuição para a Equipe")
    st.write("""
    Ao migrar para o Auxiliar Administrativo, poderei apoiar a equipe de vendas de uma maneira diferente, fornecendo o suporte administrativo necessário para que eles se concentrem em suas metas comerciais. 
    Essa colaboração pode resultar em uma operação mais coesa e eficiente.
    """)

    st.subheader("5. Maior Satisfação Pessoal")
    st.write("""
    Finalmente, a mudança para o Auxiliar Administrativo é uma decisão que visa minha satisfação pessoal e profissional. 
    Estou convencido de que desempenhando funções que me agradam e nas quais posso brilhar, contribuirei melhor para o sucesso da equipe e da corretora.
    """)

# ---- Página de Análise SWOT ----
elif page == "Análise SWOT":
    st.header("Análise SWOT Pessoal")

    # Tabela SWOT
    swot_data = {
        "Forças": [
            "Habilidades organizacionais e administrativas sólidas",
            "Experiência em suporte à equipe de vendas",
            "Capacidade de trabalhar de forma independente e em equipe",
            "Habilidade em criar análises de dados usando Streamlit"
        ],
        "Fraquezas": [
            "Falta de experiência direta em vendas",
            "Ansiedade em ambientes de alta pressão",
            "Necessidade de desenvolver algumas habilidades específicas"
        ],
        "Oportunidades": [
            "Crescimento e desenvolvimento na área administrativa",
            "Oportunidade de aprender novas habilidades relevantes",
            "Contribuição significativa para a eficiência da equipe de vendas"
        ],
        "Ameaças": [
            "Mudanças nas prioridades da empresa que podem impactar a posição",
            "Concorrência interna por cargos administrativos",
            "Desafios relacionados à adaptação a um novo papel"
        ]
    }

    swot_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in swot_data.items()]))
    st.table(swot_df)

    st.write("""
    Esta análise SWOT ajuda a identificar onde estou me saindo bem e onde posso melhorar, além de mostrar as oportunidades e ameaças que podem impactar minha transição para o cargo de Auxiliar Administrativo.
    """)

    # Design Visual com Gráfico de Radar
    st.subheader("Visualização da Análise SWOT")
    labels = np.array(['Habilidades organizacionais', 'Experiência em suporte', 'Capacidade de trabalho',
                       'Análise de dados', 'Experiência em vendas', 'Trabalho sob pressão',
                       'Desenvolvimento de habilidades'])

    # Habilidades do Cargo de Auxiliar Administrativo
    stats = np.array([4, 4, 4, 5, 2, 2, 4])  # Exemplo de pontos (4 para organizacionais, 5 para análise de dados, etc.)

    # Gráfico de Radar
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    stats = np.concatenate((stats, [stats[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='orange', alpha=0.25)
    ax.plot(angles, stats, color='orange', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title('Radar de Habilidades Pessoais', size=20)
    st.pyplot(fig)

