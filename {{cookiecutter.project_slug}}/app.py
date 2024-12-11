import streamlit as st 



st.set_page_config(layout="wide")


if "{{ cookiecutter.include_src_directory }}" == 'y':
    from src.components import sidebar
    sidebar.show_sidebar()

st.title('{{ cookiecutter.project_slug }}')
st.write('{{ cookiecutter.project_description }}')