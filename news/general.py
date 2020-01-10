from .models import *
def data(request):
    content= {
        'categoryData':Category.objects.prefetch_related('product_set').all(),
    }
    return content