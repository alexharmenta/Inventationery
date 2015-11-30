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
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Countries(models.Model):
    id_countries = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    iso_alpha2 = models.CharField(max_length=2, blank=True, null=True)
    iso_alpha3 = models.CharField(max_length=3, blank=True, null=True)
    iso_numeric = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    currency_name = models.CharField(max_length=32, blank=True, null=True)
    currrency_symbol = models.CharField(max_length=3, blank=True, null=True)
    flag = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class DirpartyDirpartymodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    name = models.CharField(db_column='Name', max_length=60)  # Field name made lowercase.
    namealias = models.CharField(db_column='NameAlias', max_length=50, blank=True, null=True)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=5)  # Field name made lowercase.
    secondname = models.CharField(db_column='SecondName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    firstlastname = models.CharField(db_column='FirstLastName', max_length=30)  # Field name made lowercase.
    secondlastname = models.CharField(db_column='SecondLastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dirparty_dirpartymodel'


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


class InventoryInventmodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    itemid = models.CharField(db_column='ItemId', unique=True, max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UnitId', max_length=20)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    vendorprice = models.DecimalField(db_column='VendorPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    itemimage = models.CharField(db_column='ItemImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    primaryvendor = models.ForeignKey('VendorVendormodel', db_column='PrimaryVendor_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory_inventmodel'


class LogisticselectronicaddressLogisticselectronicaddressmodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary')  # Field name made lowercase.
    party = models.ForeignKey(DirpartyDirpartymodel, db_column='Party_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logisticselectronicaddress_logisticselectronicaddressmodel'


class LogisticspostaladdressLogisticspostaladdressmodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=30)  # Field name made lowercase.
    countryregionid = models.CharField(db_column='CountryRegionId', max_length=3)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=30, blank=True, null=True)  # Field name made lowercase.
    streetnumber = models.SmallIntegerField(db_column='StreetNumber', blank=True, null=True)  # Field name made lowercase.
    buildingcompliment = models.CharField(db_column='BuildingCompliment', max_length=10, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary')  # Field name made lowercase.
    party = models.ForeignKey(DirpartyDirpartymodel, db_column='Party_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logisticspostaladdress_logisticspostaladdressmodel'


class PurchorderPurchlinemodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purchqty = models.IntegerField(db_column='PurchQty', blank=True, null=True)  # Field name made lowercase.
    purchunit = models.CharField(db_column='PurchUnit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    purchprice = models.DecimalField(db_column='PurchPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linedisc = models.DecimalField(db_column='LineDisc', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    linepercent = models.DecimalField(db_column='LinePercent', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lineamount = models.DecimalField(db_column='LineAmount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchlinestatus = models.CharField(db_column='PurchLineStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    linenum = models.SmallIntegerField(db_column='LineNum', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey(InventoryInventmodel, db_column='ItemId_id', blank=True, null=True)  # Field name made lowercase.
    purchorder = models.ForeignKey('PurchorderPurchordermodel', db_column='PurchOrder_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchorder_purchlinemodel'


class PurchorderPurchordermodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    purchid = models.CharField(db_column='PurchId', unique=True, max_length=45)  # Field name made lowercase.
    purchname = models.CharField(db_column='PurchName', max_length=100)  # Field name made lowercase.
    purchasetype = models.CharField(db_column='PurchaseType', max_length=50)  # Field name made lowercase.
    purchstatus = models.CharField(db_column='PurchStatus', max_length=100)  # Field name made lowercase.
    workerpurchplacer = models.CharField(db_column='WorkerPurchPlacer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=5)  # Field name made lowercase.
    deliveryname = models.CharField(db_column='DeliveryName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    confirmeddlv = models.DateField(db_column='ConfirmedDlv', blank=True, null=True)  # Field name made lowercase.
    dlvmode = models.CharField(db_column='DlvMode', max_length=20)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=3)  # Field name made lowercase.
    payment = models.CharField(db_column='Payment', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymmode = models.CharField(db_column='PaymMode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('VendorVendormodel', db_column='Vendor_id')  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchorder_purchordermodel'


class VendorVendormodel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    accountnum = models.CharField(db_column='AccountNum', unique=True, max_length=45)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=3)  # Field name made lowercase.
    onetimevendor = models.IntegerField(db_column='OneTimeVendor')  # Field name made lowercase.
    vendgroup = models.CharField(db_column='VendGroup', max_length=3)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=3)  # Field name made lowercase.
    vatnum = models.CharField(db_column='VATNum', max_length=13)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
    party = models.ForeignKey(DirpartyDirpartymodel, db_column='Party_id', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendor_vendormodel'
