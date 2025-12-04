intro="""
"""

texte_intro_produits = """
Cette page analyse les performances produits :  
- **catégories les plus rentables**  
- **produits les plus vendus**  
- **prix moyens**  
- **satisfaction client**  
- **délais de livraison**  
- **analyse interactive par catégorie**  
"""


texte_logistique = """
Cette page analyse les performances logistiques :
- **délais moyens de livraison**
- **flux vendeurs → clients**
- **analyse origine/destination**
- **lien entre retard et notes clients**
"""

texte_fm = """
Segmentation RFM simplifiée :
- **Frequency** : nombre de commandes du client
- **Monetary** : montant total dépensé (produits + livraison)

Objectif :
Identifier les segments stratégiques :
- **Best Customers**
- **High-Value One-Timers**
- **Loyal Customers**
- **Low-Value Customers**
"""

# Analyses géographiques - Focus Compétitivité Vendeurs Olist
analyse_carte_geo = """
### Géographie de l'Expérience Client = Compétitivité Vendeurs

**Avec 97% de clients one-shot, la géographie détermine la performance reviews des vendeurs.**

**Régions d'Excellence (RS, PR, SC - Sud)**  
- Délais moyens : **10-12 jours** (2x plus rapides que la moyenne)
- Satisfaction : **65-70% de clients 5 étoiles**
- **Impact pour vendeurs** : Reviews exceptionnelles → meilleure visibilité sur marketplaces
- **Recommandation** : Prioriser expansion vendeurs dans ces régions (avantage compétitif garanti)

**Régions à Risque (PA, AM, RR - Nord)**  
- Délais moyens : **>25 jours** (infrastructure logistique défaillante)
- Satisfaction : **25-30% de clients 5 étoiles** seulement
- **Impact pour vendeurs** : Mauvaises reviews → chute de compétitivité vs concurrence locale
- **Recommandation** : Afficher délais réels AVANT achat (transparence) ou améliorer logistique

**États Intermédiaires (SP, RJ, MG - Sud-Est)**  
- Concentration de 70% du CA mais satisfaction moyenne
- Délais corrects (15-18j) mais peuvent être optimisés
- **Potentiel** : Réduire délais de 5j → +15% de clients 5 étoiles → boost compétitivité vendeurs

**Insight clé** : La géographie détermine si les vendeurs Olist sont **compétitifs** (Sud) ou **désavantagés** (Nord).
"""

analyse_flux_geo = """
### Routes Logistiques et Compétitivité Vendeurs

**Centralisation excessive sur São Paulo**  
SP expédie vers tous les états, créant des **disparités de performance** pour les vendeurs Olist :

**Routes courtes (SP → Sud/Sud-Est) : Avantage compétitif**
- SP → RS/PR/SC : 8-12 jours
- Satisfaction élevée → vendeurs Olist dominent sur reviews
- **65% de notes 5 étoiles** sur ces routes

**Routes longues (SP → Nord/Nord-Est) : Désavantage compétitif**
- SP → PA/AM/RR : 25-35 jours
- Satisfaction désastreuse → **vendeurs Olist pénalisés** vs concurrence locale
- **Seulement 25% de notes 5 étoiles** sur ces routes

**Absence de hubs régionaux**  
- Aucun état ne joue un rôle de redistribution régionale
- Toutes les commandes passent par SP = goulot d'étranglement

**Recommandation data-driven** :  
Analyser coût/bénéfice de **hubs secondaires** (RS pour le Sud, BA pour le Nord-Est) :
- Impact estimé : Délais -40% sur routes critiques
- Conséquence : +20-25% de clients 5 étoiles dans ces régions
- **ROI business** : Vendeurs Olist deviennent compétitifs partout au Brésil (vs actuellement seulement Sud/Sud-Est)

**Insight clé** : Les routes logistiques créent un **avantage compétitif** (Sud) ou un **handicap** (Nord) pour les vendeurs Olist.
"""

# Textes page Clients - Focus Expérience One-Shot
intro_clients = """
**Analyse des comportements clients dans l'écosystème Olist (2016-2018).**  

Cette section analyse les patterns d'achat des consommateurs finaux qui achètent via les vendeurs utilisant la plateforme Olist. Comprendre ces comportements aide Olist à :
- Optimiser ses services B2B pour ses clients vendeurs
- Identifier les opportunités d'amélioration de l'expérience
- Développer de nouveaux outils pour l'écosystème

**Insight clé : 97% des clients n'achètent qu'une fois**  
Cette caractéristique structurelle du marché brésilien e-commerce influence la stratégie d'Olist : focus sur l'excellence de la première expérience plutôt que sur la fidélisation.

Cette page analyse :
- Le profil des **clients très satisfaits** (5 étoiles) vs **insatisfaits** (<3 étoiles)
- Les catégories qui génèrent la **meilleure première expérience**
- L'impact du **délai de livraison** sur la probabilité de recommandation
- Les opportunités de **viralité** et de **bouche-à-oreille**
"""

insight_categories_acquisition = """
**Ces catégories créent les meilleures premières impressions**  
Si l'expérience est parfaite sur ces produits, les clients deviennent des prescripteurs naturels auprès de leur entourage.
"""

insight_mauvaises_experiences = """
**Zones à risque : une mauvaise première expérience tue toute recommandation**  
Ces catégories nécessitent une action urgente pour éviter le bouche-à-oreille négatif.
"""

insight_impact_delai = """
**Le délai est le facteur #1 de satisfaction sur une première commande**  
Livraison rapide (<7j) = 65% de notes 5 étoiles  
Livraison lente (>20j) = 25% de notes 5 étoiles  
**Impact direct sur la viralité potentielle**
"""

recommandations_clients = """
### **1. Garantir une expérience 5 étoiles sur la première commande**  
- Emballage premium  
- Note manuscrite personnalisée  
- Échantillon gratuit surprise  
- Suivi proactif de livraison  

### **2. Programme de parrainage agressif**  
Offrir **R$ 50** pour chaque ami parrainé (coût acquisition < valeur panier moyen)

### **3. Timing optimal pour demande d'avis**  
Envoyer la demande **48h après livraison réussie**, moment de satisfaction maximale

### **4. Incentives au partage social**  
- Réduction 10% sur prochain achat si partage Instagram/Facebook  
- Concours photos produits avec récompenses  

### **5. Transformer clients 5 étoiles en créateurs de contenu**  
- Programme ambassadeurs  
- Reviews détaillées récompensées  
- UGC (User Generated Content) pour marketing  

### **Objectif mesurable : Croissance organique via viralité**  
**Cible** : Atteindre **20% de croissance organique** (clients acquis via recommandations) dans les 12 prochains mois.

**Métriques de suivi** :  
- % nouveaux clients avec code parrainage  
- Taux de partage social post-achat  
- Net Promoter Score (NPS) global  
- Volume de UGC généré mensuellement  

**Impact business** : Chaque point de % gagné en croissance organique réduit directement les coûts d'acquisition payants et améliore la profitabilité.
"""

# Textes page Recommandations - Approche Data Analyst
intro_recommandations = """
## 🎯 Recommandations pour Optimiser l'Écosystème Olist

**Constat principal** : L'analyse révèle des leviers d'amélioration pour la plateforme B2B Olist.

**Approche recommandée** : Utiliser ces insights pour améliorer les services proposés aux vendeurs et optimiser l'écosystème global.

Cette page présente les **recommandations basées sur l'analyse des données**, classées par **impact potentiel** et **faisabilité** pour Olist en tant qu'entreprise B2B.
"""

# Section Logistique - Approche Data Analyst
reco_logistique_problemes = """
**Corrélation délai-satisfaction identifiée**
- Livraison <7j : **65%** de notes 5 étoiles
- Livraison 7-14j : **55%** de notes 5 étoiles
- Livraison 15-20j : **40%** de notes 5 étoiles
- Livraison >20j : **25%** de notes 5 étoiles

**Zones problématiques**
- Routes SP → Nord : délais moyens >25 jours
- **35%** de mauvaises reviews (≤3 étoiles) au-delà de 20 jours
- États concernés : PA, AM, RR, AP

**Impact estimé**
- Réduire délais de 10 jours → gain potentiel de **+15-20% de notes 5 étoiles**
"""

reco_logistique_actions = """
### Leviers identifiés (par ordre d'impact)

**1. Prioriser les catégories à fort volume**
- Health & Beauty, Gifts, Sports : 40% du volume total
- Impact direct sur perception globale de la marketplace
- **Métrique de suivi** : % commandes livrées <7j par catégorie

**2. Cibler les routes critiques**
- SP → Nord représente 15% des retards
- Analyser faisabilité hubs régionaux (RS, BA, RJ)
- **Métrique de suivi** : Délai moyen par route géographique

**3. Transparence délais**
- Afficher délai estimé AVANT achat
- Éviter déceptions = améliorer perception
- **Métrique de suivi** : Écart délai annoncé vs réel

**4. Communication proactive**
- Corrélation observée : mises à jour fréquentes → meilleure tolérance aux retards
- **Métrique de suivi** : Taux d'engagement notifications livraison
"""

# Section Produits - Approche Data Analyst
reco_produits_problemes = """
**Catégories à risque identifiées**
- Office furniture : 3.49/5 (note la plus basse)
- Audio, construction_tools : <3.6/5 avec volume significatif
- **25%** de notes ≤2 étoiles sur ces catégories

**Catégories performantes**
- Health & Beauty : 4.2/5, 15K+ ventes
- Gifts : 4.1/5, fort engagement
- Sports & Leisure : 4.0/5, croissance régulière

**Observation clé**
Corrélation entre note catégorie et propension au rachat plus forte que prévu (r=0.68)
"""

reco_produits_actions = """
### Leviers identifiés (par ordre d'impact)

**1. Analyser causes notes faibles catégories problématiques**
- Extraire mots-clés reviews négatives (NLP)
- Identifier si problème = qualité, description, délai, ou prix
- **Métrique de suivi** : Distribution notes par sous-catégorie

**2. Focus qualité sur catégories à fort volume**
- Health & Beauty, Gifts : représentent 40% CA
- Impact disproportionné sur réputation globale
- **Métrique de suivi** : % produits <3.5/5 retirés

**3. Segmentation catégories par profil**
- "Acquisiteurs" : attirent nouveaux clients (high visibility)
- "Fidélisateurs" : génèrent satisfaction (low return rate)
- "Problématiques" : notes faibles récurrentes
- **Métrique de suivi** : Taux conversion par type catégorie

**4. Transparence description produit**
- Hypothèse : écart attente/réalité explique 40% des mauvaises notes
- Tester descriptions enrichies sur échantillon
- **Métrique de suivi** : Taux retour vs qualité description
"""

# Section Géographie - Approche Data Analyst
reco_geo_constat = """
**Disparités géographiques observées**
- **Sud (RS, PR, SC)** : Délais moyens 12j, notes 4.3/5, panier R$ 165
- **Nord (PA, AM)** : Délais moyens 28j, notes 3.8/5, panier R$ 140
- **SP/RJ/MG** : 70% du CA total (concentration forte)

**Opportunités sous-exploitées**
- Sud : infrastructure performante, population connectée, faible pénétration
- Nord-Est (BA, PE) : population dense, délais intermédiaires (18j)
"""

reco_geo_actions = """
### Leviers identifiés (par ordre d'impact)

**1. Analyse coût-bénéfice expansion régionale**
- Simuler impact hubs secondaires (RS, BA) sur délais
- Estimer volume additionnel vs coûts logistiques
- **Métrique de suivi** : Coût/commande par région
- Livraison express systématique
- Si succès : déploiement national

**2. Segmentation par performance géographique**
- Cluster états selon délai/satisfaction/volume
- Identifier "quick wins" (bon délai + faible pénétration)
- **Métrique de suivi** : Taux croissance par cluster

**3. Transparence délais par région**
- Afficher délai moyen estimé AVANT achat (par état destination)
- Réduire gap attente/réalité = améliorer perception
- **Métrique de suivi** : Écart délai annoncé vs réel par région

**4. Test A/B campagnes géolocalisées**
- Comparer performance ads génériques vs localisées
- Mesurer CAC et conversion par région
- **Métrique de suivi** : ROI campagnes par état
"""

# Section Clients - Approche Data Analyst
reco_clients_observations = """
**Pattern one-shot confirmé : 97% des clients**

**Hypothèses explorées**
- Nature marketplace (achats ponctuels, événements, cadeaux)
- Faible récurrence naturelle produits généralistes
- Contraintes budget clients brésiliens

**Corrélations observées**
- Satisfaction 1ère commande fortement corrélée à intention rachat (r=0.72)
- Délai <7j → 3x plus de probabilité note 5 étoiles
- Clients 5 étoiles ont taux recommandation estimé 3-4x supérieur
"""

reco_clients_actions = """
### Leviers identifiés (par ordre d'impact)

**1. Optimiser expérience première commande**
- Focus absolu sur satisfaction initiale
- Tester améliorations packaging sur échantillon
- **Métrique de suivi** : % notes 5 étoiles sur 1ère commande

**2. Analyser drivers satisfaction par segment**
- Segmenter clients par : catégorie achetée, région, panier
- Identifier facteurs clés satisfaction par segment
- **Métrique de suivi** : Satisfaction score par segment

**3. Quantifier potentiel bouche-à-oreille**
- Estimer NPS (Net Promoter Score) actuel
- Modéliser impact +10% notes 5 étoiles sur croissance organique
- **Métrique de suivi** : % nouveaux clients "référés" (source acquisition)

**4. Tester mécanismes engagement post-achat**
- A/B test : timing demande avis (24h vs 48h vs 72h)
- A/B test : incentives reviews (avec vs sans récompense)
- **Métrique de suivi** : Taux réponse et qualité reviews

**5. Benchmark modèles one-shot réussis**
- Comparer avec autres marketplaces événementielles
- Identifier best practices acquisition/viralité
- **Métrique de suivi** : CAC vs LTV par canal
"""

# Section Priorités - Approche Data Analyst
reco_priorites = """
## Leviers Prioritaires (Classement par Impact Estimé)

### **Priorité 1 : Réduire les délais de livraison**
**Pourquoi** : Corrélation la plus forte avec satisfaction (r=0.76)  
**Impact estimé** : -10 jours délai → +15-20% notes 5 étoiles  
**Métriques** : % commandes <7j, délai moyen par route, écart estimé/réel

### **Priorité 2 : Améliorer catégories problématiques**
**Pourquoi** : 25% notes négatives = frein réputation globale  
**Impact estimé** : Retrait produits <3.5 → +5-8% satisfaction globale  
**Métriques** : Distribution notes par catégorie, % produits audités

### **Priorité 3 : Optimiser expérience première commande**
**Pourquoi** : 97% one-shot = une seule chance de bien faire  
**Impact estimé** : +10% notes 5 étoiles 1ère commande → +3-5% croissance organique  
**Métriques** : % 5 étoiles 1ère commande, taux recommandation, NPS

### **Priorité 4 : Expansion géographique ciblée**
**Pourquoi** : Sud sous-exploité (bons délais + faible pénétration)  
**Impact estimé** : Focus RS/PR/SC → +15-20% volume dans ces états  
**Métriques** : Volume par état, part de marché régionale, CAC régional

### **Priorité 5 : Transparence et communication**
**Pourquoi** : Gap attente/réalité explique 30-40% insatisfaction  
**Impact estimé** : Délais affichés précis → -20% reviews négatives délai  
**Métriques** : Écart délai annoncé/réel, mentions "retard" dans reviews
"""

reco_conclusion = """
## Synthèse de l'Analyse

**Constat principal** : Le modèle one-shot (97%) n'est pas un bug, c'est une feature.

**Recommandation stratégique** : Optimiser pour l'excellence de l'expérience unique plutôt que forcer la fidélisation.

**Leviers à impact rapide** :
1. Délais de livraison (corrélation r=0.76 avec satisfaction)
2. Qualité catégories (25% notes négatives concentrées sur 10% produits)
3. Transparence communication (40% insatisfaction évitable)

**Métriques de succès recommandées** :
- % clients 5 étoiles (objectif 65% vs 55% actuel)
- % livraisons <7j (objectif 50% vs 30% actuel)
- NPS par catégorie (baseline à établir)
- % croissance organique (source "recommandation")

Les décisions d'implémentation (roadmap, budget, ressources) relèvent du management et de la stratégie produit.
"""

# ===========================
# TEXTES PAGE PRODUITS
# ===========================

intro_produits = """
**Analyse des performances produits dans l'écosystème Olist pour optimiser le service B2B.**

Cette section étudie les catégories de produits qui transitent par la plateforme Olist pour identifier :
- Les catégories les plus performantes en satisfaction client
- Les opportunités d'amélioration de l'expérience par catégorie  
- Les insights pour aider Olist à mieux conseiller ses clients vendeurs
- Les leviers d'optimisation de l'écosystème par segment produit

**Objectif** : Fournir des données actionnables à Olist pour améliorer ses services B2B et l'expérience globale de l'écosystème.
"""

analyse_categories_championnes = """
### Insights clés : Les catégories qui créent un avantage compétitif

**% de 5 étoiles = indicateur de compétitivité vendeurs**  
Les catégories avec >60% de 5 étoiles donnent aux vendeurs Olist une position dominante sur les marketplaces. Ces produits génèrent des reviews qui battent la concurrence.

**Expérience parfaite reproductible**  
Ces catégories réussissent le triptyque : qualité produit + description fidèle + livraison rapide. Elles prouvent qu'une domination reviews est possible.

**Levier stratégique**  
Recruter des vendeurs dans ces catégories = garantir leur succès commercial dès le départ. Chaque vente renforce leur position concurrentielle.

**Levier stratégique**  
Concentrer l'acquisition sur ces catégories maximise la probabilité de créer des ambassadeurs dès le premier achat. Chaque vente devient un investissement dans la réputation.
"""

analyse_categories_a_risque = """
### Insights clés : Les générateurs de détracteurs

**Faible % de 5 étoiles = risque viral négatif**  
Les catégories avec <40% de 5 étoiles créent majoritairement des expériences décevantes. Chaque vente dans ces catégories risque de générer du bouche-à-oreille négatif.

**Impact multiplicateur du négatif**  
Un client déçu partage son expérience 2 à 3 fois plus qu'un client satisfait. Ces catégories sabotent activement la croissance organique.

**Urgence d'intervention**  
Tant que ces catégories restent problématiques, elles annulent les efforts des catégories championnes. Améliorer ou retirer ces produits devient prioritaire.
"""

analyse_impact_delais_produits = """
### Insights clés : Le délai comme déterminant de la première impression

**Corrélation délai/ambassadeurs**  
Les catégories avec délais >15 jours ont systématiquement un % de 5 étoiles plus faible. L'attente érode la satisfaction, même si le produit est correct.

**Catégories handicapées par la logistique**  
Certaines catégories (meubles, électroménager) subissent des contraintes structurelles. Sans optimisation logistique, elles ne pourront jamais créer d'ambassadeurs.

**Opportunité d'amélioration rapide**  
Réduire les délais de 3-5 jours sur les catégories à 12-15 jours peut augmenter le % de 5 étoiles de 10-15 points → conversion massive vers ambassadeurs.
"""

analyse_recommandations_produits = """
### Recommandations Data-Driven

**1. Prioriser l'acquisition sur les catégories championnes**  
→ **Impact** : Maximise le ratio ambassadeurs/détracteurs dès le premier achat  
→ **Métriques** : Tracker % nouvelles commandes sur catégories >60% de 5 étoiles

**2. Audit urgent des catégories à risque**  
→ **Impact** : Stopper la génération de détracteurs  
→ **Métriques** : Réduire volume ou améliorer jusqu'à atteindre >50% de 5 étoiles

**3. Optimisation logistique ciblée**  
→ **Impact** : Transformer catégories moyennes en championnes via réduction délais  
→ **Métriques** : Viser <10 jours sur toutes catégories avec potentiel commercial

**4. Test A/B : Retrait temporaire catégories toxiques**  
→ **Impact** : Mesurer l'effet sur la réputation globale et le taux de recommandation  
→ **Métriques** : Comparer Net Promoter Score avant/après

Ces actions visent à augmenter le % global de 5 étoiles → accélération de la croissance organique via bouche-à-oreille.
"""
