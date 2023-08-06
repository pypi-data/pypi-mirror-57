import csv
from bs4 import BeautifulSoup


class gs1_ParseHTML:

    def __init__(self, csv_file_with_ticket_id, ticket_id_col, attachment_col,content_col,content_file):
        self.csv_file_with_ticket_id = csv_file_with_ticket_id
        self.ticket_id_col = ticket_id_col
        self.attachment_col = attachment_col
        self.content_col = content_col
        if(content_file):
            self.content_file = content_file
        else:
            self.content_file = csv_file_with_ticket_id

        ticket_filepath_dict = []
        with open(csv_file_with_ticket_id) as ticket_id_file:
            ticket_id_reader = csv.reader(ticket_id_file)
            next(ticket_id_reader)
            ticket_filepath_dict = {
                ticket_id_row[ticket_id_col]: [] for ticket_id_row in ticket_id_reader}
        self.ticket_filepath_dict = ticket_filepath_dict
        ticket_id_file.close()

    def get_conversation_id_from_url(self,inlineimage_url):
        inlineimage_url = inlineimage_url.replace(
            'https://servicedesk.gs1au.org/', "/")
        if('inlineimages' in inlineimage_url):
            inlineimage_url_split = inlineimage_url.split('/')
            if(inlineimage_url_split[-4] == 'Conversation'):
                filename = 'conv_' + \
                    inlineimage_url_split[-2] + '_' + inlineimage_url_split[-1]
                file_path = '/'.join(inlineimage_url_split[:-1]) + '/' + filename
            elif (inlineimage_url_split[-3] == 'WorkOrder'):
                filename = 'wo_' + \
                    inlineimage_url_split[-2] + '_' + inlineimage_url_split[-1]
                file_path = '/'.join(inlineimage_url_split[:-1]) + '/' + filename
            else:
                print("ERROR: unparseable image: " + inlineimage_url)
            return (file_path)



    def get_file_path(self,file_attchemnt):
        if(self.content_file!=self.csv_file_with_ticket_id):
        # print  ('file://'+file_attchemnt[3:].replace("\\","/").replace(' ','%20').replace('fileAttachments','fileAttachments_Conversation'))
            return ('file://'+file_attchemnt[3:].replace("\\","/").replace(' ','%20').replace('fileAttachments','fileAttachments_Conversation'))
    
    def parse_content(self, content, issue_id, file_attachment):
        '''
        Put both individual attachment and enbaded attachment into this the dict 
        '''
        soup = BeautifulSoup(content, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            image_url = image['src']
            file_path = self.get_conversation_id_from_url("file:/"+image_url)
            if(file_path ):
                try:
                    self.ticket_filepath_dict[issue_id].append(file_path)
                except KeyError:
                    pass
        if(file_attachment !='NULL'):
            try:
                self.ticket_filepath_dict[issue_id].append(self.get_file_path(file_attachment))
            except KeyError:
                pass
        try:
           self.ticket_filepath_dict[issue_id] =  list(dict.fromkeys(self.ticket_filepath_dict[issue_id]))
        except KeyError:
            pass
    
    def iter_csv(self):
        with open (self.content_file,'r',encoding='utf-8-sig') as csv_file:
            csv_reader =  csv.reader(csv_file)
            for row in csv_reader:
                issue_id = row[self.ticket_id_col]
                file_attachment = row[self.attachment_col]
                self.parse_content(row[self.content_col],issue_id,file_attachment)

    def get_local_max(self):
        local_max = 0
        for key in self.ticket_filepath_dict.keys():
            if (len(self.ticket_filepath_dict[key])>local_max):
                local_max = len(self.ticket_filepath_dict[key])
        return local_max
    
    def get_file_attachment_dict(self):
        return self.ticket_filepath_dict