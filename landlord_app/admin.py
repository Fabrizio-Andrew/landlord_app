from django.contrib import admin
from .models import User, Unit, Tenant, Lease, Tenant_Payment, Evict_Notice

# Register your models here.

admin.site.register(User)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(Tenant_Payment)
admin.site.register(Evict_Notice)