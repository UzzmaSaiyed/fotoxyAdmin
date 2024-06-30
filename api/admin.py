from django.contrib import admin
from .models import *



# class LoginAdmin(admin.ModelAdmin):
#     list_display = ['username','password','submitted_at','approval_status']
#     actions = ['approve_records', 'reject_records']

#     def approve_records(self, request, queryset):
#         queryset.update(approval_status='approved')

#     def reject_records(self, request, queryset):
#         queryset.filter(approval_status='rejected').delete()

#User
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','firstname','lastname','mobile_no','email','password','experience','other','submitted_at','approval_status']
    actions = ['approve_user', 'reject_user']

    def approve_user(self, request, queryset):
        queryset.update(approval_status='approved')

    def reject_user(self, request, queryset):
        queryset.filter(approval_status='rejected').delete()

#Photographer
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ['pusername','firstname','lastname','mobile_no','streetname','city','pincode','state','email','document','password','other','submitted_at','approval_status']
    actions = ['approve_photographer', 'reject_photographer']

    def approve_photographer(self, request, queryset):
        queryset.update(approval_status='approved')

    def reject_photographer(self, request, queryset):
        queryset.filter(approval_status='rejected').delete()

#Portfolio
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['portfolio_id','equipment','overview','experience','starting_price','skills','language_known','pusername','submitted_at','approval_status']
    actions = ['approve_portfolio', 'reject_portfolio']

    def approve_portfolio(self, request, queryset):
        queryset.update(approval_status='approved')

    def reject_portfolio(self, request, queryset):
        queryset.filter(approval_status='rejected').delete()
#Hire
class HireAdmin(admin.ModelAdmin):
    list_display = ['hire_id','model_hire','staff_hire', 'comment','experience_needed','skills_required','email_id','pusername','submitted_at','approval_status']
    actions = ['approve_hire', 'reject_hire']

    def approve_hire(self, request, queryset):
        queryset.update(approval_status='approved')

    def reject_hire(self, request, queryset):
        queryset.filter(approval_status='rejected').delete()
#BookingForm
class BookingFormAdmin(admin.ModelAdmin):
    list_display = ['booking_id','type_of_event','location_of_event','start_date','budget','additional_comments','username','pusername','submitted_at','approval_status']
    actions = ['approve_bookingform', 'reject_bookingform']

    def approve_bookingform(self, request, queryset):
        queryset.update(approval_status='approved')

    def reject_bookingform(self, request, queryset):
        queryset.filter(approval_status='rejected').delete()
#Album
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id','image','pusername']

#Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','pusername']

#Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['n_id','to_photographer','to_user','pusername','username']

# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Photographer,PhotographerAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(BookingForm,BookingFormAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Hire,HireAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Portfolio,PortfolioAdmin)






