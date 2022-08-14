import os
import pandas as pd
import smtplib
import time
import schedule
import datetime

USERNAME=os.environ.get('G_USER')
PASS=os.environ.get('G_PASS')
df=pd.read_csv('Calem.csv')
size=df.shape[0]


def send_mail():

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(USERNAME, PASS)
  subject = 'Aulas de Hoje'

  #PegarData
  getData = datetime.datetime.now()

  #essa foi a linha de codigo mais idiota que eu ja tive que fazer
  if (getData.month < 10):
    mes = ('0'+str(getData.month))
  else:
    mes = (str(getData.month))
  diaHoje = (str(getData.day)+'/'+mes+'/'+str(getData.year))
  #Puta que pariu

  #loop para achar o dia certo e para criar a mensagem a ser enviada para o email
  x = 0
  msg = ''
  i = 0
  for i in range(size):
    if (df.iloc[x, 0] != diaHoje):
      x = x+1
      if (x >= size):
        break
    else:
      while (df.iloc[x, 0] == diaHoje):
        msg = (msg+'\n\n'+(df.iloc[x, 2]) + '  ---->  ' + (df.iloc[x, 4]))
        x = x+1


  if (msg==''):
    return
  msgCompleta = f'subject:{subject}\n\n{msg}'
  server.sendmail(USERNAME,USERNAME, msgCompleta.encode('utf-8'))

schedule.every().day.at('01:00').do(send_mail)
#schedule.every(10).seconds.do(send_mail)
while True:
  schedule.run_pending()
  time.sleep(1)
