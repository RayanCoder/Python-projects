Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class File:

    @staticmethod
    def get_accounts():
        with open('accounts.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_account(username, password):
        with open('accounts.txt', 'a') as file:
            file.write(username)
            file.write(', ')
            file.write(password)
            file.write('\n')

    @staticmethod
    def get_students():
        with open('student_details.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_student(student_details):
        with open('student_details.txt', 'a') as file:
            file.write(student_details)
            file.write('\n')

    @staticmethod
    def remove_student(student_id):
        pass