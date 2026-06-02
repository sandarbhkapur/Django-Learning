from django.contrib import admin
from .models import Category, Blog, About,SocalLink

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug': ('title',)}
    list_display= ('title','category','author','status','is_featured')
    search_fields =('id','title','category__category_name','author__username','status')
    # list_editable = ('is_featured',) // we can uncommet this and use it

    list_filter = ('status', 'is_featured', 'category')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

class SocailAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link', 'created_at')

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(SocalLink, SocailAdmin)



