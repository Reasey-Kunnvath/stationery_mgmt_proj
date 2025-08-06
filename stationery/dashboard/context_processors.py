def default_sidebar(request):
    return {
        'sidebar_items': [
            {
                'url_name': 'dashboard_home', 
                'icon': 'fas fa-home', 
                'label': 'Home',
                'type': 'label'
            },
            {
                'url_name': 'user', 
                'icon': 'fas fa-users', 
                'label': 'Users',
                'type': 'label'
            },
            {
                'url_name': 'item', 
                'icon': 'fas fa-box', 
                'label': 'Items',
                'type': 'label'
            },
            {
                'url_name': 'category', 
                'icon': 'fas fa-list', 
                'label': 'Category',
                'type': 'label'
            }, 
            {
                'url_name': 'supplier', 
                'icon': 'fas fa-truck', 
                'label': 'Suppliers',
                'type': 'label'
            },
            {
                'url_name': 'sply_mgmt',
                'icon': 'fas fa-cogs',
                'label': 'Supply Management',
                'type': 'dropdown', 
                'children': [
                    {
                        'url_name': 'supply_in',
                        'icon': 'fas fa-circle',
                        'label': 'Stock In'
                    },
                    {
                        'url_name': 'supply_out',
                        'icon': 'fas fa-circle',
                        'label': 'Stock Out'
                    },
                    {
                        'url_name': 'request',
                        'icon': 'fas fa-circle',
                        'label': 'Requisitions'
                    }
                ]
            }
           
            
        ]
    }
