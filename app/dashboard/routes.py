from flask import (
    Blueprint, 
    render_template, 
    jsonify, 
    redirect, 
    url_for, 
    flash, 
    request
)
from flask_login import current_user, login_required
from app.extensions import db, cache
from sqlalchemy import distinct
from sqlalchemy import func, case
from sqlalchemy.orm import aliased
from app.database.models import Register
from app.database.forms import RegisterForm

# -----------------------------------------------------------------------------
# Blueprint
# -----------------------------------------------------------------------------

blueprint = Blueprint(
    name='dashboard',
    import_name=__name__,
)


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

def virastarStr(x):
    x = str(x)
    x = x.rstrip()
    x = x.lstrip()
    x = x.replace(' +', ' ')
    return str(x)



# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------

@blueprint.route('/', methods=['GET', 'POST'])
def home():
    
    form = RegisterForm()
        
    if request.method == 'POST':
        
        form_id = request.form.get('form_id')
        
        if form_id == 'register' and form.validate_on_submit():
            
            # check national_id duplicate
            national_id = virastarStr(form.national_id.data)
            if Register.query.filter_by(national_id=national_id).first():
                flash('کد ملی تکراری است!', 'danger')
                return redirect(location=url_for(endpoint='dashboard.home'))
            
            # check email duplicate
            email = virastarStr(form.email.data)
            if Register.query.filter_by(email=email).first():
                flash('ایمیل تکراری است!', 'danger')
                return redirect(location=url_for(endpoint='dashboard.home'))
            
            # check phone_number duplicate
            phone_number = virastarStr(form.phone_number.data)
            if Register.query.filter_by(phone_number=phone_number).first():
                flash('شماره تلفن تکراری است!', 'danger')
                return redirect(location=url_for(endpoint='dashboard.home'))
                              
            first_name = virastarStr(form.first_name.data)
            last_name = virastarStr(form.last_name.data)
            national_id = virastarStr(form.national_id.data)
            birthday = virastarStr(form.birthday.data)
            university = virastarStr(form.university.data)
            educational_stage = virastarStr(form.educational_stage.data)
            academic_discipline = virastarStr(form.academic_discipline.data)
            score = float(form.score.data)
            phone_number = virastarStr(form.phone_number.data)
            email = virastarStr(form.email.data)
            address = virastarStr(form.address.data)
            english = virastarStr(form.english.data)
            programing = virastarStr(form.programing.data)
            publication = virastarStr(form.publication.data)
            
            register = Register(
                first_name=first_name,
                last_name=last_name,
                national_id=national_id,
                birthday=birthday,
                university=university,
                educational_stage=educational_stage,
                academic_discipline=academic_discipline,
                score=score,
                phone_number=phone_number,
                email=email,
                address=address,
                english=english,
                programing=programing,
                publication=publication,
            )
            
            db.session.add(register)
            db.session.commit()
            
            flash('اطلاعات با موفقیت ثبت شد!', 'success')
            return redirect(location=url_for(endpoint='dashboard.home'))
        
    return render_template(
        template_name_or_list='dashboard/home.html',
        form=form
    )


# -----------------------------------------------------------------------------
# Registering Filters
# -----------------------------------------------------------------------------

@blueprint.app_template_filter('sort_by')
def sort_by_attribute(items, attribute):
    return sorted(items, key=lambda x: getattr(x, attribute).lower())