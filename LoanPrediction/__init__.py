import importdata

db = importdata.loandb('loandb.db')
db.createtable()

#train
#db.importtext(r'datasource\train\user_info_train.txt')
#db.importtext(r'datasource\train\bank_detail_train.txt','bank_detail_train')
#db.importtext(r'datasource\train\browse_history_train.txt','browse_history_train')
#db.importtext(r'datasource\train\bill_detail_train.txt','bill_detail_train')
#db.importtext(r'datasource\train\loan_time_train.txt','loan_time_train')
#db.importtext(r'datasource\train\overdue_train.txt','overdue_train')

#test
#db.importtext(r'datasource\test\user_info_test.txt','user_info_test')
#db.importtext(r'datasource\test\bank_detail_test.txt','bank_detail_test')
#db.importtext(r'datasource\test\browse_history_test.txt','browse_history_test')
#db.importtext(r'datasource\test\bill_detail_test.txt','bill_detail_test')
#db.importtext(r'datasource\test\loan_time_test.txt','loan_time_test')
#db.importtext(r'datasource\test\usersID_test.txt','usersID_test')