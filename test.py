import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo):
    print("Inserting BLOB into python_etest table")
    try:
        connection = mysql.connector.connect(host='mysqltestfandj.mysql.database.azure.com',
                                             database='PokeFandJ',
                                             user='saFandJ',
                                             password='Step2024')

        cursor = connection.cursor()
        sql_insert_blob_query = """ insert into test (Id, Name, Photo) values (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#insertBLOB(1, "Bulbasaur", "C:/Users/potro/OneDrive/Documentos/Documentacion Oficial/200px-Bulbasaur.png")
insertBLOB(906, "Sprigatito", "C:/Users/potro/OneDrive/Documentos/GitHub/PokedexF&J/PokeFandJ/images/200px-Sprigatito_Masters.png")