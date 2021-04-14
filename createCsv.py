import os
import csv

#pasta "incident" onde estão os arquivos PRÉ IMPORTAÇÃO (de):
path = '/Users/CarlosB/Desktop/incident/'
#pasta onde os anexos VÃO ESTAR de forma definitiva (para)
definitiveDirectory = 'D:/TOPdesk/Uploads/incident/'
#nome do csv que vai ser gerado (não mudar):
csvName = 'files.csv'
#lugar onde você quer que o CSV esteja localizado
csvDestination ='C:/Users/CarlosB/testeCSV/'

#variaveis diversas, não mexer
directory = ''
incidentNumber = ''


os.chdir(csvDestination)
print(os.getcwd())

with open( csvName, 'w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(["CallNumber", "filename", "size"])
    print("CallNumber ======= filename ======= size")

    for filenames in os.listdir(path):

        directory = path + filenames + '/'
        incidentNumber = filenames


        for filenames in os.listdir(path+filenames):

            attachmentName = filenames
            attachmentSizeInBytes = (os.stat(directory+filenames).st_size)
        
            writer.writerow([incidentNumber, definitiveDirectory + incidentNumber + '/' + filenames, attachmentSizeInBytes])
            print(incidentNumber, "|", definitiveDirectory + incidentNumber + filenames,"Size:", attachmentSizeInBytes)

print("CSV criado com sucesso:", csvDestination+ csvName)
