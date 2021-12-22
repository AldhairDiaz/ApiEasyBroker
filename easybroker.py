import requests

class ApiEasyBroker:

    def __init__(self, page, limit,api_key):
        self.page = page
        self.limit = limit
        self.api_key=api_key

    def connectApi(self):
        try:
          self.token=self.api_key
          self.website= 'https://api.stagingeb.com/v1/properties?'

          self.headers={
              'X-Authorization':self.token                    
               }
    
          self.params={
            'page':self.page,
            'limit':self.limit

             }

          self.response=requests.get(self.website,params=self.params,headers=self.headers)

          if self.response.status_code == 200:
            self.response=self.response.json()
            self.detail=self.response['pagination']
            print(f"SE HA ENCONTRADO UN LIMITE DE: {self.detail['limit']} TITULOS\
                 EN LA PAGINA: {self.detail['page']}\
                 DE UN TOTAL DE: {self.detail['total']} paginas\n")
                         
            for self.title in self.response['content']:

                print(self.title['title'])
          else:
              self.response=self.response.json()
              print(str(self.response['error']))


        except:
          print('An exception occurred')

api_key='l7u502p8v46ba3ppgvj5y2aad50lb9'
a=ApiEasyBroker(1,20,api_key) 
a.connectApi()