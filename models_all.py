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


class AdminAuditlog(models.Model):
    user_id = models.IntegerField()
    user_login = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_auditlog'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthMessage(models.Model):
    user = models.ForeignKey('AuthUser')
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_message'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BirtReportsReport(models.Model):
    reportname = models.CharField(max_length=255)
    description = models.TextField()
    reporturl = models.CharField(max_length=255)
    available_asexcel = models.IntegerField()
    available_ashtml = models.IntegerField()
    available_aspdf = models.IntegerField()
    category = models.CharField(max_length=20)
    report_permission = models.CharField(max_length=255)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'birt_reports_report'


class BirtReportsReportparam(models.Model):
    report = models.ForeignKey(BirtReportsReport)
    type = models.CharField(max_length=20)
    ismulti = models.IntegerField(db_column='isMulti')  # Field name made lowercase.
    isrequired = models.IntegerField(db_column='isRequired')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'birt_reports_reportparam'


class BookingsLocation(models.Model):
    company = models.ForeignKey('CoreCompany')
    name = models.CharField(unique=True, max_length=150)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150)
    post_code = models.CharField(max_length=20)
    max_capacity = models.IntegerField()
    created_by = models.ForeignKey(AuthUser)
    modified_by = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'bookings_location'
        unique_together = (('company', 'name'),)


class BookingsTrainingsession(models.Model):
    external_training = models.ForeignKey('CoreExternaltraining')
    location = models.ForeignKey(BookingsLocation)
    max_attendees = models.IntegerField()
    min_attendees = models.IntegerField()
    available_places = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser)
    trainer = models.ForeignKey(AuthUser, blank=True, null=True)
    modified_by = models.ForeignKey(AuthUser)
    training_type = models.CharField(max_length=50)
    cancelled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookings_trainingsession'


class BookingsTrainingsessionBranches(models.Model):
    trainingsession = models.ForeignKey(BookingsTrainingsession)
    branch = models.ForeignKey('CoreBranch')

    class Meta:
        managed = False
        db_table = 'bookings_trainingsession_branches'
        unique_together = (('trainingsession', 'branch'),)


class BookingsTrainingsessionbooking(models.Model):
    training_session = models.ForeignKey(BookingsTrainingsession)
    trainee = models.ForeignKey('CoreTrainee')
    has_attended = models.IntegerField()
    attendance = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bookings_trainingsessionbooking'


class ContentChunk(models.Model):
    system_name = models.CharField(unique=True, max_length=64)
    description = models.CharField(max_length=255)
    content = models.ForeignKey('ContentContent')

    class Meta:
        managed = False
        db_table = 'content_chunk'


class ContentContent(models.Model):
    copy = models.TextField()

    class Meta:
        managed = False
        db_table = 'content_content'


class ContentImage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_path = models.CharField(max_length=200)
    sort_order = models.IntegerField()
    display = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType')
    object_id = models.IntegerField(blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'content_image'


class ContentPage(models.Model):
    node = models.ForeignKey('ContentSitemapnode', primary_key=True)
    content = models.ForeignKey(ContentContent)
    template = models.CharField(max_length=255)
    allow_comments = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_page'


class ContentPlaceholder(models.Model):
    node = models.ForeignKey('ContentSitemapnode', primary_key=True)

    class Meta:
        managed = False
        db_table = 'content_placeholder'


class ContentSitemapnode(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    field_parent = models.ForeignKey('self', db_column='_parent_id', blank=True, null=True)  # Field renamed because it started with '_'.
    slug = models.CharField(max_length=50, blank=True, null=True)
    field_index = models.IntegerField(db_column='_index')  # Field renamed because it started with '_'.
    hidden = models.IntegerField()
    hidden_from_sitemap = models.IntegerField()
    disabled = models.IntegerField()
    anchored = models.IntegerField()
    internal_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    created_by_id = models.IntegerField(blank=True, null=True)
    last_modified_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_sitemapnode'
        unique_together = (('field_parent', 'slug'),)


class ContentSitemapnodeaccess(models.Model):
    node = models.ForeignKey(ContentSitemapnode)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_sitemapnodeaccess'
        unique_together = (('node', 'group_id'),)


class CoreAccount(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    field_company = models.ForeignKey('CoreCompany', db_column='_company_id', unique=True, blank=True, null=True)  # Field renamed because it started with '_'.
    field_individual = models.ForeignKey('CoreIndividual', db_column='_individual_id', unique=True, blank=True, null=True)  # Field renamed because it started with '_'.
    active = models.IntegerField()
    name = models.CharField(max_length=200)
    address_street_1 = models.CharField(max_length=200)
    address_street_2 = models.CharField(max_length=200)
    address_town = models.CharField(max_length=200)
    address_region = models.CharField(max_length=200)
    address_postcode = models.CharField(max_length=20)
    orderable_name = models.CharField(max_length=255)
    instant_logout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_account'


class CoreAppraisal(models.Model):
    trainee = models.ForeignKey('CoreTrainee')
    appraisal_date = models.DateField()
    appraiser = models.CharField(max_length=200, blank=True, null=True)
    additional_info = models.CharField(max_length=255)
    form_type = models.CharField(max_length=50)
    completed_date = models.DateField(blank=True, null=True)
    appraiser_notes = models.TextField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    appraiser_user = models.ForeignKey(AuthUser, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    rating_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_appraisal'


class CoreAppraisalfielddefinition(models.Model):
    label = models.CharField(max_length=200)
    sort_order = models.IntegerField()
    appraisal_form_definition = models.ForeignKey('CoreAppraisalformdefinition', blank=True, null=True)
    enabled = models.IntegerField()
    default_text = models.TextField()
    trainee_default_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_appraisalfielddefinition'


class CoreAppraisalformdefinition(models.Model):
    company = models.ForeignKey('CoreCompany')
    form_type = models.CharField(max_length=50)
    enabled = models.IntegerField()
    rating_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_appraisalformdefinition'
        unique_together = (('form_type', 'company'),)


class CoreAppraisalvalue(models.Model):
    label = models.CharField(max_length=200)
    appraisal = models.ForeignKey(CoreAppraisal)
    value = models.TextField()
    appraisal_field_definition = models.ForeignKey(CoreAppraisalfielddefinition)

    class Meta:
        managed = False
        db_table = 'core_appraisalvalue'


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

    class Meta:
        managed = False
        db_table = 'core_branch'
        unique_together = (('feed_identifier', 'company'),)


class CoreBranchcreditorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    branch = models.ForeignKey(CoreBranch)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'core_branchcreditorder'


class CoreBranchdefaultduedate(models.Model):
    module = models.ForeignKey('FlowCoreModule')
    days = models.IntegerField()
    branch = models.ForeignKey(CoreBranch)

    class Meta:
        managed = False
        db_table = 'core_branchdefaultduedate'


class CoreBranchmoduledownload(models.Model):
    module = models.ForeignKey('FlowCoreModule')
    module_version_filename = models.CharField(max_length=200)
    availability = models.CharField(max_length=9)
    filename = models.CharField(max_length=200)
    mode = models.CharField(max_length=7)
    branch = models.ForeignKey(CoreBranch)

    class Meta:
        managed = False
        db_table = 'core_branchmoduledownload'


class CoreBranchquestion(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    last_modified = models.DateTimeField()
    module_version = models.ForeignKey('FlowCoreModuleversion')
    text = models.TextField()
    type = models.CharField(max_length=20)
    field_choices = models.TextField(db_column='_choices')  # Field renamed because it started with '_'.
    branch = models.ForeignKey(CoreBranch)
    associated_slide_uuid = models.CharField(max_length=36, blank=True, null=True)
    associated_html5_slide_uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_branchquestion'


class CoreBranchresource(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    branch = models.ForeignKey(CoreBranch)
    filename = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    all_job_titles = models.IntegerField()
    must_read_within = models.IntegerField()
    expires = models.DateTimeField(blank=True, null=True)
    multiple_branches = models.IntegerField()
    archived = models.IntegerField()
    alerts_to = models.CharField(max_length=75, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey('CoreBranchresourcecategory', blank=True, null=True)
    send_alerts = models.IntegerField()
    notify_trainees = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_branchresource'
        unique_together = (('branch', 'filename'),)


class CoreBranchresourceaccessrecord(models.Model):
    created = models.DateTimeField()
    trainee = models.ForeignKey('CoreTrainee')
    branch_resource = models.ForeignKey(CoreBranchresource)
    read = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField()
    manager_alert_date = models.DateField()
    reminder_date = models.DateField()
    notified = models.DateTimeField(blank=True, null=True)
    notify_trainee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_branchresourceaccessrecord'
        unique_together = (('trainee', 'branch_resource'),)


class CoreBranchresourcecategory(models.Model):
    created = models.DateTimeField()
    name = models.CharField(max_length=244)
    order = models.IntegerField()
    company = models.ForeignKey('CoreCompany')

    class Meta:
        managed = False
        db_table = 'core_branchresourcecategory'


class CoreBranchresourcejobtitle(models.Model):
    branch_resource = models.ForeignKey(CoreBranchresource)
    job_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'core_branchresourcejobtitle'


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

    class Meta:
        managed = False
        db_table = 'core_branding'


class CoreCareerpath(models.Model):
    company = models.ForeignKey('CoreCompany')
    name = models.CharField(max_length=200)
    information_sheet_description = models.TextField()
    information_sheet_name = models.CharField(max_length=200)

    class Meta:
        managed = False
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
    account_manager = models.ForeignKey(AuthUser, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'core_company'


class CoreCompanyCustomModules(models.Model):
    company = models.ForeignKey(CoreCompany)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_company_custom_modules'
        unique_together = (('company', 'module'),)


class CoreCompanyGkoneModules(models.Model):
    company = models.ForeignKey(CoreCompany)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_company_gkone_modules'
        unique_together = (('company', 'module'),)


class CoreCompanySimpleModuleColourSchemes(models.Model):
    company = models.ForeignKey(CoreCompany)
    colourscheme = models.ForeignKey('FlowCoreColourscheme')

    class Meta:
        managed = False
        db_table = 'core_company_simple_module_colour_schemes'
        unique_together = (('company', 'colourscheme'),)


class CoreCompanySimpleModules(models.Model):
    company = models.ForeignKey(CoreCompany)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_company_simple_modules'
        unique_together = (('company', 'module'),)


class CoreCompanyappraisalfielddefinition(models.Model):
    company = models.ForeignKey(CoreCompany)
    enabled = models.IntegerField()
    label = models.CharField(max_length=200)
    sort_order = models.IntegerField()
    rating_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_companyappraisalfielddefinition'


class CoreCompanyappraisalvalue(models.Model):
    appraisal_field_definition = models.ForeignKey(CoreCompanyappraisalfielddefinition)
    appraisal = models.ForeignKey(CoreAppraisal)
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'core_companyappraisalvalue'


class CoreCompanyemailcontent(models.Model):
    company = models.ForeignKey(CoreCompany)
    training_instructions_upper = models.TextField()
    training_instructions_lower = models.TextField()
    welcome_email_upper = models.TextField()
    welcome_email_lower = models.TextField()
    print_training_instructions_upper = models.TextField()
    print_training_instructions_lower = models.TextField()
    new_branch_resource_notification_upper = models.TextField()
    new_branch_resource_notification_lower = models.TextField()
    new_branch_resource_reminder_upper = models.TextField()
    new_branch_resource_reminder_lower = models.TextField()
    branch_resource_overdue_alert_upper = models.TextField()
    branch_resource_overdue_alert_lower = models.TextField()
    trainee_appraisal_reminder_upper = models.TextField()
    trainee_appraisal_reminder_lower = models.TextField()
    trainee_appraisal_notification_upper = models.TextField()
    trainee_appraisal_notification_lower = models.TextField()
    email_social_media_footer = models.TextField()
    email_common_footer = models.TextField()
    outstanding_external_training_notification_upper = models.TextField()
    outstanding_external_training_notification_lower = models.TextField()
    outstanding_external_training_reminder_upper = models.TextField()
    outstanding_external_training_reminder_lower = models.TextField()
    email_due_date_reminder_top = models.TextField()
    email_due_date_reminder_bottom = models.TextField()
    email_due_date_overdue_top = models.TextField()
    email_due_date_overdue_bottom = models.TextField()
    second_exam_failed_warning_upper = models.TextField()
    second_exam_failed_warning_lower = models.TextField()
    existing_trainee_instructions_upper = models.TextField()
    existing_trainee_instructions_lower = models.TextField()
    changed_trainee_allocations_upper = models.TextField()
    changed_trainee_allocations_lower = models.TextField()
    new_news_notification_upper = models.TextField()
    new_news_notification_lower = models.TextField()
    launch_email_upper = models.TextField()
    launch_email_lower = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_companyemailcontent'


class CoreCompanymoduledownload(models.Model):
    module = models.ForeignKey('FlowCoreModule')
    module_version_filename = models.CharField(max_length=200)
    availability = models.CharField(max_length=9)
    filename = models.CharField(max_length=200)
    mode = models.CharField(max_length=7)
    company = models.ForeignKey(CoreCompany)

    class Meta:
        managed = False
        db_table = 'core_companymoduledownload'


class CoreCompanyquestion(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    last_modified = models.DateTimeField()
    module_version = models.ForeignKey('FlowCoreModuleversion')
    text = models.TextField()
    type = models.CharField(max_length=20)
    field_choices = models.TextField(db_column='_choices')  # Field renamed because it started with '_'.
    company = models.ForeignKey(CoreCompany)
    associated_slide_uuid = models.CharField(max_length=36, blank=True, null=True)
    associated_html5_slide_uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_companyquestion'


class CoreCourse(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    exam_blocker_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_course'


class CoreDefaultduedate(models.Model):
    company = models.ForeignKey(CoreCompany)
    module = models.ForeignKey('FlowCoreModule')
    days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_defaultduedate'
        unique_together = (('company', 'module'),)


class CoreDefaultpricing(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    account_type = models.CharField(max_length=20)
    number_of_credits = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    franchisor = models.ForeignKey('CoreFranchisor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_defaultpricing'
        unique_together = (('franchisor', 'price', 'number_of_credits', 'account_type'),)


class CoreDepartment(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(CoreCompany)

    class Meta:
        managed = False
        db_table = 'core_department'


class CoreExternaltraining(models.Model):
    company = models.ForeignKey(CoreCompany)
    name = models.CharField(max_length=200)
    description = models.TextField()
    filename = models.CharField(max_length=255)
    provider = models.CharField(max_length=200, blank=True, null=True)
    training_type = models.CharField(max_length=200, blank=True, null=True)
    training_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_externaltraining'
        unique_together = (('company', 'name'),)


class CoreFeedidentifier(models.Model):
    company = models.ForeignKey(CoreCompany)
    trainee = models.ForeignKey('CoreTrainee', blank=True, null=True)
    identifier = models.CharField(max_length=200)
    primary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_feedidentifier'
        unique_together = (('company', 'identifier'),)


class CoreFranchisee(models.Model):
    franchisor = models.ForeignKey('CoreFranchisor')
    account_code = models.CharField(max_length=200)
    postcode = models.CharField(max_length=9)
    company = models.ForeignKey(CoreCompany, unique=True, blank=True, null=True)
    company_name = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=200, blank=True, null=True)
    street_1 = models.CharField(max_length=200)
    street_2 = models.CharField(max_length=200, blank=True, null=True)
    town = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    division = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_franchisee'
        unique_together = (('franchisor', 'account_code', 'postcode'),)


class CoreFranchisor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    introduction = models.TextField(blank=True, null=True)
    enabled = models.IntegerField()
    account_code_label = models.CharField(max_length=255)
    verification_method = models.CharField(max_length=17)
    verification_code_label = models.CharField(max_length=255, blank=True, null=True)
    sso_method = models.CharField(max_length=11)
    field_sso_config = models.TextField(db_column='_sso_config')  # Field renamed because it started with '_'.
    ftp_import_enabled = models.IntegerField()
    field_ftp_import_settings = models.TextField(db_column='_ftp_import_settings')  # Field renamed because it started with '_'.
    ftp_import_log = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_franchisor'


class CoreFranchisorCustomModules(models.Model):
    franchisor = models.ForeignKey(CoreFranchisor)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_franchisor_custom_modules'
        unique_together = (('franchisor', 'module'),)


class CoreGoogleanalyticstransaction(models.Model):
    user = models.ForeignKey(AuthUser)
    account = models.CharField(max_length=20)
    affiliation = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_googleanalyticstransaction'


class CoreGoogleanalyticstransactionitem(models.Model):
    transaction = models.ForeignKey(CoreGoogleanalyticstransaction)
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_googleanalyticstransactionitem'


class CoreHospitalityallocation(models.Model):
    allocation = models.ForeignKey('FlowTrainingAllocation', primary_key=True)
    place = models.ForeignKey('CorePlace')
    latest_for_place = models.IntegerField()
    latest_for_learner = models.IntegerField()
    credits = models.IntegerField()
    prerequisite_allocation = models.ForeignKey('FlowTrainingAllocation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_hospitalityallocation'


class CoreHospitalityflashpersistentstorage(models.Model):
    storage = models.ForeignKey('FlowTrainingFlashpersistentstorage')
    place = models.ForeignKey('CorePlace')
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_hospitalityflashpersistentstorage'
        unique_together = (('place', 'module'),)


class CoreHospitalitymodule(models.Model):
    module = models.ForeignKey('FlowCoreModule', primary_key=True)
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_hospitalitymodule'


class CoreHospitalitysitting(models.Model):
    sitting = models.ForeignKey('FlowTrainingSitting', primary_key=True)
    reviewed_on = models.DateTimeField(blank=True, null=True)
    reviewed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    exported_to_gkone = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_hospitalitysitting'


class CoreIndividual(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    user = models.ForeignKey(AuthUser, unique=True)
    address_street_1 = models.CharField(max_length=200)
    address_street_2 = models.CharField(max_length=200)
    address_town = models.CharField(max_length=200)
    address_region = models.CharField(max_length=200)
    address_postcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    account_manager = models.ForeignKey(AuthUser, blank=True, null=True)
    notes = models.TextField()
    identification_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ila_token = models.CharField(max_length=255)
    ila_account_holder = models.IntegerField()
    copied_from = models.ForeignKey('CoreTrainee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_individual'


class CoreIndividualComputers(models.Model):
    individual = models.ForeignKey(CoreIndividual)
    computer = models.ForeignKey('FlowTrainingComputer')

    class Meta:
        managed = False
        db_table = 'core_individual_computers'
        unique_together = (('individual', 'computer'),)


class CoreIndividualcourseorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    individual = models.ForeignKey(CoreIndividual)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'core_individualcourseorder'


class CoreIndividualcourseorderModules(models.Model):
    individualcourseorder = models.ForeignKey(CoreIndividualcourseorder)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_individualcourseorder_modules'
        unique_together = (('individualcourseorder', 'module'),)


class CoreIndividualreactivationorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    individual = models.ForeignKey(CoreIndividual)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)
    place = models.ForeignKey('CorePlace')
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_individualreactivationorder'


class CoreJobtitle(models.Model):
    company = models.ForeignKey(CoreCompany)
    name = models.CharField(max_length=200)
    jurisdiction = models.ForeignKey('CoreJurisdiction', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_jobtitle'
        unique_together = (('company', 'jurisdiction', 'name'),)


class CoreJobtitleappraisal(models.Model):
    job_title = models.ForeignKey(CoreJobtitle)
    appraisal_form_definition = models.ForeignKey(CoreAppraisalformdefinition)
    due_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_jobtitleappraisal'


class CoreJobtitlecareerpath(models.Model):
    job_title = models.ForeignKey(CoreJobtitle)
    career_path = models.ForeignKey(CoreCareerpath)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_jobtitlecareerpath'


class CoreJobtitleexternaltraining(models.Model):
    job_title = models.ForeignKey(CoreJobtitle)
    external_training = models.ForeignKey(CoreExternaltraining)
    new_trainees_due_in = models.IntegerField(blank=True, null=True)
    existing_trainees_due_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_jobtitleexternaltraining'


class CoreJobtitlemodule(models.Model):
    job_title = models.ForeignKey(CoreJobtitle)
    module = models.ForeignKey('FlowCoreModule')
    prerequisite = models.ForeignKey('self', blank=True, null=True)
    commence_in = models.IntegerField(blank=True, null=True)
    new_trainees_due_in = models.IntegerField(blank=True, null=True)
    existing_trainees_due_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_jobtitlemodule'


class CoreJobtitlestandardcompetence(models.Model):
    job_title = models.ForeignKey(CoreJobtitle)
    standard_competence = models.ForeignKey('CoreStandardcompetence')
    competence_list_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_jobtitlestandardcompetence'


class CoreJurisdiction(models.Model):
    company = models.ForeignKey(CoreCompany)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_jurisdiction'
        unique_together = (('company', 'name'),)


class CoreLedgerentry(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    field_branch = models.ForeignKey(CoreBranch, db_column='_branch_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_individual = models.ForeignKey(CoreIndividual, db_column='_individual_id', blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.CharField(max_length=200)
    account_manager = models.ForeignKey(AuthUser, blank=True, null=True)
    reason_code = models.ForeignKey('CoreReasoncode', blank=True, null=True)
    debit = models.IntegerField()
    credit = models.IntegerField()
    credits_balance = models.IntegerField()
    cause_content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    cause_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_ledgerentry'


class CoreNoteviewmonitor(models.Model):
    admin_user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'core_noteviewmonitor'


class CoreNoteviewmonitorCompany(models.Model):
    noteviewmonitor = models.ForeignKey(CoreNoteviewmonitor)
    company = models.ForeignKey(CoreCompany)

    class Meta:
        managed = False
        db_table = 'core_noteviewmonitor_company'
        unique_together = (('noteviewmonitor', 'company'),)


class CoreNoteviewmonitorIndividual(models.Model):
    noteviewmonitor = models.ForeignKey(CoreNoteviewmonitor)
    individual = models.ForeignKey(CoreIndividual)

    class Meta:
        managed = False
        db_table = 'core_noteviewmonitor_individual'
        unique_together = (('noteviewmonitor', 'individual'),)


class CorePlace(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    field_trainee = models.ForeignKey('CoreTrainee', db_column='_trainee_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_individual = models.ForeignKey(CoreIndividual, db_column='_individual_id', blank=True, null=True)  # Field renamed because it started with '_'.
    course = models.ForeignKey(CoreCourse)
    legacy_activation_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    email_sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_place'


class CoreReasoncode(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    name = models.CharField(max_length=200)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_reasoncode'


class CoreRegistrationorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=36)
    post_data = models.TextField(blank=True, null=True)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    account = models.ForeignKey(CoreAccount, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_registrationorder'


class CoreScormsco(models.Model):
    uuid = models.CharField(unique=True, max_length=36)
    company = models.ForeignKey(CoreCompany)
    module = models.ForeignKey('FlowCoreModule')
    filename_secret = models.CharField(max_length=30)
    file_contents_secret = models.CharField(max_length=30)
    enabled = models.IntegerField()
    expires = models.DateField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    package_type = models.CharField(max_length=6)
    student_id_label = models.CharField(max_length=200)
    pending = models.IntegerField()
    storage_filename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'core_scormsco'


class CoreSimplecompanycourseorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    company = models.ForeignKey(CoreCompany)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'core_simplecompanycourseorder'


class CoreSimplecompanycourseorderModules(models.Model):
    simplecompanycourseorder = models.ForeignKey(CoreSimplecompanycourseorder)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_simplecompanycourseorder_modules'
        unique_together = (('simplecompanycourseorder', 'module'),)


class CoreSimplecompanycourseorderTrainees(models.Model):
    simplecompanycourseorder = models.ForeignKey(CoreSimplecompanycourseorder)
    trainee = models.ForeignKey('CoreTrainee')

    class Meta:
        managed = False
        db_table = 'core_simplecompanycourseorder_trainees'
        unique_together = (('simplecompanycourseorder', 'trainee'),)


class CoreSimplecompanyextracreditsorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    company = models.ForeignKey(CoreCompany)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'core_simplecompanyextracreditsorder'


class CoreSimplecompanyreactivationorder(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    company = models.ForeignKey(CoreCompany)
    number_of_credits = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AuthUser)
    place = models.ForeignKey(CorePlace)
    module = models.ForeignKey('FlowCoreModule')

    class Meta:
        managed = False
        db_table = 'core_simplecompanyreactivationorder'


class CoreSimplemodulepermission(models.Model):
    module_id = models.IntegerField(primary_key=True)
    mode = models.CharField(max_length=11)
    region = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    editors = models.CharField(max_length=11)
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_simplemodulepermission'


class CoreSimplemodulepermissionBranches(models.Model):
    simplemodulepermission = models.ForeignKey(CoreSimplemodulepermission)
    branch = models.ForeignKey(CoreBranch)

    class Meta:
        managed = False
        db_table = 'core_simplemodulepermission_branches'
        unique_together = (('simplemodulepermission', 'branch'),)


class CoreStandardcompetence(models.Model):
    company = models.ForeignKey(CoreCompany)
    competence = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'core_standardcompetence'
        unique_together = (('company', 'competence'),)


class CoreStandardcompetencelist(models.Model):
    company = models.ForeignKey(CoreCompany)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'core_standardcompetencelist'
        unique_together = (('company', 'name'),)


class CoreStandardcompetencelisting(models.Model):
    standard_competence = models.ForeignKey(CoreStandardcompetence)
    standard_competence_list = models.ForeignKey(CoreStandardcompetencelist)

    class Meta:
        managed = False
        db_table = 'core_standardcompetencelisting'


class CoreSystemmessage(models.Model):
    site = models.CharField(max_length=2)
    message = models.TextField()
    active = models.IntegerField()
    uuid = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'core_systemmessage'


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

    class Meta:
        managed = False
        db_table = 'core_trainee'


class CoreTraineeComputers(models.Model):
    trainee = models.ForeignKey(CoreTrainee)
    computer = models.ForeignKey('FlowTrainingComputer')

    class Meta:
        managed = False
        db_table = 'core_trainee_computers'
        unique_together = (('trainee', 'computer'),)


class CoreTraineeappraisalvaluenotes(models.Model):
    appraisal = models.ForeignKey(CoreAppraisal)
    appraisal_value = models.ForeignKey(CoreAppraisalvalue)
    trainee_notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_traineeappraisalvaluenotes'
        unique_together = (('appraisal_value', 'appraisal'),)


class CoreTraineecompetence(models.Model):
    trainee = models.ForeignKey(CoreTrainee)
    competence = models.CharField(max_length=255)
    supporting_document_filename = models.CharField(max_length=255)
    achieved_date = models.DateField(blank=True, null=True)
    competence_list_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_traineecompetence'


class CoreTraineeduplicate(models.Model):
    identifier = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField()
    department = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_traineeduplicate'


class CoreTraineeduplicateTrainees(models.Model):
    traineeduplicate = models.ForeignKey(CoreTraineeduplicate)
    trainee = models.ForeignKey(CoreTrainee)

    class Meta:
        managed = False
        db_table = 'core_traineeduplicate_trainees'
        unique_together = (('traineeduplicate', 'trainee'),)


class CoreTraineeexternaltraining(models.Model):
    trainee = models.ForeignKey(CoreTrainee)
    external_training = models.ForeignKey(CoreExternaltraining)
    completed_on = models.DateField(blank=True, null=True)
    notes = models.TextField()
    completed = models.CharField(max_length=3)
    issued_on = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    course = models.ForeignKey(CoreCourse, blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_traineeexternaltraining'


class CoreTraineelibrarybranchresource(models.Model):
    trainee = models.ForeignKey(CoreTrainee)
    branch_resource = models.ForeignKey(CoreBranchresource)

    class Meta:
        managed = False
        db_table = 'core_traineelibrarybranchresource'
        unique_together = (('branch_resource', 'trainee'),)


class CoreUndertaking(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    due_date = models.DateField(blank=True, null=True)
    trainee = models.ForeignKey(CoreTrainee)
    module = models.ForeignKey('FlowCoreModule')
    commencement_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_undertaking'
        unique_together = (('trainee', 'module'),)


class CoreUserprofile(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    user = models.ForeignKey(AuthUser, unique=True)
    user_type = models.CharField(max_length=20)
    company = models.ForeignKey(CoreCompany, blank=True, null=True)
    notification_frequency = models.CharField(max_length=20)
    reseller = models.ForeignKey('ResellerReseller', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_userprofile'


class CoreUserprofileFranchisors(models.Model):
    userprofile = models.ForeignKey(CoreUserprofile)
    franchisor = models.ForeignKey(CoreFranchisor)

    class Meta:
        managed = False
        db_table = 'core_userprofile_franchisors'
        unique_together = (('userprofile', 'franchisor'),)


class CoreVatrate(models.Model):
    percent = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'core_vatrate'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class FeedsFeedimportqueue(models.Model):
    created = models.DateTimeField()
    company = models.ForeignKey(CoreCompany, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feeds_feedimportqueue'


class FlowAdminPermission(models.Model):
    user = models.ForeignKey(AuthUser)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType, blank=True, null=True)
    test_type = models.CharField(max_length=50, blank=True, null=True)
    test_data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_admin_permission'


class FlowCoreColourscheme(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'flow_core_colourscheme'


class FlowCoreModule(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    module_type = models.CharField(max_length=20)
    demo_slug = models.CharField(unique=True, max_length=50, blank=True, null=True)
    core_sort_order = models.IntegerField(blank=True, null=True)
    approved_version = models.ForeignKey('FlowCoreModuleversion', blank=True, null=True)
    pending_version = models.ForeignKey('FlowCoreModuleversion', blank=True, null=True)
    internal_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.IntegerField()
    is_archived = models.IntegerField()
    private_storage_prefix = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_core_module'


class FlowCoreModuleversion(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    last_modified = models.DateTimeField()
    module = models.ForeignKey(FlowCoreModule)
    display_name = models.CharField(max_length=100)
    colour_scheme = models.ForeignKey(FlowCoreColourscheme)
    minimum_time = models.IntegerField(blank=True, null=True)
    minimum_time_message = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    approved = models.DateTimeField(blank=True, null=True)
    approved_by = models.ForeignKey(AuthUser, blank=True, null=True)
    number_of_questions = models.IntegerField(blank=True, null=True)
    pass_mark = models.IntegerField(blank=True, null=True)
    simple_introduction = models.IntegerField()
    has_certificate = models.IntegerField()
    start_message = models.CharField(max_length=120, blank=True, null=True)
    mid_message = models.CharField(max_length=120, blank=True, null=True)
    end_message = models.CharField(max_length=120, blank=True, null=True)
    share_url = models.CharField(max_length=100, blank=True, null=True)
    format = models.CharField(max_length=5)
    translation = models.ForeignKey('FlowCoreTranslation', blank=True, null=True)
    mb_created_by = models.CharField(max_length=75, blank=True, null=True)
    mb_updated_by = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_core_moduleversion'


class FlowCoreQuestion(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    last_modified = models.DateTimeField()
    module_version = models.ForeignKey(FlowCoreModuleversion)
    text = models.TextField()
    type = models.CharField(max_length=20)
    field_choices = models.TextField(db_column='_choices')  # Field renamed because it started with '_'.
    associated_slide_uuid = models.CharField(max_length=36, blank=True, null=True)
    associated_html5_slide_uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_core_question'


class FlowCoreSyncModuleversiondownload(models.Model):
    module_version = models.ForeignKey(FlowCoreModuleversion)
    filename = models.CharField(max_length=200)
    availability = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    sort_order = models.IntegerField()
    override_allowed = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'flow_core_sync_moduleversiondownload'


class FlowCoreTranslation(models.Model):
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, blank=True, null=True)
    removed = models.DateTimeField(blank=True, null=True)
    removed_by = models.ForeignKey(AuthUser, blank=True, null=True)
    last_modified = models.DateTimeField()
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'flow_core_translation'


class FlowFilesS3Storagelookup(models.Model):
    key = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'flow_files_s3storagelookup'


class FlowTrainingAllocation(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    module = models.ForeignKey(FlowCoreModule)

    class Meta:
        managed = False
        db_table = 'flow_training_allocation'


class FlowTrainingComputer(models.Model):
    identifier = models.CharField(max_length=100)
    created = models.DateTimeField()
    last_used = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flow_training_computer'


class FlowTrainingDownloadaccessrecord(models.Model):
    allocation = models.ForeignKey(FlowTrainingAllocation)
    availability = models.CharField(max_length=9)
    filename = models.CharField(max_length=200)
    last_accessed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flow_training_downloadaccessrecord'
        unique_together = (('allocation', 'availability', 'filename'),)


class FlowTrainingFlashpersistentstorage(models.Model):
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'flow_training_flashpersistentstorage'


class FlowTrainingSitting(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    started = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    allocation = models.ForeignKey(FlowTrainingAllocation)
    latest_for_allocation = models.IntegerField()
    status = models.CharField(max_length=20)
    total_time = models.IntegerField(blank=True, null=True)
    exam_time = models.IntegerField(blank=True, null=True)
    exam_result = models.CharField(max_length=4, blank=True, null=True)
    exam_marks = models.IntegerField(blank=True, null=True)
    exam_out_of = models.IntegerField(blank=True, null=True)
    exam_version = models.CharField(max_length=10, blank=True, null=True)
    exam_details_received = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_training_sitting'


class FraserTemp(models.Model):
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    field_trainee_id = models.IntegerField(db_column='_trainee_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_individual_id = models.IntegerField(db_column='_individual_id', blank=True, null=True)  # Field renamed because it started with '_'.
    course_id = models.IntegerField()
    legacy_activation_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    email_sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fraser_temp'


class FraserTempHa(models.Model):
    allocation_id = models.IntegerField(primary_key=True)
    place_id = models.IntegerField()
    latest_for_place = models.IntegerField()
    latest_for_learner = models.IntegerField()
    credits = models.IntegerField()
    prerequisite_allocation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fraser_temp_ha'


class HelpFrequentlyaskedquestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    enabled = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'help_frequentlyaskedquestion'


class MobileDevice(models.Model):
    dev_id = models.CharField(unique=True, max_length=50)
    reg_id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_device'


class NewsArticle(models.Model):
    archived = models.IntegerField()
    readers = models.CharField(max_length=20)
    company = models.ForeignKey(CoreCompany)
    created = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser)
    is_published = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField()
    last_modified_by = models.ForeignKey(AuthUser)
    headline = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    important = models.IntegerField()
    content = models.ForeignKey(ContentContent)
    notified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_article'


class NewsArticleBranches(models.Model):
    article = models.ForeignKey(NewsArticle)
    branch = models.ForeignKey(CoreBranch)

    class Meta:
        managed = False
        db_table = 'news_article_branches'
        unique_together = (('article', 'branch'),)


class NewsArticleBrandings(models.Model):
    article = models.ForeignKey(NewsArticle)
    branding = models.ForeignKey(CoreBranding)

    class Meta:
        managed = False
        db_table = 'news_article_brandings'
        unique_together = (('article', 'branding'),)


class NewsArticleJobtitles(models.Model):
    article = models.ForeignKey(NewsArticle)
    jobtitle = models.ForeignKey(CoreJobtitle)

    class Meta:
        managed = False
        db_table = 'news_article_jobtitles'
        unique_together = (('article', 'jobtitle'),)


class NewsArticleRegions(models.Model):
    article = models.ForeignKey(NewsArticle)
    articleregion = models.ForeignKey('NewsArticleregion')

    class Meta:
        managed = False
        db_table = 'news_article_regions'
        unique_together = (('article', 'articleregion'),)


class NewsArticleregion(models.Model):
    company = models.ForeignKey(CoreCompany)
    region = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'news_articleregion'
        unique_together = (('company', 'region'),)


class NewsNewsplaceholder(models.Model):
    company = models.ForeignKey(CoreCompany, unique=True)
    content = models.ForeignKey(ContentContent)

    class Meta:
        managed = False
        db_table = 'news_newsplaceholder'


class NewsTraineelibrarynews(models.Model):
    trainee = models.ForeignKey(CoreTrainee)
    article = models.ForeignKey(NewsArticle)

    class Meta:
        managed = False
        db_table = 'news_traineelibrarynews'
        unique_together = (('article', 'trainee'),)


class PaymentTransactionrecord(models.Model):
    content_type = models.ForeignKey(DjangoContentType, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    reference = models.CharField(unique=True, max_length=40)
    provider = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=3)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    outcome = models.CharField(max_length=20)
    created = models.DateTimeField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_transactionrecord'


class PaymentTransactionrecorddetail(models.Model):
    transaction_record = models.ForeignKey(PaymentTransactionrecord)
    key = models.CharField(max_length=255)
    value = models.TextField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_transactionrecorddetail'
        unique_together = (('transaction_record', 'key'),)


class RedirectsRedirect(models.Model):
    source_url = models.CharField(unique=True, max_length=255)
    destination_url = models.CharField(max_length=255)
    active = models.IntegerField()
    permanent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'redirects_redirect'


class ResellerReseller(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=255)
    reseller_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'reseller_reseller'


class SouthMigrationhistory(models.Model):
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'


class SupportFlowarticle(models.Model):
    title = models.CharField(max_length=244)
    description = models.TextField()
    article = models.TextField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    last_modified_by = models.ForeignKey(AuthUser)
    is_published = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)
    article_type = models.CharField(max_length=20)
    site = models.CharField(max_length=4)
    area = models.CharField(max_length=50)
    display_on_modal = models.IntegerField()
    tags = models.CharField(max_length=244, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=32)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'support_flowarticle'
