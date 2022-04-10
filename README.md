# Arc Au Cou
Chaque jour un nouveau sudoku est proposé et il faut le résoudre le plus rapidement possible. Un classement général affiche les meilleurs joueurs de la journée sur Arc Au Cou.

# Arc Au Cou - Backend
## Installation

### Add the daily sudoku generation
```bash
# in the folder ./arcaucou and in the virtual environment
python manage.py crontab add
```

### Dependencies
- [asgiref](https://github.com/django/asgiref) v3.4.1
- [backports.zoneinfo](https://pypi.org/project/backports.zoneinfo/) v0.2.1
- [Django](https://www.djangoproject.com/download/) v4.0.2
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) v3.10.1
- [django-crontab](https://pypi.org/project/django-crontab/) v0.7.1
- [djangorestframework](https://www.django-rest-framework.org/) v3.13.1
- [mysqlclient](https://pypi.org/project/mysqlclient/) v2.1.0
- [numpy](https://numpy.org/) v1.22.3
- [pytz](https://pypi.org/project/pytz/) v2021.3
- [sqlparse](https://pypi.org/project/sqlparse/) v0.4.2
- [typing_extensions](https://pypi.org/project/typing-extensions/) v4.1.1
- [tzdata](https://pypi.org/project/tzdata/) v2021.5

# Arc Au Cou - Frontend

## Installation
### Install dependencies
```bash
# in the folder ./arcaucou-front
npm install
```

### Start the developpement environement
```bash
# in the folder ./arcaucou-front
npm run dev
```

### Generate the static files for the server
```bash
# in the folder ./arcaucou-front
npm run generate
```

### Dependencies
## NuxtJS
- [NuxtJS](https://nuxtjs.org/) v2.15.8
- [@nuxtjs/auth](https://auth.nuxtjs.org/) v4.9.1
- [@nuxtjs/toast](https://www.npmjs.com/package/@nuxtjs/toast) v3.3.1
- [@nuxtjs/axios](https://axios-http.com/) v5.13.6
- [@nuxtjs/color-mode](https://color-mode.nuxtjs.org/) v2.1.1
- [@nuxtjs/tailwindcss](https://tailwindcss.nuxtjs.org/) v4.2.1
- [cookie-universal-nuxt](https://www.npmjs.com/package/cookie-universal-nuxt) v2.1.5

## Vue.js
- [Vue.js](https://vuejs.org/) v2.6.14
- [vue-confetti](https://www.npmjs.com/package/vue-confetti) v2.3.0

## Javascript
- [moment.js](https://momentjs.com/) v1.6.1

## Credits
- [Izzo Valentino](https://github.com/Tino3210)
- [Bruno Costa](https://github.com/Psemata)
