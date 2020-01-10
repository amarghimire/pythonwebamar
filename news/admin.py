from django.contrib import admin

# Register your models here.
from . models import *
#generic view bata users gareko
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name','status']
    search_fields = ['cat_name']
    actions = ['update_status_active','update_status_inactive']

    def update_status_active(self,request,query):
        return query.update(status=True)
    def update_status_inactive(self,request,query):
        return query.update(status=False)
    update_status_active.short_description = 'Active gar bhai'
    update_status_inactive.short_description='inactive gar bhai'

@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    list_display = ['title',]
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['product_name','status','title','posted_by','image','category'] #admin maa k k dekhaune bhanne kuraa
    search_fields = ['product_name','title','category']
    prepopulated_fields = {'slug':('title',)} #slug maa lagera title raakha bhaneko admin ko category maa

@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Photographpf)
class AdminPhotographpf(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
# admin.site.users(Category)
# admin.site.users(Gallery)
#shortcut maa yasari users garna pani sakinchha hai





@admin.register(Cosmo)
class AdminCosmo(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Entry)
class AdminEntry(admin.ModelAdmin):
    list_display = ['headline',]
    # prepopulated_fields = {'pub_date': ('headline',)}

