from registro_ig import app
from flask import render_template, request, redirect, url_for
from registro_ig.forms import MovementForm
from registro_ig.models import select_all, insert, select_by, updated_by
from datetime import date

@app.route("/")
def index():
    # consultar todos los movimientos de la BASE DE DATOS
    registros = select_all()
    return render_template("index.html", pageTitle="Todos", data = registros)

@app.route("/new", methods=["GET", "POST"])
def new():
    form = MovementForm()
    if request.method == "GET":
        return render_template("new.html", form=form, dataForm = "")
    else:
        if form.validate():
            insert([form.date.data.isoformat(), 
                    form.concept.data, 
                    form.quantity.data
                    ])

            return redirect(url_for("index"))
        else:
            return render_template("new.html", pageTitle="Alta", form=form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def modificar(id):
    form = MovementForm()
    if request.method == "GET":
        return render_template("update.html", form=form, dicc=select_by(id))
    else:
        if form.validate():
            updated_by([id,
                        form.date.data.isoformat(),
                        form.concept.data,
                        form.quantity.data])
            return redirect(url_for("index"))
        else:
            return render_template("update.html", pageTitle="Modificacion", form=form, 
                                    dicc={"id":id, "date":form.date.data.isoformat(),
                                    "concept":form.concept.data,
                                    "quantity":form.quantity.data})