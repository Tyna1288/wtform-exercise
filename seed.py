"""seed file to create smaple data for db"""

from models import Pet, db
from adopt import app


"""create tables"""
with app.app_context():
    db.drop_all()
    db.create_all()


    p1 = Pet(id='1', name='Woofly', age='3', species='dog', 
             photo_url='https://www.what-dog.net/Images/faces2/scroll001.jpg',notes='Incredibly adorable.', available=True)
    p2 = Pet(id='2', name='finley', age='4', species='porcupine',
             photo_url='http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', notes='Somewhat spiky.', available=True)
    p3 = Pet(id='3', name='mainley', age='2', species='cat',
             photo_url='https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', notes='Kitty kat!', available=False)
    p4 = Pet(id='4', name='marley', age='6', species='cat',
             photo_url='https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', notes='null.', available=True)
    

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)


    db.session.commit()

    