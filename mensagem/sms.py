#Importando o Twilio
from twilio.rest import Client

#Nossa conta
account_sid =  'contaTwilio'

#Nosso Token
auth_token ='tokenTwilio'

client = Client(account_sid, auth_token)

#enviar
client.messages.create(from_="numeroTwilio", body="Mensagem para teste de Twilio", to="+5511970246102") 