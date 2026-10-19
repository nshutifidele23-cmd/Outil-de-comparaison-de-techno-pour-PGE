# Outil-de-comparaison-de-techno-pour-PGE

Bonjour,
J'ai créé ce script pour nous aider à comparer les technologies et les paramètres de manière plus rigoureuse. Le principe est simple : il suffit de saisir quelques paramètres dans une feuille Excel et une équation dans l'outil pour obtenir un graphique comparatif.
L'objectif est de simplifier notre travail, de limiter le recours à l'IA, qui pourrait induire en erreur, et de garantir une analyse approfondie.
Dans la lignée de l’open source, il s’agit ici de la version V1 et je vous invite à y apporter les modifications nécessaires afin que nous puissions les intégrer et continuer à nous entraider.

Pour l’utiliser, voici la marche à suivre : 

Clonez le dépôt :
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/nshutifidele23-cmd/Outil-de-comparaison-de-techno-pour-PGE.git)

Installez les dépendances :
pip install numpy pandas matplotlib openpyxl

Configurez le fichier Excel : ajoutez vos composants et leurs paramètres de modèle, à une composante par ligne.

Configurez profilage.py : définissez le nom du fichier Excel, les libellés des axes, la plage de tracé, le point de fonctionnement et l’équation mathématique.

Exécutez le script :
python profilage.py
