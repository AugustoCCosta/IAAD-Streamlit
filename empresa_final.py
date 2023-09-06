import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MypizzaAugus261402*',
    database='Empresa_adaptado',
)

mycursor = mydb.cursor()
print('Conectado')


def main():
    st.title('Banco de Dados: Empresa Adaptado')
    opcao = st.sidebar.selectbox(label='Selecione a operação que deseja realizar', options=(
        'Create (Criar)', 'Read (Ler)', 'Update (Atualizar)', 'Delete (Deletar)'))

    if opcao == 'Create (Criar)':
        st.subheader('Escolha onde devo criar')
        tabela = st.selectbox(label=' ', options=(
            'Funcionario', 'Departamento','Dependente'))
        if tabela == 'Funcionario':
            st.subheader('Criando Funcionário')
            Pnome = st.text_input('Primeiro nome do funcionário:')
            Minicial = st.text_input('Inicial do nome do meio:')
            Unome = st.text_input('Último sobrenome:')
            Cpf = st.text_input('CPF:')
            Datanasc = st.text_input('Data de nascimento (ANO-MÊS-DIA):')
            Endereco = st.text_input('Endereço:')
            Sexo = st.selectbox("Sexo", ["M", "F"])
            Salario = st.number_input("Salário", min_value=0)
            Cpf_supervisor = st.text_input(
                'CPF do seu supervisor (Sem pontos e traços):')
            Dnr = st.number_input("Número do Departamento", min_value=1)
            if st.button('Criar'):
                sql = 'insert into funcionario(Pnome, Minicial, Unome, Cpf, Datanasc, Endereco, Sexo, Salario, Cpf_supervisor, Dnr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                values = (Pnome, Minicial, Unome, Cpf, Datanasc, Endereco, Sexo, Salario, Cpf_supervisor, Dnr)
                mycursor.execute(sql, values)
                mydb.commit()
                st.success('Criado com sucesso!')

        elif tabela == 'Departamento':
            st.subheader('Criando Departamento')
            dnome = st.text_input('Nome do departamento:')
            dnumero = st.number_input('Número do departamento:', min_value=1)
            cpf_gerente = st.text_input('CPF do gerente:')
            data_inicio_gerente = st.text_input(
                'Data que começou na gerencia (ANO-MÊS-DIA):')
            if st.button('Criar'):
                sql = 'insert into departamento(dnome, dnumero, cpf_gerente, data_inicio_gerente) values(%s, %s, %s, %s)'
                values = (dnome, dnumero, cpf_gerente, data_inicio_gerente)
                mycursor.execute(sql, values)
                mydb.commit()
                st.success('Criado com sucesso!')

        elif tabela == 'Dependente':
            st.subheader('Criando Dependente')
            fcpf = st.text_input('CPF do parente:')
            nome_dependente = st.text_input('Nome do dependente:')
            sexo = st.selectbox('Sexo do Dependente (F/M):', ["M", "F"])
            datanasc = st.text_input(
                'Data de nascimento do dependente (ANO-MÊS-DIA):')
            parentesco = st.text_input('Grau de parentesco:')
            if st.button('Criar'):
                sql = 'insert into dependente(fcpf, nome_dependente, sexo, datanasc, parentesco) values(%s, %s, %s, %s, %s)'
                values = (fcpf, nome_dependente, sexo, datanasc, parentesco)
                mycursor.execute(sql, values)
                mydb.commit()
                st.success('Criado com sucesso!')

    elif opcao == 'Read (Ler)':
        st.subheader('Escolha o que quer visualizar')
        para_ler = st.selectbox(label=' ', options=(
            'Funcionario', 'Departamento','Dependente'))
        mycursor.execute(f'select * from {para_ler}')
        resultado = mycursor.fetchall()
        st.table(resultado)

    elif opcao == 'Update (Atualizar)':
        st.subheader('Escolha de onde quer atualizar')
        para_atualizar = st.selectbox(label=' ', options=(
            'Funcionario', 'Departamento', 'Dependente'))
        if para_atualizar == 'Funcionario':
            st.subheader('Atualizando a tabela Funcionario')
            at_coluna = st.text_input('Diga qual coluna devo atualizar:')
            valor_coluna = st.text_input('Diga qual novo valor:')
            at_linha = st.text_input('Diga qual a condição:')
            valor_linha = st.text_input('Diga qual linha devo atualizar:')
            if st.button('Atualizar'):
                if valor_coluna.isnumeric() and at_coluna == 'Salario':
                    valor_coluna = int(valor_coluna)
                    if valor_coluna > 55000:
                        st.error('O salário não pode ser maior que R$ 55000')
                else:
                    if at_linha == '' or valor_linha == '':
                        sql = f'update funcionario set {at_coluna} = {valor_coluna}'
                        mycursor.execute(sql)
                        mydb.commit()
                        st.success('Dado atualizado com sucesso!')
                    else:
                        sql = f'update funcionario set {at_coluna} = {valor_coluna} where {at_linha} = {valor_linha}'
                        mycursor.execute(sql)
                        mydb.commit()
                        st.success('Dado atualizado com sucesso!')

        elif para_atualizar == 'Departamento':
            st.subheader('Atualizando a tabela Departamento')
            at_coluna = st.text_input('Diga qual coluna devo atualizar:')
            valor_coluna = st.text_input('Diga qual novo valor:')
            at_linha = st.text_input('Diga qual a condição:')
            valor_linha = st.text_input('Diga qual linha devo atualizar:')
            if st.button('Atualizar'):
                if at_linha or valor_linha is None:
                    sql = f'update departamento set {at_coluna} = {valor_coluna}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Dado atualizado com sucesso!')
                else:
                    sql = f'update departamento set {at_coluna} = {valor_coluna} where {at_linha} = {valor_linha}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Dado atualizado com sucesso!')

        elif para_atualizar == 'Dependente':
            st.subheader('Atualizando a tabela Dependente')
            at_coluna = st.text_input('Diga qual coluna devo atualizar:')
            valor_coluna = st.text_input('Diga qual novo valor:')
            at_linha = st.text_input('Diga qual a condição:')
            valor_linha = st.text_input('Diga qual linha devo atualizar:')
            if st.button('Atualizar'):
                if at_linha or valor_linha is None:
                    sql = f'update dependente set {at_coluna} = {valor_coluna}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Dado atualizado com sucesso!')
                else:
                    sql = f'update dependente set {at_coluna} = {valor_coluna} where {at_linha} = {valor_linha}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Dado atualizado com sucesso!')

    elif opcao == 'Delete (Deletar)':
        st.subheader('Escolha de onde quer deletar')
        para_deletar = st.selectbox(label=' ', options=(
            'Funcionario', 'Departamento', 'Dependente'))
        if para_deletar == 'Funcionario':
            st.subheader('Deletando da tabela')
            del_linha = st.text_input('Diga qual coluna devo deletar:')
            valor_del_linha = st.text_input(
                'Diga o valor da linha que será deletada (deixe vazio para deletar tudo da tabela):')
            if st.button('Deletar'):
                if del_linha == '' or valor_del_linha == '':
                    sql = 'delete from funcionario'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')
                else:
                    sql = f'delete from funcionario where {del_linha} = {valor_del_linha}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')

        elif para_deletar == 'Departamento':
            st.subheader('Deletando da tabela')
            del_linha = st.text_input('Diga qual coluna devo deletar:')
            valor_del_linha = st.text_input(
                'Diga o valor da linha que será deletada (deixe vazio para deletar tudo da tabela):')
            if st.button('Deletar'):
                if del_linha == '' or valor_del_linha == '':
                    sql = 'delete from departamento'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')
                else:
                    sql = f'delete from departamento where {del_linha} = {valor_del_linha}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')

        elif para_deletar == 'Dependente':
            st.subheader('Deletando da tabela')
            del_linha = st.text_input('Diga qual coluna devo deletar:')
            valor_del_linha = st.text_input(
                'Diga o valor da linha que será deletada (deixe vazio para deletar tudo da tabela):')
            if st.button('Deletar'):
                if del_linha == '' or valor_del_linha == '':
                    sql = 'delete from dependente'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')
                else:
                    sql = f'delete from dependente where {del_linha} = {valor_del_linha}'
                    mycursor.execute(sql)
                    mydb.commit()
                    st.success('Deletado com sucesso!')

if __name__ == '__main__':
    main()
