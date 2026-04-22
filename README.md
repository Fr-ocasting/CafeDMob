#### Fichier construit par moi même:
- `index.qmd` : contient l'ensemble du contenu des slides, les codes python (ou R, Julia, ...) 
- `custom.css` : configure le style des slides
- `plot/`: contient les figures ou vidéos à intégrer dans les slides  
- `template_cerema/fig/`: fig svg à call dans l'en-tête de index.qmd
- `chatbot_context_token_date.json`: contient une dataset pour un graph d'analyse développé en python dans index.qmd
- `.gititgnore`
- `README.md`
- `environment.yml`: environnement conda pour compiler quarto & ma visualisation python  


####   Fichier construit après run de  `quarto publish gh-pages index.qmd`:
- `site_libs/`
- `.quarto/`
- `index.html` 