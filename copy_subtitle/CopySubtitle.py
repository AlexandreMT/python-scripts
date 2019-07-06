import shutil

def getFilePath(release):
    return release[:release.rfind('/')]

originalRelease = input('Insira o nome do release do release base: ').replace("\\", "/")

filePath = getFilePath(originalRelease)

release = input('Insira o nome do release a ser criado: ')
releases = []
while release != '':
    releases.append(release)
    release = input('Insira o nome do release a ser criado: ')

for i in range(len(releases)):
    shutil.copyfile(originalRelease, filePath + '/' + releases[i] + '.srt')