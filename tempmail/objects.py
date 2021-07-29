class NewEmail:
  def Email(self, data):
    self.json = data
    self.email=data['email']
    self.token=data['token']
    return self

class messages:
  def messages(self,data):
    self.json=data
    self.attachments= []
    self.body_html= []
    self.body_text = []
    self.created_at= []
    self.author= []
    self.id= []
    self.subject= []
    self.to= []

    for e in self.json:
      self.id.append(e['id'])
      self.to.append(e['to'])
      self.subject.append(e['subject'])
      self.body_text.append(e['body_text'])
      self.created_at.append(e['created_at'])
      self.author.append(e['from'])
      self.body_html.append(e['body_html'])
      self.attachments.append(e['attachments'])
    return self

class readMessage:
  def message(self,data):
    self.json = data
    self.attachments= data['attachments']
    self.body_html= data['body_html']
    self.body_text= data['body_text']
    self.cc= data['cc']
    self.created_at= data['created_at']
    self.author= data['from']
    self.id= data['id']
    self.subject= data['subject']
    self.to= data['to']
    return self