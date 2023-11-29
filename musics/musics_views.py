from django.shortcuts import render

def musics_by_category(request):
    context = {
        'pop_musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
        ],

        'rock_musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg"
            },
        ],

        'metal_musics': [
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
        ],
    }
    return render(request, "musics/musics_by_category.html", context)
