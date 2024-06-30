# Generated by Django 3.2.25 on 2024-04-15 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInterfaceTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('active', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('title_visible', models.IntegerField()),
                ('logo', models.CharField(max_length=100)),
                ('logo_visible', models.IntegerField()),
                ('css_header_background_color', models.CharField(max_length=10)),
                ('title_color', models.CharField(max_length=10)),
                ('css_header_text_color', models.CharField(max_length=10)),
                ('css_header_link_color', models.CharField(max_length=10)),
                ('css_header_link_hover_color', models.CharField(max_length=10)),
                ('css_module_background_color', models.CharField(max_length=10)),
                ('css_module_text_color', models.CharField(max_length=10)),
                ('css_module_link_color', models.CharField(max_length=10)),
                ('css_module_link_hover_color', models.CharField(max_length=10)),
                ('css_module_rounded_corners', models.IntegerField()),
                ('css_generic_link_color', models.CharField(max_length=10)),
                ('css_generic_link_hover_color', models.CharField(max_length=10)),
                ('css_save_button_background_color', models.CharField(max_length=10)),
                ('css_save_button_background_hover_color', models.CharField(max_length=10)),
                ('css_save_button_text_color', models.CharField(max_length=10)),
                ('css_delete_button_background_color', models.CharField(max_length=10)),
                ('css_delete_button_background_hover_color', models.CharField(max_length=10)),
                ('css_delete_button_text_color', models.CharField(max_length=10)),
                ('list_filter_dropdown', models.IntegerField()),
                ('related_modal_active', models.IntegerField()),
                ('related_modal_background_color', models.CharField(max_length=10)),
                ('related_modal_rounded_corners', models.IntegerField()),
                ('logo_color', models.CharField(max_length=10)),
                ('recent_actions_visible', models.IntegerField()),
                ('favicon', models.CharField(max_length=100)),
                ('related_modal_background_opacity', models.CharField(max_length=5)),
                ('env_name', models.CharField(max_length=50)),
                ('env_visible_in_header', models.IntegerField()),
                ('env_color', models.CharField(max_length=10)),
                ('env_visible_in_favicon', models.IntegerField()),
                ('related_modal_close_button_visible', models.IntegerField()),
                ('language_chooser_active', models.IntegerField()),
                ('language_chooser_display', models.CharField(max_length=10)),
                ('list_filter_sticky', models.IntegerField()),
                ('form_pagination_sticky', models.IntegerField()),
                ('form_submit_sticky', models.IntegerField()),
                ('css_module_background_selected_color', models.CharField(max_length=10)),
                ('css_module_link_selected_color', models.CharField(max_length=10)),
                ('logo_max_height', models.PositiveSmallIntegerField()),
                ('logo_max_width', models.PositiveSmallIntegerField()),
                ('foldable_apps', models.IntegerField()),
                ('language_chooser_control', models.CharField(max_length=20)),
                ('list_filter_highlight', models.IntegerField()),
                ('list_filter_removal_links', models.IntegerField()),
                ('show_fieldsets_as_tabs', models.IntegerField()),
                ('show_inlines_as_tabs', models.IntegerField()),
                ('css_generic_link_active_color', models.CharField(max_length=10)),
                ('collapsible_stacked_inlines', models.IntegerField()),
                ('collapsible_stacked_inlines_collapsed', models.IntegerField()),
                ('collapsible_tabular_inlines', models.IntegerField()),
                ('collapsible_tabular_inlines_collapsed', models.IntegerField()),
            ],
            options={
                'db_table': 'admin_interface_theme',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('pusername', models.CharField(db_column='PUSERNAME', max_length=30, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FIRSTNAME', max_length=30)),
                ('lastname', models.CharField(db_column='LASTNAME', max_length=30)),
                ('mobile_no', models.IntegerField(db_column='MOBILE_NO')),
                ('streetname', models.CharField(db_column='STREETNAME', max_length=100)),
                ('city', models.CharField(db_column='CITY', max_length=50)),
                ('pincode', models.IntegerField(db_column='PINCODE')),
                ('state', models.CharField(db_column='STATE', max_length=50)),
                ('email', models.EmailField(db_column='EMAIL_ID', max_length=100)),
                ('document', models.FileField(db_column='DOCUMENT', upload_to='images/')),
                ('password', models.CharField(db_column='P_PASSWORD', max_length=100)),
                ('other', models.CharField(db_column='OTHER', max_length=200)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'photographer',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(db_column='USERNAME', max_length=30, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FIRSTNAME', max_length=30)),
                ('lastname', models.CharField(db_column='LASTNAME', max_length=30)),
                ('mobile_no', models.IntegerField(db_column='MOBILE_NO')),
                ('email', models.EmailField(db_column='EMAIL_ID', max_length=100)),
                ('password', models.CharField(db_column='USER_PASSWORD', max_length=100)),
                ('experience', models.IntegerField(db_column='EXPERIENCE')),
                ('other', models.CharField(db_column='OTHER', max_length=200)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('id', models.IntegerField(null=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('get_email_field_name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('portfolio_id', models.AutoField(db_column='PORTFOLIO_ID', primary_key=True, serialize=False)),
                ('equipment', models.CharField(db_column='EQUIPMENT', max_length=100)),
                ('overview', models.CharField(db_column='OVERVIEW', max_length=100)),
                ('experience', models.IntegerField(db_column='EXPERIENCE')),
                ('starting_price', models.IntegerField(db_column='STARTING_PRICE')),
                ('skills', models.CharField(db_column='SKILLS', max_length=150)),
                ('language_known', models.CharField(db_column='LANGUAGE_KNOWN', max_length=50)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('n_id', models.AutoField(db_column='N_ID', primary_key=True, serialize=False)),
                ('to_photographer', models.CharField(db_column='TO_PHOTOGRAPHER', max_length=100)),
                ('to_user', models.CharField(db_column='TO_USER', max_length=100)),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
                ('username', models.ForeignKey(db_column='USERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('hire_id', models.AutoField(db_column='HIRE_ID', primary_key=True, serialize=False)),
                ('model_hire', models.CharField(db_column='MODEL_HIRE', max_length=3)),
                ('staff_hire', models.CharField(db_column='STAFF_HIRE', max_length=3)),
                ('comment', models.CharField(db_column='COMMENT', max_length=100)),
                ('experience_needed', models.IntegerField(db_column='EXPERIENCE_NEEDED')),
                ('skills_required', models.CharField(db_column='SKILLS_REQUIRED', max_length=50)),
                ('email_id', models.EmailField(db_column='EMAIL_ID', max_length=100)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
            ],
            options={
                'db_table': 'hire',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('category', models.CharField(db_column='CATEGORY', max_length=100)),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='BookingForm',
            fields=[
                ('booking_id', models.AutoField(db_column='BOOKING_ID', primary_key=True, serialize=False)),
                ('type_of_event', models.CharField(db_column='TYPE_OF_EVENT', max_length=20)),
                ('location_of_event', models.CharField(db_column='LOCATION_OF_EVENT', max_length=200)),
                ('start_date', models.DateTimeField(db_column='START_DATE')),
                ('budget', models.IntegerField(db_column='BUDGET')),
                ('additional_comments', models.CharField(db_column='ADDITIONAL_COMMENTS', max_length=100)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
                ('username', models.ForeignKey(db_column='USERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'booking form',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(db_column='IMAGE', max_length=200, upload_to='')),
                ('pusername', models.ForeignKey(db_column='PUSERNAME', on_delete=django.db.models.deletion.CASCADE, to='api.photographer')),
            ],
        ),
    ]