from app import app, db
from app.models import Person, Phonenumber, Nationality, Junction
from flask import redirect, render_template
from faker import Faker
fake = Faker()

@app.route('/create_fakes')
def create_fakes():
    # create fake data
    name = fake.name()
    print(name)
    emailname = name.replace(' ', '')
    address = fake.address()
    print(address)
    number1 = fake.phone_number()
    print(number1)
    number2 = fake.phone_number()
    print(number2)
    country = fake.country()
    print(country)

    # create class instances
    person = Person(name,f'{emailname}@gmail.com',address)
    phone_number1 = Phonenumber(number1)
    phone_number2 = Phonenumber(number2)
    nationality = Nationality(country)
    junction = Junction()

    # phone number appends
    person.phonenumbers.append(phone_number1)
    person.phonenumbers.append(phone_number2)

    # nationality junction 
    person.nationality_junc.append(junction)
    nationality.person_junc.append(junction)

    # push to db
    db.session.add(person)
    db.session.add(phone_number1)
    db.session.add(phone_number2)
    db.session.add(nationality)
    db.session.add(junction)
    db.session.commit()
    return "fake created"


@app.route('/number/<phonenumber>')
# display all the info of a person depending on their phone number.
def number(phonenumber):
    number = Phonenumber.query.filter_by(number=phonenumber).first()
    try:
        person = Person.query.filter_by(id=number.person).first()
    except:
        return "number not found"
    return render_template('number.html', person_name=person.name, person_email=person.email, person_address=person.address)

@app.route('/name/<name>')
#  display all the info of a person depending on their name. display their phone number(s) as well.
def name(name):
    person = Person.query.filter_by(name=name).first()
    nationality = db.session.query(Nationality).join(Junction, Nationality.id==Junction.nationality_id).join(Person, Junction.person_id==Person.id).filter_by(name=name).first()
    print(nationality)
    try:
        number = Phonenumber.query.filter_by(person=person.id).all()
    except:
        return "number not found"
    print(number)
    return render_template('person.html', person_name=person.name, person_email=person.email, person_address=person.address, person_number=number, person_nationality=nationality.nationality)

@app.route('/nationality/<nationality>')
def nationality(nationality):
    people = []
    persons = db.session.query(Person).all()
    for person in persons:
        numbers = Phonenumber.query.filter_by(person=person.id).all()
        nationality = db.session.query(Nationality).join(Junction, Nationality.id==Junction.nationality_id).filter_by(person_id=person.id).join(Person, Junction.person_id==Person.id).first()
        person_tmp = {'name': person.name, 'email': person.email, 'address': person.address, 'numbers': numbers, 'nationality': nationality}
        people.append(person_tmp)
    return render_template('nationality.html', people=people)

