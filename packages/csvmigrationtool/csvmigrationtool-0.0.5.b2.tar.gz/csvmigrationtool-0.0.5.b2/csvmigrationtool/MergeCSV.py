import csv
class MergeCSV:

    def __init__ (self,source_csv1,source_csv2,output_file,column_header):
        self.source_csv1 = source_csv1
        if(source_csv2):
            self.source_csv2 = source_csv2
        else:
            self.source_csv2 = input("second source file: ")
        self.output_file = output_file
        self.column_header = column_header
        self.header = ""
        self.row_list = []

    
    def merge_csv(self):
        with open(self.source_csv1,'r',encoding='utf-8-sig') as source_file_1,  open(self.source_csv2,'r',encoding='utf-8-sig') as source_file_2:
            soruce_reader1_iter = iter( csv.reader(source_file_1))
            source_reader2_iter = iter(csv.reader(source_file_2))
            local_max = 0

            reader1_header = next(soruce_reader1_iter)
            i = 0 
            while(True):
                try:
                    second_iter_list = next(source_reader2_iter)
                    self.row_list.append(next(soruce_reader1_iter)+second_iter_list)
                    if(len(second_iter_list)> local_max):
                        local_max = len(second_iter_list)
                except StopIteration as identifier:
                    break
            header = reader1_header+ ([self.column_header]* local_max)
        
        with open(self.output_file,'w',encoding='utf-8-sig') as output_file:
            output_writer  = csv.writer(output_file)
            output_writer.writerow(header)
            for row in self.row_list:
                output_writer.writerow(row)