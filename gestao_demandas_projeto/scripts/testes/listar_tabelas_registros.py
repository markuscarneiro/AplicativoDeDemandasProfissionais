import sqlite3

# Caminho para o banco de dados SQLite
DB_PATH = '../db.sqlite3'

def listar_tabelas_e_registros():
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Listar todas as tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()

        print("\n📋 Tabelas no banco de dados:")
        for tabela in tabelas:
            print(f"- {tabela[0]}")

        # Listar registros de cada tabela
        print("\n📊 Registros por tabela:")
        for tabela in tabelas:
            print(f"\nTabela: {tabela[0]}")
            cursor.execute(f"SELECT * FROM {tabela[0]};")
            registros = cursor.fetchall()

            if registros:
                for registro in registros:
                    print(registro)
            else:
                print("(Nenhum registro encontrado)")

        # Fechar conexão
        conn.close()

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

if __name__ == "__main__":
    listar_tabelas_e_registros()