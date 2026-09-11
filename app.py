import streamlit as st
import database as db

db.criar_tabela()

st.title("PAINEL DE GESTÃO DE LIVROS", text_alignment="center")

st.markdown("### --- Cadastro dos Livros ---", text_alignment="center")
with st.form("cadastro_livro"):
    titulo = st.text_input("Preencha com o título do livro")
    autor = st.text_input("Preencha com o nome do autor")
    ano_publicacao= st.number_input("Preencha com o ano de publicação", step=1, max_value= 2100, min_value=0)
   
    btn_form= st.form_submit_button("Enviar")

if btn_form:
      msg = db.cadastro_livro(titulo, autor, ano_publicacao,status="Não lido")

      if "Erro" in msg:
            st.error(msg)
      else:
            st.success(msg)

st.markdown("#### --- Lista de Livros Cadastrados ---" , text_alignment="center")

listaLivros = db.getLivros()

if listaLivros == None:
        st.warning("Não há livros cadastrados!")
else:
        dataLivros = [{"id" : livro[0], "titulo":livro [1] , "autor": livro[2], 
                        "ano": livro[3], "status": livro[4]} for livro in listaLivros]

        st.dataframe(dataLivros, width="stretch")

st.markdown("--- Alteração de cadastro de livros ---", text_alignment="center")
with st.form("form_update_livros"):
        id = st.number_input("Coloque o id do livro", value=0, step=1, min_value=0)          
        status = st.text_input("Coloque o novo status do livro")

        btn_update_livros = st.form_submit_button("Alterar")

if btn_update_livros:
        msg = db.update_livro_status(id, status) 

        if msg == 1 or "sucesso" in str(msg).lower():
                st.success("Livro alterado com sucesso!") 
        else:
                st.error(msg)

st.markdown("#### --- Exclusão de Livro ---", text_alignment="center")
with st.form("deletar_livro"):
    id = st.number_input("id", value=0, step=1, min_value=0)

    btn_delete_livro = st.form_submit_button("Deletar", 
    help= "Ao clicar aqui você deleta um livro")

if btn_delete_livro:
        msg = db.deletar_livro(id)
        if "Erro" in msg:
            st.error(msg)
        else:
            st.success(msg)
