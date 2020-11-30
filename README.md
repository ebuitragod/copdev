#### Qué encontrarán en este repositorio. 

1. Un admin.py configurado. En el administrador de Django, podrán crear, modificar y eliminar elementos en los modelos de productos y consumiciónes pero _no en el de categorías_.
2. Un Rest-framework API configurado para ver los objetos de productos en lista e individuales, por código; categorías, en lista e individuales, por código; y las consumiciones, en lista e individuales, por fecha. 
3. Un CRUD configurado con unos formularios básicos en html en los cuales se podrá crear, modificar o eliminar elementos de los modelos de productos, consumiciones y categorías. 
4. Tres tipos de tests creados para verificar los modelos, los forms y los views. Lamentablemente no hice todos los que se hubieran podido haber hecho, pero hice los que sirven de modelo para hacer el resto.

## Listado de urls a encontrar. 
### API
No necesita estar autenticado. Esta opción se puede cambiar. 

        '/api/categorias/'
        
        '/api/informacion_categorias/code=<str:code>/'
        
        '/api/productos/'
        
        '/api/informacion_productos/code=<str:code>/'
        
        '/api/consumiciones/'
        
        '/api/informacion_consumiciones/code=<str:code>/'
        
        
### CRUD

No necesita estar autenticado. 

#===Category

    '/api/categoria/lista/'
    
    '/api/categoria/crear/'
    
    '/api/categoria/code=<str:code>/'
    
    '/api/categoria/code=<str:code>/editar/'
    
    '/api/categoria/code=<str:code>/eliminar/'
    
    
#===Product

    '/api/producto/lista/'
    
    '/api/producto/crear/'
    
    '/api/producto/code=<str:code>/'
    
    '/api/producto/code=<str:code>/editar/'
    
    '/api/producto/code=<str:code>/eliminar/'
    
    
#===Consumption

    '/api/consumicion/lista/'
    
    '/api/consumicion/crear/'
    
    '/api/consumicion/timestamp=<str:timestamp>/'
    
    '/api/consumicion/timestamp=<str:timestamp>/editar/'
    
    '/api/consumicion/timestamp=<str:timestamp>/eliminar/' 
    



### ADMIN

Necesita estar autenticado. 

    run <cd /backend/ python manage.py createsuperuser>
    
    Siga las instrucciones. 
    
    run <python manage.py runserver
    
    Ingrese a /admin/ el usuario y la contraseña creados en los pasos anteriores. 
    
    Juegue con la plataforma del Django-Admin.
    
    
