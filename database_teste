import sqlite3

def conectar(nome_banco= "booktrack.db"):
    conn = sqlite3.connect(nome_banco)
    return conn

def criar_tabela(nome_banco= "booktrack.db"):
    conn = conectar(nome_banco)
    cursor= conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    status TEXT NOT NULL
    )
""")
    conn.commit()
    conn.close()

def cadastro_livro(titulo:str, autor:str, ano_publicacao, status:str="Não lido", nome_banco= "booktrack.db"):
    if ano_publicacao > 2026:
        return "O ano é inválido."
    else:
        conn = conectar(nome_banco)
        cursor= conn.cursor()

        cursor.execute("INSERT INTO livros(titulo, autor, ano_publicacao, status) VALUES (?, ?, ?, ?)",(titulo, autor, ano_publicacao,status))

        conn.commit()
        conn.close()

    return "Livro cadastrado com sucesso!"


def getLivros(nome_banco = "booktrack.db"):
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    dados_livros = cursor.fetchall()

    conn.close()
    return dados_livros

def update_livro_status(id: int,novo_status, nome_banco = "booktrack.db"): 
    status_permitidos = ["Não lido","Lendo", "Lido"]
    if novo_status not in status_permitidos:
        return f"Erro: status '{novo_status}' não é permitido!"
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET status = ? WHERE id  = ?" , (novo_status,id))
    rows_affected = cursor.rowcount 
    if rows_affected > 0:
        conn.commit()
        conn.close()

        return "Status atualizado com sucesso!"
    else:
        return f"Erro: livro com ID = {id}, não encontrado"

def deletar_livro(id , nome_banco = "booktrack.db"):
    if id > 0:
            
        conn = conectar(nome_banco)
        cursor = conn.cursor()

        cursor.execute("SELECT status FROM livros WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    
    if not resultado:
        conn.close()
        return f"Erro: Livro com ID = {id} não encontrado."
        
    status_atual = str(resultado[0])
    
    if status_atual.strip().lower() == "lendo":
        conn.close()
        return "Erro: Não é possível excluir um livro com status 'Lendo'!"
    
    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
    linhas_afetadas = cursor.rowcount
    
    conn.commit()
    conn.close()

    if linhas_afetadas > 0:
        return f"O livro de ID {id} foi deletado com sucesso!"
    else:
        return "Erro ao tentar deletar o livro."
