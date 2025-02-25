from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    FloatField,
    SelectField,
    DecimalField,
    TextAreaField,
    SelectMultipleField
)
from flask_wtf.file import (
    FileAllowed, 
    FileField
)
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    InputRequired,
    NumberRange,
    Email
)


# ------------------------------------------------------------------------------
# Validate Functions
# ------------------------------------------------------------------------------

def validate_phone_start(form, field):
    if not field.data.startswith('09'):
        raise ValidationError('شماره تلفن باید با 09 شروع شود!')


def validate_iranian_national_code(form, field):
    code = field.data
    code_len = len(code)

    if code_len > 10 or code_len < 8:
        raise ValidationError('کد ملی میتواند 8 تا 10 رقم باشد!')

    if len(set(code)) == 1:
        raise ValidationError('همه ارقام کدملی نمیتواند یکسان باشد!')

    if len(code) < 10:
        code = code.zfill(10)

    factors = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    checksum = sum(int(code[i]) * factors[i] for i in range(len(code) - 1))
    remainder = checksum % 11
    last_digit = int(code[-1])

    if remainder < 2:
        if remainder != last_digit:
            raise ValidationError('کدملی اشتباه وارد شده است!')
    else:
        if 11 - remainder != last_digit:
            raise ValidationError('کدملی اشتباه وارد شده است!')

# -----------------------------------------------------------------------------
# Forms
# -----------------------------------------------------------------------------


class RegisterForm(FlaskForm):

    first_name = StringField(
        label='نام',
        validators=[
            DataRequired(
                message="وارد کردن نام الزامیست!"
            ),
            Length(
                max=100,
                message='حداکثر 100 کاراکتر!'
            )
        ],
        render_kw={
            "placeholder": "نام را وارد کنید"
        }
    )

    last_name = StringField(
        label='نام خانوادگی',
        validators=[
            DataRequired(
                message="وارد کردن نام خانوادگی الزامیست!"
            ),
            Length(
                max=100,
                message='حداکثر 100 کاراکتر!'
            )
        ],
        render_kw={
            "placeholder": "نام خانوادگی را وارد کنید"
        }
    )

    national_id = StringField(
        label='کدملی',
        validators=[
            DataRequired(
                message="وارد کردن کدملی الزامیست!"
            ),
            validate_iranian_national_code
        ],
        render_kw={
            "placeholder": "کدملی را وارد کنید"
        }
    )

    birthday = StringField(
        label='تاریخ تولد',
        validators=[
            DataRequired(
                message="وارد کردن تاریخ تولد الزامیست!"
            ),
            Length(
                max=100,
                message='حداکثر 100 کاراکتر!'
            )
        ],
        render_kw={
            "placeholder": "تاریخ تولد را انتخاب کنید",
            'data-jdp': 'true'
        }
    )
    
    phone_number = StringField(
        label='تلفن همراه',
        validators=[
            DataRequired(
                message="وارد کردن تلفن همراه الزامیست!"
            ),
            Length(
                min=11,
                max=11,
                message='تلفن همراه میتواند 11 کاراکتر باشد!'
            ),
            validate_phone_start
        ],
        render_kw={
            "placeholder": "تلفن همراه را وارد کنید"
        }
    )

    email = StringField(
        label='ایمیل',
        validators=[
            DataRequired(
                message="وارد کردن ایمیل الزامیست!"
            ),
            Email(
                message='ایمیل معتبر نیست!'
            ),
        ],
        render_kw={
            "placeholder": "ایمیل را وارد کنید"
        }
    )

    university = SelectField(
        label='دانشگاه',
        validators=[
            DataRequired(
                message="انتخاب دانشگاه الزامیست!"
            ),
            Length(
                max=50,
                message='حداکثر 30 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "دانشگاه را انتخاب کنید"
        }
    )

    educational_stage = SelectField(
        label='مقطع تحصیلی',
        validators=[
            DataRequired(
                message="انتخاب مقطع تحصیلی الزامیست!"
            ),
            Length(
                max=20,
                message='حداکثر 20 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "مقطع تحصیلی را انتخاب کنید"
        }
    )

    academic_discipline = SelectField(
        label='رشته تحصیلی',
        validators=[
            DataRequired(
                message="وارد کردن رشته تحصیلی الزامیست!"
            ),
            Length(
                max=50,
                message='حداکثر 50 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "رشته تحصیلی را وارد کنید"
        }
    )

    score = FloatField(
        label='آخرین معدل',
        validators=[
            DataRequired(
                message="وارد کردن معدل الزامیست!"
            ),
            NumberRange(min=0, max=20, message="معدل باید بین 0 و 20 باشد.")
        ],
        render_kw={
            "placeholder": "معدل را وارد کنید"
        }
    )
    
    student_identification_number = StringField(
        label='شماره دانشجویی',
        validators=[
            DataRequired(
                message="وارد کردن شماره دانشجویی الزامیست!"
            ),
            Length(
                max=100,
                message='حداکثر 15 کاراکتر!'
            )
        ],
        render_kw={
            "placeholder": "شماره دانشجویی را وارد کنید",
        }
    )

    accommodation = SelectField(
        label='نیاز به اسکان دارید؟',
        validators=[
            DataRequired(
                message="انتخاب کردن نیاز به اسکان الزامیست!"
            ),
            Length(
                max=10,
                message='حداکثر 10 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "نیاز به اسکان خود را انتخاب کنید"
        }
    )
    
    english = SelectField(
        label='انتخاب سطح زبان انگلیسی',
        validators=[
            DataRequired(
                message="وارد کردن سطح زبان انگلیسی الزامیست!"
            ),
            Length(
                max=30,
                message='حداکثر 30 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "سطح زبان انگلیسی"
        }
    )
    
    programing = SelectField(
        label='انتخاب سطح آشنایی با زبان‌های برنامه نویسی',
        validators=[
            DataRequired(
                message="انتخاب سطح آشنایی با زبان‌های برنامه نویسی الزامیست!!"
            ),
            Length(
                max=30,
                message='حداکثر 30 کاراکتر!'
            )
        ],
        default='',
        render_kw={
            "data-placeholder": "آشنایی با زبان‌های برنامه‌نویسی"
        }
    )
    
    programing_language = SelectMultipleField(
        label='زبان‌های برنامه نویسی',
        choices=[],
        validators=[
            DataRequired(
                message="حداقل انتخاب یک مورد الزامیست!"
            )
        ],
        render_kw={
            "data-placeholder": "حداقل یک مورد را انتخاب کنید"
        }
    )
    
    
    resume = FileField(
        label='رزومه علمی',
        validators=[
            DataRequired(
                message="بارگزاری رزومه الزامیست!"
            ),
            FileAllowed(upload_set=['pdf', 'doc', 'docx'], message="فایل های مجاز: PDF, DOC, DOCX")
        ],
        render_kw={
            "placeholder": "رزومه علمی را بارگزاری کنید"
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.university.choices = [
            ('', 'انتخاب دانشگاه ...'),
            ('دانشگاه فردوسی مشهد', 'دانشگاه فردوسی مشهد'),
            ('دانشگاه بیرجند', 'دانشگاه بیرجند'),
            ('دانشگاه صنعتی بیرجند', 'دانشگاه صنعتی بیرجند'),
            ('دانشگاه بجنورد', 'دانشگاه بجنورد'),
            ('دانشگاه سجاد', 'دانشگاه سجاد'),
            ('دانشگاه آزاد اسلامی واحد مشهد', 'دانشگاه آزاد اسلامی واحد مشهد'),
            ('مجتمع آموزش عالی گناباد', 'مجتمع آموزش عالی گناباد'),
            ('دانشگاه خیام', 'دانشگاه خیام'),
            ('دانشگاه مازندران', 'دانشگاه مازندران'),
        ]
        self.educational_stage.choices = [
            ('', 'انتخاب مقطع تحصیلی ...'),
            ('کارشناسی ارشد', 'کارشناسی ارشد'),
            ('دکتری', 'دکتری'),
        ]
        self.academic_discipline.choices = [
            ('', 'انتخاب رشته تحصیلی ...'),
            ('علوم و مهندسی کامپیوتر و هوش مصنوعی',
            'علوم و مهندسی کامپیوتر و هوش مصنوعی'),
            ('مهندسی برق', 'مهندسی برق'),
            ('مهندسی عمران', 'مهندسی عمران'),
            ('علوم و مهندسی آب', 'علوم و مهندسی آب'),
            ('ریاضیات کاربردی', 'ریاضیات کاربردی'),
        ]
        self.accommodation.choices = [
            ('', 'انتخاب نیاز به اسکان ...'),
            ('بله', 'بله'),
            ('خیر', 'خیر'),
        ]
        self.programing.choices = [
            ('', 'انتخاب سطح آشنایی با زبان‌های برنامه نویسی ...'),
            ('مبتدی', 'مبتدی'),
            ('متوسط', 'متوسط'),
            ('پیشرفته', 'پیشرفته'),            
        ]
        self.english.choices = [
            ('', 'انتخاب سطح زبان انگلیسی ...'),
            ('مبتدی', 'مبتدی'),
            ('متوسط', 'متوسط'),
            ('پیشرفته', 'پیشرفته'),
        ]
        self.programing_language.choices = [
            ('', 'انتخاب یک مورد الزامیست ...'),
            ('هیچکدام', 'هیچکدام'),
            ('Python', 'Python'),
            ('MATLAB', 'MATLAB'),
            ('R', 'R'),
            ('JavaScript', 'JavaScript'),
            ('C, C++, C#', 'C, C++, C#'),
            ('Julia', 'Julia'),
            ('ّFortran', 'ّFortran'),
            ('زبان های دیگر', 'زبان های دیگر'),
        ]
