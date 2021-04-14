import os
import csv

#pasta "incident" onde estão os arquivos PRÉ IMPORTAÇÃO (de):
path = 'C:/Users/carlo/Documents/chamados/example/'
#pasta onde os anexos VÃO ESTAR de forma definitiva (para)
FutureDir = 'D:/TOPdesk/Uploads/incident/'
#nome do csv que vai ser gerado (não mudar):
csvName = 'files.csv'
#lugar onde você quer que o CSV esteja localizado
csvDestination ='C:/Users/carlo/Documents/chamados/csvDestination'

#variaveis diversas, não mexer
directory = ''
incidentNumber = ''


os.chdir(csvDestination)
print(os.getcwd())

with open( csvName, 'w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(["CallNumber", "filename", "size"])
    print("CallNumber ======= filename ======= size")

    for directory in os.listdir(path):

        rootDir = path + directory + '/'
        incidentNumber = directory


        for filenames in os.listdir(rootDir):

            attachmentName = filenames
            attachmentSizeInBytes = (os.stat(rootDir+filenames).st_size)
            printableSize = "| Size:" + str(attachmentSizeInBytes)
            printableDirectoryAndIncidentNumber = incidentNumber+ " | "+ FutureDir + incidentNumber +'/'+ filenames

            writer.writerow([incidentNumber, FutureDir + incidentNumber + '/' + filenames, attachmentSizeInBytes])
            
            print(printableDirectoryAndIncidentNumber, printableSize.rjust(os.get_terminal_size().columns+ -1 - len(printableDirectoryAndIncidentNumber)))

print("CSV criado com sucesso:", csvDestination+ csvName)
