from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app.extensions import db, cache
from sqlalchemy import distinct
from sqlalchemy import func, case
from sqlalchemy.orm import aliased


# -----------------------------------------------------------------------------
# Blueprint
# -----------------------------------------------------------------------------

blueprint = Blueprint(
    name='dashboard',
    import_name=__name__,
)


# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------

@blueprint.route('/')
# @login_required
def home():
    return render_template(
        template_name_or_list='dashboard/home.html',
    )


# -----------------------------------------------------------------------------
# Registering Filters
# -----------------------------------------------------------------------------

@blueprint.app_template_filter('sort_by')
def sort_by_attribute(items, attribute):
    return sorted(items, key=lambda x: getattr(x, attribute).lower())