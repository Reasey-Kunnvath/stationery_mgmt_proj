def default_sidebar(request):
    return {
        'sidebar_items': [
            {'url_name': 'dashboard_home', 'icon': 'fas fa-home', 'label': 'Home'},
            {'url_name': 'category', 'icon': 'fas fa-list', 'label': 'Category'},  
            {'url_name': 'user', 'icon': 'fas fa-users', 'label': 'Users'},       
        ]
    }
