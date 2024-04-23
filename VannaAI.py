import vanna
from vanna.remote import VannaDefault

api_key='65972c34807d425b9ede327daabfc981'
vanna_model_name='stwai'
vn = VannaDefault(model=vanna_model_name, api_key=api_key)
vn.connect_to_mssql(odbc_conn_str='DRIVER={ODBC Driver 17 for SQL Server};SERVER=STWDOTNETSERVER\\DEV19;DATABASE=ADAM;UID=stw;PWD=StW@2021*!$') # You can use the ODBC connection string here
from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run()