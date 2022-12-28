from html.parser import HTMLParser


# Custom html parser which will Covert HTML to LIST
class html_to_list_parser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    # These variables will tell the parser what data it's reading at the moment
    self.pd_table = False
    self.ru_table = False
    self.bu_table = False
    self.tr = False
    self.td = False
    self.date = ''
    self.subList = []

    self.index = 0
    self.product_detail = []
    self.recent_usage = []
    self.battery_usage = []
  
  # Called everytime the parser encounters a new tag
  # e.g. <html> or <p>
  def handle_starttag(self, tag, attrs):
    if tag == 'table':
      self.index += 1
      if self.index == 1:
        self.pd_table = True
      elif self.index == 3:
        self.ru_table = True
      elif self.index == 4:
        self.bu_table = True
    elif tag == 'tr':
      self.tr = True
    elif tag == 'td':
      self.td = True

  # Called when the parser encounters the contents of a tag
  # e.g. 'Some word' in '<p>Some word</p>
  def handle_data(self, data):
    if self.pd_table or self.ru_table or self.bu_table:
      if self.tr:
        if self.td:
          data = data.strip('\n')
          data = data.lower().strip()
          if data:
            self.subList.append(data)
          

  # Similar to above
  def handle_endtag(self, tag):
    if tag == 'table':
      self.pd_table = False
      self.ru_table = False
      self.bu_table = False
    elif tag == 'tr':
      self.tr  = False
      if self.pd_table:
        self.product_detail.append(self.subList)
        self.subList = []
      elif self.ru_table:
        self.subList.append(self.product_detail[0][1])
        if self.subList[1] == "suspended":
          self.subList.insert(2,"-")
        elif self.subList[2] == "suspended":
          self.subList.insert(3,"-")
        if '2022' in self.subList[0]:
          self.date = self.subList[0]
        else:
          self.subList.insert(0,self.date)
        self.recent_usage.append(self.subList)
        self.subList = []
      elif self.bu_table:
        if self.subList:
          self.subList.append(self.product_detail[0][1])
          if '2022' in self.subList[0]:
            self.date = self.subList[0]
          else:
            self.subList.insert(0,self.date)
          self.battery_usage.append(self.subList)
          self.subList = []
    elif tag == 'td':
      self.td  = False

  # Return List
  def get_ru(self):
    self.recent_usage.pop(0)
    return self.recent_usage

  # Return List
  def get_bu(self):
    self.battery_usage.pop(0)
    return self.battery_usage



# Run the parser!
parsers = []
for i in range(7):
  parser = html_to_list_parser()
  html_file = open(rf"scripts\battery-reports\{i}.html", "r").read()
  parser.feed(html_file)
  parser.close()
  parsers.append(parser)

# for parser in parsers:
#   print(parser.get_ru())
#   print("\n\n")

# output = [
#   ['2022-07-05', '11:04:39', 'active', '0:02:46', '1 %', '468 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:07:25', 'connected standby', '0:04:30', '-', '91 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:11:56', 'active', '0:26:56', '32 %', '10,249 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:38:52', 'connected standby', '0:00:04', '-', '34 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:44:04', 'connected standby', '0:00:00', '-', '-', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '13:48:27', 'active', '0:02:34', '1 %', '262 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '13:51:02', 'connected standby', '0:05:29', '-', '69 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '13:56:31', 'active', '0:40:46', '18 %', '5,916 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '14:37:18', 'connected standby', '0:01:37', '-', '57 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '14:38:55', 'active', '0:48:00', '27 %', '8,710 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '15:29:11', 'active', '0:33:20', '14 %', '4,629 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '16:23:09', 'active', '0:07:59', '3 %', '1,094 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '18:20:20', 'connected standby', '16:08:39', '15 %', '4,833 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '10:30:29', 'connected standby', '0:00:35', '1 %', '239 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '10:31:05', 'active', '0:26:15', '12 %', '3,899 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '10:57:20', 'connected standby', '0:04:02', '-', '46 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:01:23', 'active', '0:33:36', '13 %', '4,320 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:35:00', 'connected standby', '0:06:17', '-', '80 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '11:41:18', 'active', '0:35:48', '13 %', '4,298 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '12:17:06', 'connected standby', '0:17:55', '-', '148 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '12:35:01', 'active', '0:43:18', '34 %', '10,978 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '14:11:04', 'active', '0:00:12', '-', '23 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '16:25:37', 'active', '0:23:57', '18 %', '5,734 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-05', '16:49:34', 'connected standby', '4:40:32', '5 %', '1,527 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '10:05:05', 'active', '0:59:00', '25 %', '7,969 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '11:04:06', 'connected standby', '0:03:00', '-', '68 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '11:07:07', 'active', '1:11:26', '26 %', '8,493 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '12:18:33', 'connected standby', '0:00:30', '-', '46 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '12:19:04', 'active', '0:00:25', '-', '103 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '12:19:29', 'connected standby', '0:35:08', '1 %', '262 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '12:54:37', 'active', '0:03:02', '5 %', '1,676 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '13:45:23', 'active', '0:04:01', '2 %', '639 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '15:50:14', 'active', '0:47:20', '18 %', '5,882 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '16:37:35', 'connected standby', '0:00:02', '-', '-', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '16:37:38', 'active', '0:06:14', '2 %', '730 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '16:43:52', 'connected standby', '0:03:34', '-', '68 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '16:47:26', 'active', '0:01:34', '1 %', '217 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-07', '16:49:01', 'connected standby', '17:49:49', '18 %', '5,711 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-08', '10:38:51', 'active', '0:05:15', '3 %', '981 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-08', '10:44:07', 'connected standby', '0:01:41', '-', '57 mwh', 'xe-ggn-it-02893'], 
#   ['2022-07-08', '10:45:48', 'active', '0:11:48', '6 %', '2,006 mwh', 'xe-ggn-it-02893']
# ]
