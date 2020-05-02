# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class StockApp(models.Model):
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    dates = models.TextField(blank=True, null=True)
    consolidated_income = models.BigIntegerField(db_column='Consolidated Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_of_revenue = models.BigIntegerField(db_column='Cost of Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_per_share = models.BigIntegerField(db_column='Dividend per Share', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebit = models.BigIntegerField(db_column='EBIT', blank=True, null=True)  # Field name made lowercase.
    ebit_margin = models.BigIntegerField(db_column='EBIT Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebitda = models.BigIntegerField(db_column='EBITDA', blank=True, null=True)  # Field name made lowercase.
    ebitda_margin = models.BigIntegerField(db_column='EBITDA Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps = models.BigIntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    eps_diluted = models.BigIntegerField(db_column='EPS Diluted', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earnings_before_tax_margin = models.BigIntegerField(db_column='Earnings Before Tax Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earnings_before_tax = models.BigIntegerField(db_column='Earnings before Tax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    free_cash_flow_margin = models.BigIntegerField(db_column='Free Cash Flow margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_margin = models.BigIntegerField(db_column='Gross Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_profit = models.BigIntegerField(db_column='Gross Profit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income_tax_expense = models.BigIntegerField(db_column='Income Tax Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interest_expense = models.BigIntegerField(db_column='Interest Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income = models.BigIntegerField(db_column='Net Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_discontinued_ops = models.BigIntegerField(db_column='Net Income - Discontinued ops', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_non_controlling_int = models.BigIntegerField(db_column='Net Income - Non-Controlling int', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_com = models.BigIntegerField(db_column='Net Income Com', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_profit_margin = models.BigIntegerField(db_column='Net Profit Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operating_expenses = models.BigIntegerField(db_column='Operating Expenses', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operating_income = models.BigIntegerField(db_column='Operating Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preferred_dividends = models.BigIntegerField(db_column='Preferred Dividends', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profit_margin = models.BigIntegerField(db_column='Profit Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    r_d_expenses = models.BigIntegerField(db_column='R&D Expenses', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue = models.BigIntegerField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    revenue_growth = models.BigIntegerField(db_column='Revenue Growth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sg_a_expense = models.BigIntegerField(db_column='SG&A Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weighted_avg_shs_out = models.BigIntegerField(db_column='Weighted Avg Shs Out', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weighted_average_shs_out_dil = models.BigIntegerField(db_column='Weighted Average Shs Out_Dil', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'stock_app'
