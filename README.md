---

## 👥 Acteurs de l'application

| Acteur | Rôle |
|--------|------|
| Visiteur | Consulter les médecins, s'inscrire |
| Patient | Réserver, annuler, voir l'historique |
| Médecin | Gérer disponibilités, consulter planning |
| Administrateur | Gérer la plateforme complète |

---

## 🤖 Fonctionnalité IA

Le module d'orientation utilise **TF-IDF** et la **similarité cosinus** pour
analyser les symptômes saisis par le patient et suggérer une spécialité médicale.

**Exemple :**
- Entrée : `douleur poitrine palpitations essoufflement`
- Sortie : `Cardiologie (85%)`, `Médecine générale (12%)`

> ⚠️ Cette fonctionnalité est indicative uniquement et ne constitue pas
> un diagnostic médical.

---

## 🧪 Tests

```bash
python manage.py test
```

Résultat attendu : `3 tests OK`

---

##  Sécurité

- Mots de passe hashés par Django
- Protection CSRF activée sur tous les formulaires
- Variables sensibles dans `.env` (jamais commitées)
- Mode DEBUG désactivé en production
- Accès limité par rôle utilisateur
- Validation des formulaires côté serveur

---

##  CI/CD GitHub Actions

Chaque push sur `main` déclenche automatiquement :

1.  Récupération du code
2.  Installation Python & dépendances
3.  Migrations de test
4.  Exécution des tests
5.  Vérification qualité (flake8)
6.  Build image Docker
7.  Push sur Docker Hub

---

##  Captures d'écran

> Ajouter les captures d'écran de l'application ici

---

##  Auteur

**Khaoula** — Filière ingénieurs  
Module : Développement Web avec Django  
Année universitaire 2025–2026