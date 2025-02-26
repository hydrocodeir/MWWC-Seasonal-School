import os
from flask import (
    Blueprint, 
    render_template, 
    jsonify, 
    redirect, 
    url_for, 
    flash, 
    request,
    send_from_directory,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db, cache
from sqlalchemy import distinct
from sqlalchemy import func, case
from sqlalchemy.orm import aliased
from app.database.models import Register
from app.database.forms import RegisterForm
from app.bot import send_new_register

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


def save_resume(form_resume, nid):
    _, f_ext = os.path.splitext(form_resume.filename)
    resume_fn = nid + f_ext
    resume_path = os.path.join('app/assets/uploads', resume_fn)
    form_resume.save(resume_path)
    return resume_path, resume_fn



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
            phone_number = virastarStr(form.phone_number.data)
            email = virastarStr(form.email.data)
            
            university = virastarStr(form.university.data)
            educational_stage = virastarStr(form.educational_stage.data)
            academic_discipline = virastarStr(form.academic_discipline.data)
            score = float(form.score.data)
            student_identification_number = virastarStr(form.student_identification_number.data)

            accommodation = virastarStr(form.accommodation.data)
            english = virastarStr(form.english.data)
            programing = virastarStr(form.programing.data)
            
            selected_programing_language = request.form.getlist('programing_language')
            selected_programing_language = ','.join(selected_programing_language)
            programing_language = virastarStr(selected_programing_language)
            
            if form.resume.data:
                resume_path, resume = save_resume(form_resume=form.resume.data, nid=national_id)
                
            
            
            register = Register(
                first_name=first_name,
                last_name=last_name,
                national_id=national_id,
                birthday=birthday,
                phone_number=phone_number,
                email=email,
                
                university=university,
                educational_stage=educational_stage,
                academic_discipline=academic_discipline,
                score=score,
                student_identification_number=student_identification_number,
                
                accommodation=accommodation,
                english=english,
                programing=programing,
                programing_language=programing_language,
                resume=resume
            )
            
            db.session.add(register)
            db.session.commit()
            
            flash('اطلاعات با موفقیت ثبت شد!', 'success')
            
            send_new_register(
                text=f"متقاضی جدیدی ثبت نام کرد:\nنام: {first_name}\nنام خانوادگی: {last_name}\nدانشگاه: {university}\nمقطع تحصیلی: {educational_stage}\nرشته تحصیلی: {academic_discipline}\n",
                file_path=resume_path
            )
            return redirect(location=url_for(endpoint='dashboard.home'))
        
    return render_template(
        template_name_or_list='dashboard/home.html',
        form=form
    )


@blueprint.route('/resume_template', methods=['GET', 'POST'])
def download_resume_template():   
    return send_from_directory(
        directory=os.path.join(current_app.root_path, 'assets', 'uploads'), 
        path="resume.docx",
        as_attachment=True
    )


# -----------------------------------------------------------------------------
# Registering Filters
# -----------------------------------------------------------------------------

@blueprint.app_template_filter('sort_by')
def sort_by_attribute(items, attribute):
    return sorted(items, key=lambda x: getattr(x, attribute).lower())