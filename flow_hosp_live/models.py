# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class CoreBranch(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    company = models.ForeignKey('CoreCompany')
    name = models.CharField(max_length=200)
    address_street_1 = models.CharField(max_length=200)
    address_street_2 = models.CharField(max_length=200)
    address_town = models.CharField(max_length=200)
    address_region = models.CharField(max_length=200)
    address_postcode = models.CharField(max_length=20)
    region = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    trainee_feed_identifier = models.CharField(max_length=200, blank=True, null=True)
    branch_notifications_to = models.CharField(max_length=200)
    branch_resources_introduction = models.TextField(blank=True, null=True)
    archived = models.IntegerField()
    top_level = models.CharField(max_length=200)
    extra_top_level = models.CharField(max_length=200)
    feed_identifier = models.CharField(max_length=200, blank=True, null=True)
    jurisdiction = models.ForeignKey('CoreJurisdiction', blank=True, null=True)
    branding = models.ForeignKey('CoreBranding', blank=True, null=True)
    pending = models.IntegerField()

    def __unicode__(self):
    	return 'Branch Name: {}, {}'.format(self.name,self.company) 

    class Meta:
        managed = True
        db_table = 'core_branch'
        unique_together = (('feed_identifier', 'company'),)

class CoreBranding(models.Model):
    company = models.ForeignKey('CoreCompany', blank=True, null=True)
    name = models.CharField(max_length=50)
    is_default = models.IntegerField()
    mm_welcome_text = models.TextField()
    mm_slug = models.CharField(max_length=50)
    noticeboard_label = models.CharField(max_length=255)
    careers_label = models.CharField(max_length=255)
    field_palette = models.TextField(db_column='_palette')  # Field renamed because it started with '_'.
    external_training_label = models.CharField(max_length=255)
    competence_label = models.CharField(max_length=255)
    appraisal_label = models.CharField(max_length=255)
    noticeboard_label_plural = models.CharField(max_length=255)
    careers_label_plural = models.CharField(max_length=255)
    external_training_label_plural = models.CharField(max_length=255)
    competence_label_plural = models.CharField(max_length=255)
    appraisal_label_plural = models.CharField(max_length=255)
    field_mobile_palette = models.TextField(db_column='_mobile_palette')  # Field renamed because it started with '_'.

    def __unicode__(self):
    	return '\nName: {}, {}'.format(self.name, self.company)

    class Meta:
        managed = True
        db_table = 'core_branding'

class CoreCareerpath(models.Model):
    company = models.ForeignKey('CoreCompany')
    name = models.CharField(max_length=200)
    information_sheet_description = models.TextField()
    information_sheet_name = models.CharField(max_length=200)

    def __unicode__(self):
    	return 'Name: {}, {}'.format(self.name, self.company)

    class Meta:
        managed = True
        db_table = 'core_careerpath'
        unique_together = (('company', 'name'),)

class CoreCompany(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=200)
    address_street_1 = models.CharField(max_length=200)
    address_street_2 = models.CharField(max_length=200)
    address_town = models.CharField(max_length=200)
    address_region = models.CharField(max_length=200)
    address_postcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    account_manager = models.ForeignKey(User, blank=True, null=True)
    number_of_employees = models.CharField(max_length=20)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    notes = models.TextField()
    is_simple_company = models.IntegerField()
    simple_company_trainee_alert_count = models.IntegerField()
    questionnaire_url = models.CharField(max_length=200)
    reseller = models.ForeignKey('ResellerReseller', blank=True, null=True)
    trainee_feed_type = models.CharField(max_length=200, blank=True, null=True)
    field_trainee_feed_settings = models.TextField(db_column='_trainee_feed_settings', blank=True, null=True)  # Field renamed because it started with '_'.
    simple_modules_enabled = models.IntegerField()
    simple_module_colour_scheme = models.ForeignKey('FlowCoreColourscheme', blank=True, null=True)
    simple_module_active_limit = models.IntegerField(blank=True, null=True)
    appraisals_enabled = models.IntegerField()
    career_paths_enabled = models.IntegerField()
    branch_resources_enabled = models.IntegerField()
    self_service_custom_downloads_enabled = models.IntegerField()
    self_service_custom_questions_enabled = models.IntegerField()
    maximum_custom_questions = models.IntegerField()
    branch_resources_introduction = models.TextField(blank=True, null=True)
    scorm_enabled = models.IntegerField()
    scorm_valid_days = models.IntegerField()
    open_pdfs = models.IntegerField()
    open_pdfs_pre_module = models.IntegerField()
    top_level_enabled = models.IntegerField()
    top_level_label = models.CharField(max_length=200)
    region_label = models.CharField(max_length=200)
    area_label = models.CharField(max_length=200)
    departments_enabled = models.IntegerField()
    extra_top_level_enabled = models.IntegerField()
    extra_top_level_label = models.CharField(max_length=200)
    hide_access_codes = models.IntegerField()
    field_gkone_export_settings = models.TextField(db_column='_gkone_export_settings', blank=True, null=True)  # Field renamed because it started with '_'.
    slug = models.CharField(unique=True, max_length=50)
    news_enabled = models.IntegerField()
    competences_enabled = models.IntegerField()
    dashboard_cache_enabled = models.IntegerField()
    dashboard_cache_hours = models.IntegerField()
    dashboard_cache_auto_update = models.IntegerField()
    dashboard_cache_last_auto_updated = models.DateTimeField(blank=True, null=True)
    external_training_enabled = models.IntegerField()
    mm_view_appraisal_introduction = models.TextField(blank=True, null=True)
    ms_appraisal_statement = models.TextField()
    birtreports_enabled = models.IntegerField()
    scorm_hosting_enabled = models.IntegerField()
    mb_modules_enabled = models.IntegerField()
    emailauth_enabled = models.IntegerField()
    commencement_days_enabled = models.IntegerField()
    default_commencement_days = models.IntegerField()
    override_platform_branding = models.IntegerField()
    override_platform_name = models.CharField(max_length=200, blank=True, null=True)
    override_platform_from_email = models.CharField(max_length=75, blank=True, null=True)
    override_platform_mm_link = models.CharField(max_length=200, blank=True, null=True)
    override_platform_ms_link = models.CharField(max_length=200, blank=True, null=True)
    department_label = models.CharField(max_length=200)
    branch_label = models.CharField(max_length=200)
    top_level_label_plural = models.CharField(max_length=200)
    extra_top_level_label_plural = models.CharField(max_length=200)
    region_label_plural = models.CharField(max_length=200)
    area_label_plural = models.CharField(max_length=200)
    department_label_plural = models.CharField(max_length=200)
    branch_label_plural = models.CharField(max_length=200)
    allow_bulk_trainee_upload = models.IntegerField()
    allow_trainee_external_identifiers = models.IntegerField()
    require_trainee_external_identifiers = models.IntegerField()
    trainee_import_unique_id = models.CharField(max_length=200)
    field_results_export_settings = models.TextField(db_column='_results_export_settings', blank=True, null=True)  # Field renamed because it started with '_'.
    is_pending = models.IntegerField()
    mobile_app_enabled = models.IntegerField()
    training_calendar_enabled = models.IntegerField()
    cloud2_enabled = models.IntegerField()

    def __unicode__(self):
    	return "Company Name: {}".format(self.name)

    class Meta:
        managed = True
        db_table = 'core_company'

class CoreDepartment(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(CoreCompany)

    def __unicode__(self):
    	return 'Department Name: {}, {}'.format(self.name, self.company)

    class Meta:
        managed = True
        db_table = 'core_department'

class CoreIndividual(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    user = models.OneToOneField(User, related_name="coreIndividualUser")
    address_street_1 = models.CharField(max_length=200)
    address_street_2 = models.CharField(max_length=200)
    address_town = models.CharField(max_length=200)
    address_region = models.CharField(max_length=200)
    address_postcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    account_manager = models.ForeignKey(User, blank=True, null=True, related_name="coreIndividualAccountManager")
    notes = models.TextField()
    identification_code = models.CharField(unique=True, max_length=20, blank=True, null=True, )
    ila_token = models.CharField(max_length=255)
    ila_account_holder = models.IntegerField()
    copied_from = models.ForeignKey('CoreTrainee', blank=True, null=True)

    def __unicode__(self):
    	return 'User: {}, Address: {}'.format(self.user, self.address_street_1)

    class Meta:
        managed = True
        db_table = 'core_individual'

class CoreJurisdiction(models.Model):
    company = models.ForeignKey(CoreCompany)
    name = models.CharField(max_length=200)

    def __unicode__(self):
    	return 'Jurisdiction: {}, {}'.format(self.name, self.company)

    class Meta:
        managed = True
        db_table = 'core_jurisdiction'
        unique_together = (('company', 'name'),)


class CoreTrainee(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    branch = models.ForeignKey(CoreBranch)
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=75)
    mobile_number = models.CharField(max_length=20)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField()
    orderable_name = models.CharField(max_length=255)
    identification_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=50)
    training_notes = models.TextField()
    taken_questionnaire = models.IntegerField()
    ila_token = models.CharField(max_length=255)
    ila_account_holder = models.IntegerField()
    field_copied_from_inidividual = models.ForeignKey(CoreIndividual, db_column='_copied_from_inidividual_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_copied_from_trainee = models.ForeignKey('self', db_column='_copied_from_trainee_id', blank=True, null=True)  # Field renamed because it started with '_'.
    marked_as_leaver = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    training_performance = models.TextField()
    career_path = models.ForeignKey(CoreCareerpath, blank=True, null=True)
    department = models.ForeignKey(CoreDepartment, blank=True, null=True)

    def __unicode__(self):
    	return 'Trainee Name: {} {}, {}'.format(self.forename, 
    											self.surname,
    											self.branch)

    class Meta:
        managed = True
        db_table = 'core_trainee'

class FlowCoreColourscheme(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='flowCoreColourschemeCreated')
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(User, blank=True, null=True, related_name='flowCoreColourschemeRemoved')
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=100)
    highlight_text_colour = models.CharField(max_length=6)
    base_text_colour = models.CharField(max_length=6)
    footer_text_colour = models.CharField(max_length=6)
    button_text_colour = models.CharField(max_length=6)
    textbox_border = models.CharField(max_length=6)
    textbox_background_colour_a = models.CharField(max_length=6)
    textbox_background_colour_b = models.CharField(max_length=6)
    html_background_colour = models.CharField(max_length=6)
    html_text_colour = models.CharField(max_length=6)
    popup_heading_left = models.CharField(max_length=6)
    popup_heading_right = models.CharField(max_length=6)

    def __unicode__(self):
    	return 'Colour Scheme: {}, Created BY: {}'.format(self.name,self.created_by)

    class Meta:
        managed = True
        db_table = 'flow_core_colourscheme'



class ResellerReseller(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=255)
    reseller_type = models.CharField(max_length=50)

    def __unicode__(self):
    	return 'Reseller Name: {}, Patner: {}'.format(self.name, self.parent)

    class Meta:
        managed = True
        db_table = 'reseller_reseller'