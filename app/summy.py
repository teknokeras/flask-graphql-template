from database.base import engine, db_session, Base 
from database.department import Department 
from database.employee import Employee

Base.metadata.create_all(bind=engine)

# Fill the tables with some data
engineering = Department(name='Engineering')
db_session.add(engineering)

hr = Department(name='Human Resources')
db_session.add(hr)

peter = Employee(name='Peter', department=engineering)
db_session.add(peter)

roy = Employee(name='Roy', department=engineering)
db_session.add(roy)

tracy = Employee(name='Tracy', department=hr)
db_session.add(tracy)
db_session.commit()