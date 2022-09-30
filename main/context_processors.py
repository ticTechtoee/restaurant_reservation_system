from .models import Menu

def menu_navbar(request):
    menu_item = Menu.objects.all()
    return {
        'menu_item' : menu_item
    }
