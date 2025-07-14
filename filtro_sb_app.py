import streamlit as st

def filtrar_codigos_sb_streamlit():
    """
    Cria uma interface Streamlit para colar e filtrar códigos "SB".
    """
    st.set_page_config(page_title="Filtro de Códigos SB", layout="centered")

    st.title("🗂️ Filtro de Códigos SB")
    st.write("Cole seus códigos na caixa de texto abaixo (um por linha) e clique em 'Filtrar Códigos SB'.")

    # Área de texto para entrada de dados
    # st.session_state é usado para manter o texto da caixa de entrada após o re-execução do script
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""

    input_text = st.text_area(
        "Cole seus códigos aqui:",
        value=st.session_state.input_text,
        height=250,
        help="Cada código deve estar em uma linha separada."
    )

    # Botão para acionar o filtro
    if st.button("Filtrar Códigos SB"):
        st.session_state.input_text = input_text # Salva o texto na sessão

        if not input_text.strip():
            st.warning("Por favor, cole alguns códigos antes de filtrar.")
            st.stop() # Interrompe a execução para exibir o aviso

        # Processamento dos dados (lógica Python pura)
        # Divide o texto em linhas e remove linhas vazias/espaços
        input_data = [line.strip() for line in input_text.splitlines() if line.strip()]

        if not input_data:
            st.warning("Nenhum código válido encontrado após a limpeza. Verifique se há conteúdo real.")
            st.stop()

        codigos_filtrados = []
        for codigo in input_data:
            codigo_limpo = str(codigo).strip()
            if codigo_limpo.upper().startswith('SB'):
                codigos_filtrados.append(codigo_limpo)

        # Exibir os resultados
        if not codigos_filtrados:
            st.info("Nenhum código iniciado com 'SB' foi encontrado na sua lista.")
        else:
            st.success(f"**{len(codigos_filtrados)}** códigos 'SB' encontrados:")
            
            # Exibe os códigos como texto puro para fácil cópia
            st.text_area("Códigos 'SB' Filtrados:", value="\n".join(codigos_filtrados), height=200, key="output_area")
            
            # Opção para copiar para a área de transferência (requer um navegador moderno)
            st.markdown(
                """
                <script>
                function copyToClipboard(elementId) {
                    var copyText = document.getElementById(elementId).querySelector('textarea');
                    copyText.select();
                    document.execCommand("copy");
                }
                </script>
                """,
                unsafe_allow_html=True
            )
            st.button("Copiar Códigos Filtrados", on_click=lambda: st.runtime.legacy_caching.clear_cache() or st.experimental_rerun() if st.query_params.get("copy") != "true" else None, help="Copia o conteúdo da caixa de texto de resultados para a área de transferência.")
            if st.query_params.get("copy") == "true":
                st.write("Copiado para a área de transferência!")

# Ponto de entrada do aplicativo Streamlit
if __name__ == "__main__":
    filtrar_codigos_sb_streamlit()