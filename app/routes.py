from flask import Blueprint, render_template, session, redirect, url_for
from .auth import login_required

bp = Blueprint("routes", __name__)

@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/login_vuln")
def login_vuln_get():
    return render_template("login_vuln.html")


@bp.get("/login_safe")
def login_safe_get():
    return render_template("login_safe.html")


@bp.get("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=session.get("username"))


@bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.index"))

