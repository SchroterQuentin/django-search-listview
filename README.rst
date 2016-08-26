========================
Django-drybones
========================

.. image:: https://landscape.io/github/unistra/django-drybones/master/landscape.svg?style=flat
   :target: https://landscape.io/github/unistra/django-drybones/master
   :alt: Code Health

Template pour les projets Django 1.8.

Prérequis
===================
pip, virtualenv et virtualenvwrapper doivent être installés.

Procédure
===================
Pour générer un template pour le projet "**myapp**" :

Création de l'environnement virtuel
-----------------------------------

Pour créer l'environnement virtuel, se placer dans le répertoire d'installation du projet::

    $ mkvirtualenv myapp

Installation de Django
----------------------

Pour installer Django dans l'environnement virtuel::

    $ pip install "Django>1.8,<1.9"

Création du projet
-------------------

Pour créer le nouveau projet en utilisant le template::

    $ django-admin.py startproject --template=https://github.com/unistra/django-drybones/archive/master.zip --extension=html,rst,ini,coveragerc --name=Makefile myapp

Configuration du projet
-----------------------

Pour configurer le projet dans l'environnement virtuel::

    $ cd myapp
    $ setvirtualenvproject $VIRTUAL_ENV $(pwd)

    # Edition du fichier postactivate
    $ echo "export DJANGO_SETTINGS_MODULE=myapp.settings.dev" >> $VIRTUAL_ENV/bin/postactivate

    # Edition du fichier postdeactivate
    $ echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

    # Rechargement de l'environnement virtuel
    $ workon myapp

Installation des librairies
---------------------------

Pour installer les librairies ::

    $ cdproject
    $ pip install -r requirements/dev.txt

Lancer le serveur de développement
----------------------------------

Pour finaliser l'installation et lancer le serveur::

    $ chmod u+x manage.py
    $ ./manage.py migrate
    $ ./manage.py runserver

Goodies
-------

Vous pouvez ajouter une fonction à vos dotfiles pour faciliter la création d'un projet::

    # inits project for django-drybone project
    # see https://github.com/unistra/django-drybones
    # Usage initproject project_name [ -p python_version -d django_version]
    # example initproject -p 3 -d 1.8.4
    initproject () {

            # TODO: be sure those variables are required by vitualenv* stuff

            declare -g PYTHON_VERSION=${PYTHON_VERSION:=3.4}
            declare -g PYTHON_PATH=
            declare -g PYTHON_VERSION_PATH=$( which python$PYTHON_VERSION )

            # TODO: split this message up: make it readable

            test -z $1 && {
                    echo -e "Missing argument. Script usage:\n" "   initproject project_name [ -p python_version -d django_version]" "   example : initproject -p 3 -d 1.8.4 "
                    return 1
            }

            local PROJECT_NAME=$1
            local DJANGO_VERSION=${DJANGO_VERSION:=Django>1.8,<1.9}

            local ARGS=`getopt --long -o "p:d:" "$@"`
            eval set -- "$ARGS"
            while true
            do
                    case "$1" in
                            (-p) PYTHON_VERSION=$2
                                    shift 2 ;;
                            (-d) DJANGO_VERSION=Django==$2
                                    shift 2 ;;
                            (*) break ;;
                    esac
            done

            mkvirtualenv $PROJECT_NAME -p "$PYTHON_VERSION_PATH"
            workon $PROJECT_NAME
            test -n ${VIRTUAL_ENV-} || {
                echo no env, no gain >&2
                return 1
            }

            pip install "$DJANGO_VERSION"

            django-admin startproject --template=https://github.com/unistra/django-drybones/archive/master.zip --extension=html,rst,ini,coveragerc --name=Makefile $PROJECT_NAME
            cd $PROJECT_NAME
            setvirtualenvproject $VIRTUAL_ENV $PWD
            echo "export DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.dev" >> $VIRTUAL_ENV/bin/postactivate
            echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
            workon $PROJECT_NAME
            chmod +x manage.py
            pip install -r requirements/dev.txt
    }

Et ensuite pour creer le virtualenv, installer django et initialiser le projet::

    $ initproject mon_projet

pour preciser la version de python et/ou de django -p pour la version de python et -d pour la version de django::

    $ initproject mon_projet -p 3 -d 1.8.4


