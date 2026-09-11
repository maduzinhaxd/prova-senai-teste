import unittest
import sqlite3
import os
import database as db


class TestCadastroLivro(unittest.TestCase):
    def setUp(self):

        self.banco_teste = "banco_teste.db"
        db.criar_tabela(nome_banco = self.banco_teste)

    def tearDown(self):
        if os.path.exists(self.banco_teste):
            os.remove(self.banco_teste)

    def test_cadastro_livro_com_sucesso(self):
            db.cadastro_livro("e assim que acaba", "collen hover", 0,"Lido", self.banco_teste)

            conn = sqlite3.connect(self.banco_teste)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livros WHERE titulo= 'e assim que acaba'")
            livro_salvo = cursor.fetchone()
            conn.close()

            self.assertIsNotNone(livro_salvo,"O Livro deveria ter sido cadastrado")
            self.assertEqual(livro_salvo[1], "e assim que acaba")
            self.assertEqual(livro_salvo[2], "collen hover")
            self.assertEqual(livro_salvo[3], 0)
            self.assertEqual(livro_salvo[4], "Lido")

class TestDeletarLivro(unittest.TestCase):
      def setUp(self):
     
             self.banco_teste = "banco_teste.db"
             db.criar_tabela(nome_banco = self.banco_teste)
     
      def tearDown(self):
             if os.path.exists(self.banco_teste):
                 os.remove(self.banco_teste)

      def test_deletar_livro_com_sucesso(self):
        db.cadastro_livro("e assim que acaba" , "collen hover" , 0,"Lido", self.banco_teste)

        conn = sqlite3.connect(self.banco_teste)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM livros WHERE titulo = 'e assim que acaba'")
        livro_salvo = cursor.fetchone()

        db.deletar_livro(livro_salvo[0] , self.banco_teste)
        
        cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_salvo[0],))
        livro_deletado = cursor.fetchone()
        conn.close()

        self.assertIsNone(livro_deletado, "O livro deveria ter sido deletado do banco de dados")

if __name__ == "__main__":
    unittest.main()
