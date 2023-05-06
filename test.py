from database import SessionLocal

from models import Question

from datetime import datetime

db = SessionLocal()
for i in range(300):
     q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=datetime.now())
     db.add(q)

db.commit()

#<a use:link class="nav-link" href="https://github.com/login/oauth/authorize?client_id=994695e52ea17b472426">로그인</a>