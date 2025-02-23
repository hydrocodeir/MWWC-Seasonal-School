from app.db import BaseModel
from app.extensions import db
from flask_login import UserMixin
from sqlalchemy import event


# ------------------------------------------------------------------------------
# Models                                           
# ------------------------------------------------------------------------------

class Register(BaseModel, UserMixin):
    
    __tablename__ = "register"
    
    first_name = db.Column(
        db.String(100),
        unique=False,
        nullable=False,
        info={'verbose_name': 'نام'}
    )
    
    last_name = db.Column(
        db.String(100),
        unique=False,
        nullable=False,
        info={'verbose_name': 'نام خانوادگی'}
    )
    
    national_id = db.Column(
        db.String(10),
        unique=True,
        nullable=False,
        info={'verbose_name': 'کد ملی'}
    )
    
    birthday = db.Column(
        db.String(10), 
        unique=False, 
        nullable=False,
        info={'verbose_name': 'تاریخ تولد'}
    )
    
    university = db.Column(
        db.String(50),
        unique=False,
        nullable=False,
        info={'verbose_name': 'دانشگاه'}
    )
    
    educational_stage = db.Column(
        db.String(20),
        unique=False, 
        nullable=False, 
        info={'verbose_name': 'مقطع تحصیلی'}
    )
    
    academic_discipline = db.Column(
        db.String(50), 
        unique=False, 
        nullable=False, 
        info={'verbose_name': 'رشته تحصیلی'}
    )
    
    score = db.Column(
        db.Float, 
        unique=False, 
        nullable=False, 
        info={'verbose_name': 'آخرین معدل'} 
    )
    
    phone_number = db.Column(
        db.String(11),
        unique=True,
        nullable=False,
        info={'verbose_name': 'شماره تماس'}
    )
    
    email = db.Column(
        db.String(100),
        unique=True, 
        nullable=False, 
        info={'verbose_name': 'ایمیل'}
    )
    
    address = db.Column(
        db.String(200),
        unique=False, 
        nullable=False,
        info={'verbose_name': 'آدرس محل سکونت'}
    )
    
    english = db.Column(
        db.String(30),
        unique=False, 
        nullable=False,
        info={'verbose_name': 'سطح زبان انگلیسی'}
    )
    
    programing = db.Column(
        db.String(30),
        unique=False, 
        nullable=False,
        info={'verbose_name': 'آشنایی با برنامه نویسی'}
    )
    
    publication = db.Column(
        db.String(30),
        unique=False, 
        nullable=False,
        info={'verbose_name': 'مدارک علمی'}
    )
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    