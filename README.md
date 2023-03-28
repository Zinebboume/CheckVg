# CheckVg
#Create Virtual (Windows) Environment:

py -m venv env
.\env\Scripts\activate


#prerequis: 

pip install -r reuiqrements.txt

run app: 
streamlit run app.py           

# To share with public: 

Pour partager votre application Streamlit avec le public, vous pouvez utiliser Streamlit Sharing, un service d'hébergement gratuit pour vos applications Streamlit. Voici comment procéder :

Créez un compte GitHub si vous n'en avez pas déjà un.
Créez un nouveau dépôt (repository) sur GitHub et donnez-lui un nom approprié.
Ajoutez tous les fichiers de votre application Streamlit dans ce dépôt. Assurez-vous d'inclure tous les fichiers nécessaires, tels que le fichier contenant votre code (par exemple app.py), les fichiers de données (par exemple OpenFoodFacts.csv) et éventuellement les fichiers requirements.txt et Procfile.
Allez sur share.streamlit.io et connectez-vous avec votre compte GitHub.
Cliquez sur "New app" en haut à droite de la page.
Sélectionnez le dépôt que vous avez créé à l'étape 2, puis sélectionnez la branche et le fichier de votre application (par exemple, app.py).
Cliquez sur "Deploy" pour déployer votre application.
Streamlit Sharing déploiera votre application et vous fournira un lien public que vous pourrez partager avec d'autres personnes. Notez que l'utilisation de Streamlit Sharing est gratuite, mais soumise à certaines limitations en termes de ressources et de temps d'exécution.

Si vous souhaitez plus de contrôle sur votre hébergement ou si vous avez besoin de ressources supplémentaires, vous pouvez envisager d'autres options d'hébergement comme Heroku, AWS, Google Cloud ou Microsoft Azure.



