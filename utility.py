import streamlit as st
import re
import sqlite3
from sqlite3 import Error
import pandas as pd
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
import streamlit_authenticator as stauth


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def create_dbconnection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    the_conn = None
    try:
        the_conn = sqlite3.connect(db_file, check_same_thread=False)
        return the_conn
    except Error as e:
        print(e)

    return the_conn


def create_table(the_conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param the_conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = the_conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_row(the_conn, kayit):
    sql_for_insert_row = """INSERT INTO staff_table(title,Name,Surname,Category,Orcid_no,BC_degree,MSc_degree,PhD,
    Specialized_on, Case_study, Capacity_need, Levelofexperience)
       VALUES(?,?,?,?,?,?,?,?,?,?,?,?) """
    cur = the_conn.cursor()
    cur.execute(sql_for_insert_row, kayit)
    the_conn.commit()


def delete_row(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' DELETE FROM staff_table
                 WHERE id=?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def update_row(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE staff_table
                 SET title = ?, Name = ?, Surname=?, Category=?, Orcid_no=?, BC_degree=?, MSc_degree=?, PhD=?, Specilized_on=?, Case_study=?, Capacity_need=?, Levelofexperience=?   
                 WHERE id=? '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()



def insert_user(the_conn, kayit):
    """Returns the user on a successful user creation, otherwise raises and error"""
    sql_for_user_ekle = """INSERT INTO users(key,name,password) 
       VALUES(?,?,?) """
    cur = the_conn.cursor()
    cur.execute(sql_for_user_ekle, kayit)
    the_conn.commit()


# veritabanı oluştur ve tabloları olustur
database = r"veriler.db"
the_conn = create_dbconnection(database)
if the_conn is not None:
    sql_for_create_staff_table = """ CREATE TABLE IF NOT EXISTS staff_table(
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        Name text NOT NULL,
                                        Surname text NOT NULL,
                                        Category text NOT NULL,
                                        Orcid_no text NOT NULL,
                                        BC_degree text NOT NULL,
                                        MSc_degree text NOT NULL,
                                        PhD text NOT NULL,
                                        Specialized_on text NOT NULL,
                                        Case_study text NOT NULL,
                                        Capacity_need text NOT NULL,
                                        Levelofexperience text NOT NULL
                                    ); """

    create_users_table_sql = """ CREATE TABLE IF NOT EXISTS users(
                                            id integer PRIMARY KEY,
                                            key text NOT NULL,
                                            name text NOT NULL,
                                            password text NOT NULL
                                        ); """

    create_table(the_conn, sql_for_create_staff_table)
    create_table(the_conn,create_users_table_sql)

    print('Tablolar başarılı')
else:
    print("Hata! veritabani baglantisi kurulamiyor.Tablolar Oluşturulamadı.")


df_staff = pd.read_sql_query("SELECT * from staff_table", the_conn)

# --- USER AUTHENTICATION ---
names = ["Selda Hacaloğlu", "Burcu Uyuşur"]
usernames = ["shacaloglu", "buyusur"]
passwords = ['Shacaloglu123..', 'Buyusur123..']
hashed_passwords = stauth.Hasher(passwords=passwords).generate()

for (name, user, hash_password) in zip(names, usernames, hashed_passwords):
    insert_user(the_conn=the_conn, kayit=(user, name, hash_password))

