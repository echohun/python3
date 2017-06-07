import zipfile
def extractFile(toPath,zFile,password):
    try:
        zFile.extractall(path=toPath,pwd=password);
        print('SCUCESS'+password);
        return password;
    except Exception,e:
        return;
def main():
    zFile = zipfile.ZipFile("C:\Users\Leticia\Desktop\233.zip");
    passFile = open('C:\Users\Leticia\Desktop\mutou.txt');
    for line in passFile.readlines():
            password = line.strip('\N');
            guess = extractFile("C:\Users\Leticia\Desktop",zFile,password);
            if guess:
                print('SCUCESS'+password);
                exit(0);
if __name__=='__MAIN__':
    main();
