import pandas as pd
import smtplib


# Read the Excel with all the data
old_books = pd.read_excel("libro_autor.xlsx")
t_books = old_books.to_records(index=False)
tuplas_books = list(t_books)
tuplas_b = []
print("Tamaño tuplas_books",len(tuplas_books), "\n")
count = 0
for l_a in tuplas_books:
    libro = l_a[0]
    autores = str(l_a[1])
    # print(l_a[1])
    if "/" in autores:
        autores_temp = autores.split("/")
        for i in autores_temp:
            tuplas_b.append((libro, i))
    else:
        tuplas_b.append((libro, autores))



# brent_prices = pd.read_excel("brent_xls.xls")
# records = brent_prices.to_records(index=False)
# tuplas_brent = list(records)
# print("Tamaño tuplas_brent",len(tuplas_brent), "\n")

# fechas_brent = []
# for tp in tuplas_brent:
#     fechas_brent.append(tp[0])

# tuplas_copy_cop = tuplas_cop

# for tp in tuplas_copy_cop:
#     if tp[0] not in fechas_brent:
#         tuplas_cop.remove(tp)


# print("Tamaño cop nuevo" ,len(tuplas_cop))

df2 = pd.DataFrame(tuplas_b)
df2.to_csv("tablas/output.csv")

### Create an HTML version of your message:
# 1. in the message itself write {0} where you want the tabbycat link
# 2. In order to convert your email to HTML format, use this website:
#       https://www.textfixer.com/html/convert-text-html.php
#       make sure to choose "Use paragraph and line break tags"

# # Loop through the emails
# for idx, row in email_list.iterrows():
#     #reset the msg before every send
#     message["Subject"] = subject
#     message["From"] = your_email
#
#     # Get each records name, email, subject and message
#     name = row['Name']
#     email = row['Email']
#     url = row['URL']
