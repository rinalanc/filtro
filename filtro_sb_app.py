import streamlit as st

def filtrar_codigos_sb_simples():
    """
    Cria uma interface Streamlit minimalista para colar e filtrar códigos "SB".
    """
    st.set_page_config(page_title="Filtro de Códigos SB", layout="centered")

    # ----- REMOVIDOS: st.title e st.write de instruções iniciais -----

    # Área de texto para entrada de dados
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""

    input_text = st.text_area(
        "Cole seus códigos aqui:", # Mantido um rótulo mínimo para a caixa de entrada
        value=st.session_state.input_text,
        height=250,
        help="Cada código deve estar em uma linha separada."
    )

    # Botão para acionar o filtro
    if st.button("Filtrar Códigos SB"):
        st.session_state.input_text = input_text # Salva o texto na sessão

        if not input_text.strip():
            # Mantido o aviso de entrada vazia para feedback essencial ao usuário
            st.warning("Nenhum código colado. Cole seus códigos na caixa acima.")
            st.stop() 

        # Processamento dos dados (lógica Python pura)
        input_data = [line.strip() for line in input_text.splitlines() if line.strip()]

        if not input_data:
            st.warning("Nenhum código válido encontrado após a limpeza. Verifique se há conteúdo real.")
            st.stop()

        codigos_filtrados = []
        for codigo in input_data:
            codigo_limpo = str(codigo).strip()
            if codigo_limpo.upper().startswith('SB'):
                codigos_filtrados.append(codigo_limpo)

        # Exibir os resultados de forma minimalista
        st.success(f"**{len(codigos_filtrados)}** códigos 'SB' encontrados:")
        
        # Exibe os códigos como texto puro para fácil cópia, mesmo que a lista esteja vazia
        # Isso garante que a caixa de saída esteja sempre lá, conforme a imagem de referência
        st.text_area("Códigos 'SB' Filtrados:", value="\n".join(codigos_filtrados), height=200, key="output_area")
        
        # Botão Copiar (lógica original)
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
    filtrar_codigos_sb_simples()
