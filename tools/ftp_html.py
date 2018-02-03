"""
CREAt: 2017/4/18
AUTHOR: Hehahutu
"""
from ftplib import FTP
import os


class FtpUpload():
    def __init__(self):
        self.ftp = FTP()

    def send_file(self, filename):
        self.ftp.connect('103.72.166.182', 8080, 50)
        self.ftp.login('admin', 'admin135')
        filename = filename
        self.ftp.storbinary(f'STOR /pub/{filename}', open(f'templates/test_log/{filename}', 'rb'), 8192)
        # self.ftp.set_debuglevel(0)
        self.ftp.close()
        # self.ftp.quit()
        print('文件上传成功')

#
# if __name__ == '__main__':
#     ftp = FtpUpload()
#     ftp.send_file()
