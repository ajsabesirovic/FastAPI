from sqlalchemy import create_engine
DATABASE_URL = 'sqlite:///.blog.db'
engine = create_engine(DATABASE_URL,connect_args={'check_same_thread':False})