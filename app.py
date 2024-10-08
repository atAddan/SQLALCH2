
from datetime import datetime
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from database import db, Books, janr


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bibl.db'
db.init_app(app)

""" with app.app_context():
    db.drop_all()
    db.create_all()

    fantastic = janr(text="Фантастика")
    fentesi = janr(text="Фентези")
    action = janr(text="Экшн")
    db.session.add(fantastic)
    db.session.add(fentesi)
    
    db.session.add(
        Books(
            author = "автор1",
            name = "книга1",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор2",
            name = "книга2",
            janr = fentesi,
        )
        
    )
    
    db.session.add(
        Books(
            author = "автор3",
            name = "книга3",
            janr = fentesi,
        )
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга4",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга5",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга6",
            janr = fantastic,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга7",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга8",
            janr = fantastic,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга9",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга10",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга11",
            janr = fantastic,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга12",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга13",
            janr = fantastic,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга14",
            janr = fentesi,
        )
        
    )
    db.session.add(
        Books(
            author = "автор1",
            name = "книга15",
            janr = fantastic,
        )
        
    )

    db.session.commit() """


@app.route("/")
def all_book():
    
    book = Books.query.limit(15).all()
    return render_template("all_book.html", book=book)


@app.route("/janr/<int:id_janr>")
def books_by_janr(id_janr):
    janrDef = janr.query.get_or_404(id_janr)
    return render_template(
        "books_by_janr.html", 
        janr_name = janrDef.text, 
        book = janrDef.book,
    )

if __name__ == "__main__":
    app.run(debug=True)