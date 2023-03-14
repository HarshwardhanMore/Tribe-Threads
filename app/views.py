from django.shortcuts import render, redirect
from .models import Database
from .models import UserSpace
from .models import UserSpace

from django.contrib.auth.models import User
# Create your views here.

from numpy import random

import uuid

import simplejson as json


#

from .forms import CreateUserForm
from django.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#


@login_required(login_url='login')
def home(request):

    user_id = request.user
    obj = UserSpace.objects.filter(user_id=user_id)
    if obj:
        print()
    else:
        wishlist = []
        cart = []

        wishlist = json.dumps(wishlist)
        cart = json.dumps(cart)

        obj = UserSpace.objects.create(
            user_id=user_id, wishlist=wishlist, cart=cart)
        obj.save()

    products = Database.objects.all()
    superCategories = set()
    for i in products:
        superCategories.add(i.superCategory)

    superCategories = list(superCategories)
    superCategories.sort()
    superCategoriesDictList = []
    for i in superCategories:
        obj = Database.objects.filter(superCategory=i)
        # print(obj[0].imageName)
        superCategoriesDictList.append(
            {"name": i, "imageName": obj[0].imageName})

    # print(superCategoriesDictList)

    brands = set()
    for i in products:
        brands.add(i.brandName)

    brands = list(brands)
    brands.sort()
    brandsDictList = []

    for i in brands:
        obj = Database.objects.filter(brandName=i)
        brandsDictList.append(
            {"brandName": i, "brandImageName": obj[0].imageName})
        # print(i)

    # print(brandsDictList)

    seasons = set()
    for i in products:
        seasons.add(i.season)
        # print(i.season)

    seasons = list(seasons)
    seasons.sort()
    # print(seasons)
    # seasonsDictList = []

    # for i in seasons:
    #     obj = Database.objects.filter(season=i)
    #     seasonsDictList.append(
    #         {"seasonName": i, })
    #     print(i)

    # print(seasonsDictList)

    context = {
        "superCategoriesDictList": superCategoriesDictList,
        "brandsDictList": brandsDictList,
        "seasons": seasons,
    }

    return render(request, 'index.html', context=context)


@ login_required(login_url='login')
def seller(request):
    if (request.method == 'POST'):

        name = request.POST.get('name')
        gender = request.POST.get('gender')
        price = request.POST.get('price')
        description = request.POST.get('description')
        superCategory = request.POST.get('supercategory')

        subCategories = request.POST.get('supercategory')
        # subCategories = subCategories.split(' ')

        color = request.POST.get('color')
        brandName = request.POST.get('brandname')

        availableSize = request.POST.get('availablesize')
        # availableSize = availableSize.split(' ')

        age = request.POST.get('age')
        season = request.POST.get('season')

        image = request.FILES.get('image')
        imageName = 'default'
        if (image):
            imageName = image.name

        database = Database.objects.create(name=name,
                                           gender=gender,
                                           price=price,
                                           description=description,
                                           superCategory=superCategory,
                                           subCategories=subCategories,
                                           color=color,
                                           brandName=brandName,
                                           availableSize=availableSize,
                                           age=age,
                                           season=season,
                                           image=image,
                                           imageName=imageName,
                                           product_id=brandName + "_" + color +
                                           "_" + name + "_" +
                                           str(random.rand())
                                           )
        database.save()
        return render(request, 'seller.html')

    return render(request, 'seller.html')


# def shop(request):

#     wishlist_dict = []
#     user_id = request.user
#     if (request.method == 'POST'):
#         if (UserSpace.objects.filter(user_id=user_id)):
#             obj = UserSpace.objects.filter(user_id=user_id)

#             user_id = obj[0].user_id
#             quantity = request.POST.get('quantity')
#             wishlist = UserSpace.objects.filter(user_id=user_id)[
#                 0].wishlist + request.POST.get('product_id') + "&Q&" + quantity + "&P&"

#             # Making unique
#             wishlist_list = wishlist.split("&P&")
#             wishlist_set = list(set(wishlist_list))
#             unique_wishlist = ""
#             for i in wishlist_set:
#                 unique_wishlist = unique_wishlist + i + "&P&"

#             obj.delete()

#             userspace = UserSpace.objects.create(user_id=user_id,
#                                                  wishlist=unique_wishlist)
#             userspace.save()

#             #########################################################
#             my_object = UserSpace.objects.filter(user_id=user_id)
#             if my_object:
#                 my_object_wishlist = my_object[0].wishlist
#                 print(my_object_wishlist)
#                 for i in my_object_wishlist.split("&P&"):
#                     print(i)
#                     temp = i.split('&Q&')
#                     print(temp)
#                     if my_object_wishlist:
#                         wishlist_dict = wishlist_dict.append(
#                             dict({"product_id": temp[0], "quantity": temp[1]}))

#         else:
#             user_id = user_id
#             quantity = request.POST.get('quantity')
#             product_id = request.POST.get('product_id')
#             wishlist = str(product_id) + "&Q&" + str(quantity) + "&P&"

#         # ( product1 &Q& quantity1 ) &P& ( product2 &Q& quantity2 ) -- STRING

#             userspace = UserSpace.objects.create(user_id=user_id,
#                                                  wishlist=wishlist)
#             userspace.save()
#         # print(request.user)

#             #########################################################
#             my_object = UserSpace.objects.filter(user_id=user_id)
#             if my_object:
#                 my_object_wishlist = my_object[0].wishlist
#                 print(my_object_wishlist)
#                 for i in my_object_wishlist.split("&P&"):
#                     print(i)
#                     temp = i.split('&Q&')
#                     print(temp)
#                     if my_object_wishlist:
#                         wishlist_dict = wishlist_dict.append(
#                             dict({"product_id": temp[0], "quantity": temp[1]}))

#                 # product = i.split("&Q&")[0]
#                 # quantity = i.split("&Q&")[1]
#                 # quantity = i.product_id

#         # for i in range(len(userspace_objects)):
#         #     products.append(userspace_objects[i])

#     objects = Database.objects.all()

#     # for i in object:
#     #     print(i)
#     # print(objects)
#     # print(objects[0])
#     # print(objects[1])
#     print("----")

#     # for i in range(len(objects)):
#     #     print(objects[i])
#     #     print(objects[i])

#     products = []
#     for i in range(len(objects)):
#         products.append(objects[i])

#     context = {
#         'products': products,
#         'wishlist': wishlist_dict
#     }

#     return render(request, 'shop.html', context=context)

@ login_required(login_url='login')
def shop(request):

    # user_id = hex(uuid.getnode())
    user_id = request.user
    # print("==>")
    # print(request.user)
    user_id = str(request.user)
    wishlist = '[]'
    cart = '[]'

    obj = UserSpace.objects.filter(user_id=user_id)
    if obj:
        print()
    else:
        wishlist = []
        cart = []

        wishlist = json.dumps(wishlist)
        cart = json.dumps(cart)

        obj = UserSpace.objects.create(
            user_id=user_id, wishlist=wishlist, cart=cart)
        obj.save()

    if (request.method == 'POST'):

        product_id = request.POST.get("product_id")
        # quantity = request.POST.get("quantity")

        product = Database.objects.filter(product_id=product_id)
        if product:
            product = product[0]

        # item = {"product_id": str(product_id), "quantity": int(quantity)}

        obj = UserSpace.objects.filter(user_id=user_id)

        # cart = ''

        if (obj):
            user_id = obj[0].user_id
            wishlist = obj[0].wishlist

            cart = obj[0].cart

            # From String to List
            jsonDec = json.decoder.JSONDecoder()
            wishlist = jsonDec.decode(wishlist)

            # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
            #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

            item = product_id

            if item not in wishlist:
                wishlist.append(item)

            # wishlist = list(set(wishlist))

            # From List To String
            wishlist = json.dumps(wishlist)

            # print("DONE")

        else:
            user_id = user_id
            # wishlist = obj[0].wishlist

            # From String to List
            # jsonDec = json.decoder.JSONDecoder()
            # wishlist = jsonDec.decode(wishlist)

            # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
            #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

            item = product_id

            wishlist = [item]

            # wishlist = list(set(wishlist))

            # From List To String
            wishlist = json.dumps(wishlist)
            cart = json.dumps(cart)

            # print("DONE")

        obj.delete()
        obj = UserSpace.objects.create(
            user_id=user_id, wishlist=wishlist, cart=cart)
        obj.save()

    objects = Database.objects.all()

    # # # # # # # # # # # # # # # # # # # # WISH LIST WORK

    my_obj = UserSpace.objects.filter(user_id=user_id)
    wishlist = '[]'
    if my_obj:
        wishlist = my_obj[0].wishlist
    jsonDec = json.decoder.JSONDecoder()
    wishlist = jsonDec.decode(wishlist)

    # # # # # # # # # # # # # # # # # # # # FILTER WORK ( Gender )

    if (request.method == 'POST'):
        gender = request.POST.get("gender")
        if (gender):
            objects = Database.objects.filter(gender=gender)

    # # # # # # # # # # # # # # # # # # # # FILTER WORK ( superCategory )

    if (request.method == 'POST'):
        superCategory = request.POST.get("superCategory")
        if (superCategory):
            objects = Database.objects.filter(superCategory=superCategory)

    # # # # # # # # # # # # # # # # # # # # FILTER WORK ( brandName )

    if (request.method == 'POST'):
        brandName = request.POST.get("brandName")
        if (brandName):
            objects = Database.objects.filter(brandName=brandName)

    # # # # # # # # # # # # # # # # # # # # FILTER WORK ( season )

    if (request.method == 'POST'):
        season = request.POST.get("season")
        if (season):
            objects = Database.objects.filter(season=season)

    # # # # # # # # # # # # # # # # # # # # SEACH WORK ( any )

    results = set()
    if (request.method == 'POST'):
        searchQuery = request.POST.get("searchQuery")
        if (searchQuery):

            objects = Database.objects.filter(name=searchQuery)
            if(objects):
                results.add(objects)
            objects = Database.objects.filter(gender=searchQuery)
            if(objects):
                results.add(objects)
            objects = Database.objects.filter(description=searchQuery)
            if(objects):
                results.add(objects)
            objects = Database.objects.filter(superCategory=searchQuery)
            if(objects):
                results.add(objects)
            objects = Database.objects.filter(brandName=searchQuery)
            if(objects):
                results.add(objects)
            objects = Database.objects.filter(season=searchQuery)
            if(objects):
                results.add(objects)

    # # # # # # # # # # # # # # # # # # # # RENDER WORK
    products = []
    for i in range(len(objects)):
        products.append(objects[i])

    # random.shuffle(products)

    context = {
        'products': products,
        'wishlist': wishlist
    }

    return render(request, 'shop.html', context=context)


@ login_required(login_url='login')
def wishlist(request):

    user_id = request.user
    obj = UserSpace.objects.filter(user_id=user_id)
    if obj:
        print()
    else:
        wishlist = []
        cart = []

        wishlist = json.dumps(wishlist)
        cart = json.dumps(cart)

        obj = UserSpace.objects.create(
            user_id=user_id, wishlist=wishlist, cart=cart)
        obj.save()

    user_id = request.user
    wishlist = '[]'
    product_id_remove = None
    product_id_addToCart = None

    if (request.method == 'POST'):

        product_id_remove = request.POST.get("remove")
        product_id_addToCart = request.POST.get("addToCart")
        # quantity = request.POST.get("quantity")

        if (product_id_addToCart):

            product_id = product_id_addToCart

            product = Database.objects.filter(product_id=product_id)[0]

            # item = {"product_id": str(product_id), "quantity": int(quantity)}

            obj = UserSpace.objects.filter(user_id=user_id)
            cart = obj[0].cart

            if (obj):
                user_id = obj[0].user_id
                wishlist = obj[0].wishlist

                # From String to List
                jsonDec = json.decoder.JSONDecoder()
                wishlist = jsonDec.decode(wishlist)

                # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
                #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

                item = product_id

                if item not in wishlist:
                    wishlist.append(item)

                # wishlist = list(set(wishlist))

                # From List To String
                wishlist = json.dumps(wishlist)

                # print("DONE")

            else:
                user_id = user_id
                # wishlist = obj[0].wishlist

                # From String to List
                # jsonDec = json.decoder.JSONDecoder()
                # wishlist = jsonDec.decode(wishlist)

                # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
                #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

                item = product_id

                wishlist = [item]

                # wishlist = list(set(wishlist))

                # From List To String
                wishlist = json.dumps(wishlist)

                # print("DONE")

            obj.delete()
            obj = UserSpace.objects.create(
                user_id=user_id, wishlist=wishlist, cart=cart)
            obj.save()
        if product_id_remove:
            product_id = product_id_remove

            obj = UserSpace.objects.filter(user_id=user_id)
            user_id = obj[0].user_id
            wishlist = obj[0].wishlist
            cart = obj[0].cart

            jsonDec = json.decoder.JSONDecoder()
            wishlist = jsonDec.decode(wishlist)

            wishlist.remove(product_id)

            # if len(wishlist) > 0:
            wishlist = json.dumps(wishlist)

            obj.delete()

            obj = UserSpace.objects.create(
                user_id=user_id, wishlist=wishlist, cart=cart)
            obj.save()

    # removeFromWishlist_product_id = None
    # if (request.method == 'POST'):
    #     removeFromWishlist_product_id = request.POST.get(
    #         "removeFromWishlist_product_id")
    #     if (removeFromWishlist_product_id != None):
    #         obj = UserSpace.objects.filter(user_id=user_id)[0]
    #         user_id = obj.user_id
    #         cart = obj.cart
    #         wishlist = obj.wishlist
    #         jsonDec = json.decoder.JSONDecoder()
    #         wishlist = jsonDec.decode(wishlist)
    #         cnt = 0
    #         for i in wishlist:
    #             if i.product_id == removeFromWishlist_product_id:
    #                 break
    #             cnt += 1
    #         wishlist.pop(cnt)

    #         obj.delete()

    #         wishlist = json.dump(cart)

    #         obj = UserSpace.objects.create(
    #             user_id=user_id, wishlist=wishlist, cart=cart)
    #         obj.save()

            # wishlist.remove()

    objects = Database.objects.all()

    my_obj = UserSpace.objects.filter(user_id=user_id)
    wishlist = '[]'
    if my_obj:
        wishlist = my_obj[0].wishlist
    jsonDec = json.decoder.JSONDecoder()
    wishlist = jsonDec.decode(wishlist)

    new_wishlist = []
    for i in wishlist:
        my_obj = Database.objects.filter(product_id=i)
        if (my_obj):
            my_obj = my_obj[0]
            new_wishlist.append(
                {"product_id": my_obj.product_id, "product_title": my_obj, "name": my_obj.name, "imageName": my_obj.imageName, "price": my_obj.price})
            # print(my_obj.name)
    products = []
    for i in range(len(objects)):
        products.append(objects[i])

    context = {
        'products': products,
        'wishlist': new_wishlist
    }

    return render(request, "wishlist.html", context=context)


@ login_required(login_url='login')
def cart(request):
    # print("+++++++++++++++++++++++++++")

    user_id = request.user
    cart = '[]'
    addToCart = None

    product_id_remove = None

    if (request.method == 'POST'):

        addToCart = request.POST.get("addToCart")
        product_id_remove = request.POST.get("remove")

        # product_id_remove = remove

        if addToCart:

            product_id = addToCart
            # quantity = request.POST.get("quantity")

            # product = Database.objects.filter(product_id=product_id)[0]

            # item = {"product_id": str(product_id), "quantity": int(quantity)}

            obj = UserSpace.objects.filter(user_id=user_id)
            wishlist = obj[0].wishlist
            cart = obj[0].cart

            if obj:
                user_id = obj[0].user_id
                cart = obj[0].cart

                if cart != None:
                    # From String to List
                    jsonDec = json.decoder.JSONDecoder()
                    cart = jsonDec.decode(cart)

                    # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
                    #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

                    item = product_id

                    # print("PRODUCT ID : ")
                    # print(product_id)

                    if item not in cart:
                        cart.append(item)

                    # wishlist = list(set(wishlist))

                    # From List To String
                    cart = json.dumps(cart)

                    # print("DONE")
                else:

                    # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
                    #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

                    item = product_id

                    cart = [item]
                    # From List To String
                    cart = json.dumps(cart)

                    # print("DONE INSIDE CART")

            else:
                user_id = user_id
                # wishlist = obj[0].wishlist

                # From String to List
                # jsonDec = json.decoder.JSONDecoder()
                # wishlist = jsonDec.decode(wishlist)

                # item = {"product_id": product_id, "image_name": product.imageName, "brand": product.brandName,
                #         "name": product.name, "price": product.price, "color": product.color, "size": product.availableSize, "quantity": quantity}

                item = product_id

                cart = [item]

                # wishlist = list(set(wishlist))

                # From List To String
                cart = json.dumps(cart)

                # print("DONE INSIDE CART")

            obj.delete()
            obj = UserSpace.objects.create(
                user_id=user_id, wishlist=wishlist, cart=cart)
            obj.save()

        if product_id_remove:
            product_id = product_id_remove

            obj = UserSpace.objects.filter(user_id=user_id)
            user_id = obj[0].user_id
            wishlist = obj[0].wishlist
            cart = obj[0].cart

            jsonDec = json.decoder.JSONDecoder()
            cart = jsonDec.decode(cart)

            if product_id in cart:
                cart.remove(product_id)

            # if len(wishlist) > 0:
            cart = json.dumps(cart)

            obj.delete()

            obj = UserSpace.objects.create(
                user_id=user_id, wishlist=wishlist, cart=cart)
            obj.save()

    objects = Database.objects.all()

    my_obj = UserSpace.objects.filter(user_id=user_id)
    cart = ''
    cart = json.dumps(cart)
    if my_obj:
        cart = my_obj[0].cart
    jsonDec = json.decoder.JSONDecoder()
    cart = jsonDec.decode(cart)

    products = []
    for i in range(len(objects)):
        products.append(objects[i])
        # print(objects[i])

    obj = UserSpace.objects.filter(user_id=user_id)
    cart = obj[0].cart
    jsonDec = json.decoder.JSONDecoder()
    cart = jsonDec.decode(cart)
    # print(cart)
    cart_products = []

    for i in cart:
        obj = Database.objects.filter(product_id=str(i))
        if (obj):
            cart_products.append(obj[0])
        # print(i)
        # print(obj[0])

    # new_cart = []
    # for i in cart:
    #     my_obj = Database.objects.filter(product_id=i)
    #     if (my_obj):
    #         my_obj = my_obj[0]
    #         new_cart.append(
    #             {"product_id": my_obj.product_id, "product_title": my_obj, "name": my_obj.name, "imageName": my_obj.imageName, "price": my_obj.price})

    # print(cart_products)

    total = 0
    for i in cart_products:
        total += float(i.price)
        # print(i)
    # print(i[0])

    context = {
        'products': products,
        'cart': cart,
        'cart_products': cart_products,
        'total': total
    }

    return render(request, "cart.html", context=context)


@ login_required(login_url='login')
def categories(request):
    products = Database.objects.all()
    superCategories = set()
    for i in products:
        superCategories.add(i.superCategory)

    superCategories = list(superCategories)
    superCategories.sort()
    superCategoriesDictList = []
    for i in superCategories:
        obj = Database.objects.filter(superCategory=i)
        # print(obj[0].imageName)
        superCategoriesDictList.append(
            {"name": i, "imageName": obj[0].imageName})

    # print(superCategoriesDictList)

    brands = set()
    for i in products:
        brands.add(i.brandName)

    brands = list(brands)
    brands.sort()
    brandsDictList = []

    for i in brands:
        obj = Database.objects.filter(brandName=i)
        brandsDictList.append(
            {"brandName": i, "brandImageName": obj[0].imageName})
        # print(i)

    # print(brandsDictList)

    seasons = set()
    for i in products:
        seasons.add(i.season)

    seasons = list(seasons)
    seasons.sort()
    # print(seasons)
    # seasonsDictList = []

    # for i in seasons:
    #     obj = Database.objects.filter(season=i)
    #     seasonsDictList.append(
    #         {"seasonName": i, })
    #     print(i)

    # print(seasonsDictList)

    context = {
        "superCategoriesDictList": superCategoriesDictList,
        "brandsDictList": brandsDictList,
        "seasons": seasons,
    }
    return render(request, "categories.html", context=context)



def profile(request):
    
    my_obj = UserSpace.objects.filter(user_id=request.user)
    wishlist_len = 0
    cart_len = 0

    if(my_obj):
        jsonDec = json.decoder.JSONDecoder()
        wishlist_len = len(jsonDec.decode(my_obj[0].wishlist))
        cart_len = len(jsonDec.decode(my_obj[0].cart))

    print(wishlist_len)
    print(cart_len)

    me = User.objects.filter(username=request.user)
    if(me):
        me = me[0]

    context={"me":me,
             "wishlist_len": wishlist_len, 
             "cart_len": cart_len}

    return render(request, "profile.html", context=context)


# ############################## LOGIN


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticate user

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account Created successfully for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

# ##############################
