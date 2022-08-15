# UTPlanner
 Planejador de aulas UTFPR

O programa ira enviar a matéria das aulas que você no dia e o conteudo desta aula ( de acordo com o planejamento) para que seja facil a revisão pré-aula.



Substituir as informações de Calem.csv (NÃO MUDAR AS INFORMAÇOES DAS COLUNAS, A QUANTIDADE DE LINHAS PODE SER AUMENTADA/DIMINUIDA CONFORME NECESSIDADE) por outro csv com as informaçoes de aula atualizadas, é facil adicionar informaçoes mandadas , é necessario 2 variaveis de sistemas:
USERNAME-> com o seu Email (gmail)
e PASS -> com uma senha de app que o google precisa faz para você

è necessario utilizar o task scheduler do windows para poder automatizar o sistema.

é necessario criar um arquivo com o pyinstaller juntando o csv com o .py em um unico com:
pyinstaller --onefile --add-data "nomedoarquivo.csv/nomedoaquivo" Main.py

o arquivo gerado é o arquivo que vai ser utilizado no task scheduler para o agendamento do sistema 
