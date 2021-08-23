# **Visitor**.yaml — Role Example
> App: **cookbook** 

> Models: [ **category, ingredient & recipe** ]

```yaml
# Role
visitor:

    # App
    cookbook:

        # Model-1
        category: 
            create : [id, name]
            update : [id, name]
            read   : [id, name, ingredients: cookbook.ingredient]
            delete : [del]

        # Model-2
        ingredient: 
            create : [id, name, category: cookbook.category]
            update : [id, name, category: cookbook.category]
            read   : [id, name, recipes: cookbook.recipe]
            delete : [del]

        # Model-3
        recipe: 
            create : [id, name]
            update : [id, name]
            read   : [id, name]
            delete : [del]
```