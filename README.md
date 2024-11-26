USAGE
---------------------

GET <http://host/v2/api/{from_city}/{to_city}/{date}>

Data Comes from Enuygun.com

HOW TO RUN
--------------------
cd easybus/ 

uvicorn main:app
--------------------
*ENVIRONMENT*

EASYBUS_HOST = ip address to serve
EASYBUS_PORT = which port to use
