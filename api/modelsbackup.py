# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from rest_framework_simplejwt.tokens import Token
# from PIL import Image
# import io #only use above 2 if stored binaryfield blob directly in db
 
class Photographer(AbstractBaseUser):
    pusername = models.CharField(db_column='PUSERNAME', primary_key=True, max_length=30)
    firstname = models.CharField(db_column='FIRSTNAME', max_length=30)
    lastname = models.CharField(db_column='LASTNAME', max_length=30)
    mobile_no = models.IntegerField(db_column='MOBILE_NO')
    streetname = models.CharField(db_column='STREETNAME', max_length=100)
    city = models.CharField(db_column='CITY', max_length=50)
    pincode = models.IntegerField(db_column='PINCODE')
    state = models.CharField(db_column='STATE', max_length=50)
    email = models.EmailField(db_column='EMAIL_ID', max_length=100)
    #document = models.BinaryField(db_column='DOCUMENT')  # BinaryField to store image data directly in the database
    document = models.FileField(db_column='DOCUMENT',upload_to='images/')
    password = models.CharField(db_column='P_PASSWORD', max_length=100)
    other = models.CharField(db_column='OTHER', max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    last_login = models.DateTimeField(auto_now=True)
    id=models.IntegerField(null=True)
   
    USERNAME_FIELD = 'pusername'

    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.pusername


    class Meta:
        # managed = False
        db_table = 'photographer'

class User(models.Model):
    username = models.CharField(db_column='USERNAME', primary_key=True, max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=30)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=30)  # Field name made lowercase.
    mobile_no = models.IntegerField(db_column='MOBILE_NO')  # Field name made lowercase.
    email = models.EmailField(db_column='EMAIL_ID', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='USER_PASSWORD', max_length=100)  # Field name made lowercase.
    experience = models.IntegerField(db_column='EXPERIENCE')  # Field name made lowercase.
    other = models.CharField(db_column='OTHER', max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending') # Field name made lowercase.
    id=models.IntegerField(null=True)
    last_login = models.DateTimeField(auto_now=True)
    get_email_field_name=models.CharField(max_length=200,null=True)

    
    # USERNAME_FIELD = 'email'
    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.username


    class Meta:
        db_table = 'user'
    


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.IntegerField()
    title = models.CharField(max_length=50)
    title_visible = models.IntegerField()
    logo = models.CharField(max_length=100)
    logo_visible = models.IntegerField()
    css_header_background_color = models.CharField(max_length=10)
    title_color = models.CharField(max_length=10)
    css_header_text_color = models.CharField(max_length=10)
    css_header_link_color = models.CharField(max_length=10)
    css_header_link_hover_color = models.CharField(max_length=10)
    css_module_background_color = models.CharField(max_length=10)
    css_module_text_color = models.CharField(max_length=10)
    css_module_link_color = models.CharField(max_length=10)
    css_module_link_hover_color = models.CharField(max_length=10)
    css_module_rounded_corners = models.IntegerField()
    css_generic_link_color = models.CharField(max_length=10)
    css_generic_link_hover_color = models.CharField(max_length=10)
    css_save_button_background_color = models.CharField(max_length=10)
    css_save_button_background_hover_color = models.CharField(max_length=10)
    css_save_button_text_color = models.CharField(max_length=10)
    css_delete_button_background_color = models.CharField(max_length=10)
    css_delete_button_background_hover_color = models.CharField(max_length=10)
    css_delete_button_text_color = models.CharField(max_length=10)
    list_filter_dropdown = models.IntegerField()
    related_modal_active = models.IntegerField()
    related_modal_background_color = models.CharField(max_length=10)
    related_modal_rounded_corners = models.IntegerField()
    logo_color = models.CharField(max_length=10)
    recent_actions_visible = models.IntegerField()
    favicon = models.CharField(max_length=100)
    related_modal_background_opacity = models.CharField(max_length=5)
    env_name = models.CharField(max_length=50)
    env_visible_in_header = models.IntegerField()
    env_color = models.CharField(max_length=10)
    env_visible_in_favicon = models.IntegerField()
    related_modal_close_button_visible = models.IntegerField()
    language_chooser_active = models.IntegerField()
    language_chooser_display = models.CharField(max_length=10)
    list_filter_sticky = models.IntegerField()
    form_pagination_sticky = models.IntegerField()
    form_submit_sticky = models.IntegerField()
    css_module_background_selected_color = models.CharField(max_length=10)
    css_module_link_selected_color = models.CharField(max_length=10)
    logo_max_height = models.PositiveSmallIntegerField()
    logo_max_width = models.PositiveSmallIntegerField()
    foldable_apps = models.IntegerField()
    language_chooser_control = models.CharField(max_length=20)
    list_filter_highlight = models.IntegerField()
    list_filter_removal_links = models.IntegerField()
    show_fieldsets_as_tabs = models.IntegerField()
    show_inlines_as_tabs = models.IntegerField()
    css_generic_link_active_color = models.CharField(max_length=10)
    collapsible_stacked_inlines = models.IntegerField()
    collapsible_stacked_inlines_collapsed = models.IntegerField()
    collapsible_tabular_inlines = models.IntegerField()
    collapsible_tabular_inlines_collapsed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class Album(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.ImageField(db_column='IMAGE', max_length=200)  # Field name made lowercase.
    pusername = models.ForeignKey('Photographer', models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.

    # class Meta:
    db_table = 'album'


# class Login(models.Model):
#     username=models.CharField(max_length = 50)
#     password=models.CharField(max_length = 12)
#     # is_approved = models.BooleanField(default=False)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    
#     def __str__(self):
#         return self.username



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'

class BookingForm(models.Model):
    booking_id = models.AutoField(db_column='BOOKING_ID', primary_key=True)  # Field name made lowercase.
    type_of_event = models.CharField(db_column='TYPE_OF_EVENT', max_length=20)  # Field name made lowercase.
    location_of_event = models.CharField(db_column='LOCATION_OF_EVENT', max_length=200)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE')  # Field name made lowercase.
    budget = models.IntegerField(db_column='BUDGET')  # Field name made lowercase.
    additional_comments = models.CharField(db_column='ADDITIONAL_COMMENTS', max_length=100)  # Field name made lowercase.
    username = models.ForeignKey('User', models.CASCADE, db_column='USERNAME')  # Field name made lowercase.
    pusername = models.ForeignKey('Photographer', models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.
    submitted_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    
    class Meta:
        # managed = False
        db_table = 'booking form'


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=100)  # Field name made lowercase.
    pusername = models.ForeignKey('Photographer', models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    # auth_token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_session'


class Hire(models.Model):
    hire_id = models.AutoField(db_column='HIRE_ID', primary_key=True)  # Field name made lowercase.
    model_hire = models.CharField(db_column='MODEL_HIRE', max_length=3)  # Field name made lowercase.
    staff_hire = models.CharField(db_column='STAFF_HIRE', max_length=3)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=100)  # Field name made lowercase.
    experience_needed = models.IntegerField(db_column='EXPERIENCE_NEEDED')  # Field name made lowercase.
    skills_required = models.CharField(db_column='SKILLS_REQUIRED', max_length=50)  # Field name made lowercase.
    email_id = models.EmailField(db_column='EMAIL_ID', max_length=100)  # Field name made lowercase.
    pusername = models.ForeignKey('Photographer', models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.
    submitted_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    class Meta:
        # managed = False
        db_table = 'hire'


class Notification(models.Model):
    n_id = models.AutoField(db_column='N_ID', primary_key=True)  # Field name made lowercase.
    to_photographer = models.CharField(db_column='TO_PHOTOGRAPHER', max_length=100)  # Field name made lowercase.
    to_user = models.CharField(db_column='TO_USER', max_length=100)  # Field name made lowercase.
    pusername = models.ForeignKey('Photographer', models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.
    username = models.ForeignKey('User', models.CASCADE, db_column='USERNAME')  # Field name made lowercase.
    
    class Meta:
        # managed = False
        db_table = 'notification'





class Portfolio(models.Model):
    portfolio_id = models.AutoField(db_column='PORTFOLIO_ID', primary_key=True)  # Field name made lowercase.
    equipment = models.CharField(db_column='EQUIPMENT', max_length=100)  # Field name made lowercase.
    overview = models.CharField(db_column='OVERVIEW', max_length=100)  # Field name made lowercase.
    experience = models.IntegerField(db_column='EXPERIENCE')  # Field name made lowercase.
    starting_price = models.IntegerField(db_column='STARTING_PRICE')  # Field name made lowercase.
    skills = models.CharField(db_column='SKILLS', max_length=150)  # Field name made lowercase.
    language_known = models.CharField(db_column='LANGUAGE_KNOWN', max_length=50)  # Field name made lowercase.
    pusername = models.ForeignKey(Photographer, models.CASCADE, db_column='PUSERNAME')  # Field name made lowercase.
    submitted_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    class Meta:
        # managed = False
        db_table = 'portfolio'






       




