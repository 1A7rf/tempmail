import requests,json 
import objects
class tempMail:
  def __init__(self):
    self.email = None
    self.token = None
    self.headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'application-name': 'web',
    'application-version': '2.2.13',
    'content-length': '43',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://temp-mail.io',
    'referer': 'https://temp-mail.io/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    }
  
  def login(self,email : str = None,token : str = None):
    self.email=email
    self.token = token
  
  def getNewMail(self,max_length : int = 10,min_length : int = 10,name : str = None,domain : str = None):
    data=json.dumps({
      'domain': domain,
      'name': name,
      'max_name_length': max_length,
      'min_name_length': min_length
    })
    req=requests.post("https://api.internal.temp-mail.io/api/v3/email/new",headers=self.headers,data=data)
    if req.status_code != 200 : raise TypeError(req.text)
    r=json.loads(req.text)
    self.email = r['email']
    self.token=r['token']
    return objects.NewEmail().Email(r)

  def getMessages(self):
    req=requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{self.email}/messages')
    if req.status_code != 200: raise TypeError(req.text)
    return objects.messages().messages(json.loads(req.text))

  def readMessage(self,messageId : str = None):
    req=requests.get(f'https://api.internal.temp-mail.io/api/v3/message/2ee46adb-a405-487f-b881-63c94a650859')
    if req.status_code != 200: raise TypeError(req.text)
    return objects.readMessage().message(json.loads(req.text))