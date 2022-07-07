from src.studi_kasus_2 import StudiKasus2
import os

if __name__ == '__main__':
    main_class = StudiKasus2('localhost', '3306', 'root',  os.environ["MYSQL_PASS"])
    df = main_class.import_csv('data/Mall_Customers.csv')
    print(main_class.create_db('Mall_Customers'))
    print(main_class.create_table('Mall_Customers','Customers',df))
    print(main_class.load_data('Mall_Customers', 'Customers'))
