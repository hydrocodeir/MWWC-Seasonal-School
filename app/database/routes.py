import os
import secrets
from flask import (
    Blueprint, 
    render_template, 
    flash, 
    redirect, 
    url_for, 
    request, 
    jsonify
)
from app.extensions import db
from sqlalchemy import or_, asc, desc
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_required
from app.users.routes import role_required
from PIL import Image

from app.database.models import Register
from app.database.forms import RegisterForm

# -----------------------------------------------------------------------------
# Blueprint
# -----------------------------------------------------------------------------

blueprint = Blueprint(
    name='database',
    import_name=__name__,
)



# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------

@blueprint.route(rule='/database', methods=['GET', 'POST'])
@login_required
@role_required('کاربر عادی')
def home():
    return render_template(
        template_name_or_list='database/home.html',
    )


# -----------------------------------------------------------------------------
# APIs
# -----------------------------------------------------------------------------
