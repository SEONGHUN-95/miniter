test_db = {			
    'user'     : 'root',
    'password' : 'rntjdgns526!',
    'host'     : 'localhost',
    'port'     : 3306,
    'database' : 'database-1'
}

test_config = {		
    'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8"
}