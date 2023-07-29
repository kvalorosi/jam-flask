from app import app

from flask import flash, redirect, render_template, request, url_for
import requests
from app.auth.forms import FoodForm
# from app.models import Products

@app.route('/')
def land():

    return render_template('opening.html')

# @app.route('/ingredeints', methods=['GET', 'POST'])
# def ingredients():
#     form = FoodForm()
#     if request.method == 'POST':
#         if form.validate():
#             food_name = form.food_name.data
#             Ingredients = Ingredients.query.filter_by(food_name=food_name).first()
#             if ingredients:
#                 print(ingredients)
#                 return render_template('home.html', form=form, food=ingredients)
            
#             response = requests.get(f"https://api.spoonacular.com/food/ingredients/search")
#             if response.ok:
#                 data = response.json()
#                 print(data)
#                 ingredients = {}
#                 ingredients['food_name'] = data['name']

#                 ingredient_list = Ingredients(
#                     food_name= ingredients['food_name']
#                 )
    
#                 ingredient_list.save_food()
#                 return render_template('opening.html', form=form, food=ingredients)
                


#     return render_template('opening.html', form=form, food=ingredients)

# @app.get('/products')
# def get_the_products():
#     products = Products.query.all()
#     p_list = {p.to_dict() for p in products}
#     return {
#         'status' : 'ok',
#         'products' : p_list
#     }