import os
import shutil


class ReadPathFiles():
    def __init__(self, directory):
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) if arq.lower().endswith('.xml')]


if __name__ == '__main__':
    paths = ReadPathFiles('2022').all_files()
    contagem_arquivos = 1
    num = 1
    for path in paths:
        if contagem_arquivos == 1:
            os.mkdir(f'dir{num}')
            nova_pasta = f'dir{num}'
            num += 1
        if contagem_arquivos < 30:
            arquivo = os.getcwd() + os.sep + f'{nova_pasta}'
            shutil.move(path, arquivo)
            contagem_arquivos += 1
        else:
            arquivo = os.getcwd() + os.sep + f'{nova_pasta}'
            shutil.move(path, arquivo)
            contagem_arquivos = 1

    shutil.rmtree(path='2022')
