import pandas as pd
import openpyxl
import twilio
import os
from twilio.rest import Client

account_sid = "Your User ID"
auth_token = "Your Account Token"
client = Client(account_sid, auth_token)


listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
for mes in listaMeses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')
    if (tabelaVendas['Vendas'] > 50000).any():
        vendedor = tabelaVendas.loc[tabelaVendas['Vendas'] > 50000, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] > 50000, 'Vendas'].values[0]
        print(f'No mes {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}  \n')
        message = client.messages.create(
            body=f"No mes {mes} alguém bateu a meta.\nVendedor: {vendedor} \nVendas: {vendas}  \n",
            from_="+15746525935",
            to="Your Number"
        )
    else:
        print(f'No mes {mes} não encontramos \n')





