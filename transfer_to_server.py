import os
import re

STUDENT_NO_REGEX = r"e\d{7}"
TARGET_SERVER = "{student_number}@stu.comp.nus.edu.sg"


if __name__ == '__main__':
    print("This file transfer files from your local computer to stu.comp.nus.edu.sg")
    student_number = input('Student number: ')
    if not re.match(STUDENT_NO_REGEX, student_number):
        print('Invalid student number')
        exit(1)

    file_name = input('File name: ')
    if not os.path.isfile(file_name):
        print('File does not exist')
        exit(1)

    print(f"Transferring {file_name}")
    os.system("scp {file_name} {target_server}:.".format(
        file_name=file_name,
        target_server=TARGET_SERVER.format(
            student_number=student_number
        ),
    ))
    print("Transfer complete")
