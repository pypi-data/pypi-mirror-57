import csv

'''
Merge two csv:
Notes: we assume only the source_csv1 has the header, not the one on the right
'''

class MergeCSV:

    def __init__ (self,source_csv1,source_csv2,output_file,column_header):
        if(source_csv1):
            self.source_csv1 = source_csv1
        else:
            self.source_csv1 = input("first source file: ")
        if(source_csv2):
            self.source_csv2 = source_csv2
        else:
            self.source_csv2 = input("second source file: ")
        self.output_file = output_file
        if (column_header):
            self.column_header = column_header
        else:
            self.column_header= input('header :')
        self.header = ""
        self.row_list = []

    
    def merge_csv(self):
        with open(self.source_csv1,'r',encoding='utf-8-sig') as source_file_1,  open(self.source_csv2,'r',encoding='utf-8-sig') as source_file_2:
            soruce_reader1_iter = iter( csv.reader(source_file_1))
            source_reader2_iter = iter(csv.reader(source_file_2))
            local_max = 0

            reader1_header = next(soruce_reader1_iter)
            header_len = len(reader1_header)
            i = 0 
            while(True):
                try:
                    second_iter_list = next(source_reader2_iter)
                    first_iter_list = next(soruce_reader1_iter)
                    first_len = len(first_iter_list)
                    self.row_list.append(first_iter_list +  list(' ' * (header_len-first_len) ) +second_iter_list)
                    # self.row_list.append( first_iter_list +  [ ] * (header_len-first_len) + second_iter_list)
                    if(len(second_iter_list)> local_max):
                        local_max = len(second_iter_list)
                except StopIteration as identifier:
                    break
            # print (local_max)
            header = reader1_header+ ([self.column_header]* local_max)
        
        with open(self.output_file,'w',encoding='utf-8-sig') as output_file:
            output_writer  = csv.writer(output_file)
            output_writer.writerow(header)
            for row in self.row_list:
                # row = row + [ ]  * (header_len+local_max-len(row))
                row = row + list( ' ' * (header_len+local_max-len(row)))
                print (len(row))
                output_writer.writerow(row)