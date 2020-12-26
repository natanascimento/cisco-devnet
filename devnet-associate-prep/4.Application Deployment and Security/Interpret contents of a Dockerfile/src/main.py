import streamlit as st

def main():
    st.title("Teste DevNet")
    st.subheader("Testando Deploy com Docker")
    main_options = st.selectbox(
             'Teste',
            ('Docker 1', 'Docker 2'))
    if main_options == 'Docker 1':
        st.set_option('deprecation.showfileUploaderEncoding', False)
        #Analisando dados dos chamados abertos
        file = st.file_uploader('Escolha a base de dados (.xls)', encoding=None, type='xls')

    if main_options == 'Docker 2':
        st.set_option('deprecation.showfileUploaderEncoding', False)
        #Analisando dados dos chamados abertos
        file = st.file_uploader('Escolha a base de dados (.xls)', encoding=None, type='xls')

if __name__ == "__main__":
    main()