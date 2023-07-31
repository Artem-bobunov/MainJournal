import datetime


now = datetime.datetime.now()
dt_string =  now.strftime("%d.%m.%Y")
time_string =  now.strftime("%H:%M")


file = r'C:\Projects\MainJournal\journal_set\journal_set\logger\log.txt'

class LoggerJournal:

    def __init__(self,users, reg):
        self.users = str(users)
        self.reg = str(reg)

    def add_record(self):
        with open(file, 'a') as f:
            f.writelines("Регистрация в журнале,{},{},{}\n".format(self.users, self.reg,now))
            f.close()

    def update_record(self):
        with open (file,'a') as f:
            #for i in f.readline():
            f.writelines("Обновление в журнале,{},{},{},{}\n".format(self.users, self.reg,dt_string,time_string))
            f.close()
                #print("Пользователь {} обновил запись под № акта {}".format(self.users, self.number))

    def mark_users(self):
        with open(file, 'a') as f:
            # for i in f.readline():
            f.writelines("Подпись в журнале,{},{},{},{}\n".format(self.users, self.reg, dt_string, time_string))
            f.close()

    def delete_record(self):
        with open(file, 'a') as f:
            f.write('Пользователь {} удалил запись под №  {} \n'.format(self.users, self.reg))
            f.close()





