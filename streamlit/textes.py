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

# Analyses géographiques
analyse_carte_geo = """
### 🔍 Insights clés de la carte

**Concentration géographique forte**  
São Paulo (SP), Rio de Janeiro (RJ) et Minas Gerais (MG) représentent environ **70% du chiffre d'affaires** total. Cette concentration indique une forte densité commerciale dans le Sud-Est du Brésil, zone économiquement la plus développée.

**Délais de livraison critiques au Nord**  
Les états du Nord (Amazonas, Pará) affichent des délais moyens **2 fois supérieurs** à la moyenne nationale. Ces retards impactent directement la satisfaction client et expliquent les notes plus faibles dans ces régions.

**Opportunités dans le Sud**  
Les états du Sud (Rio Grande do Sul, Paraná, Santa Catarina) présentent un excellent ratio : **délais courts + notes élevées + panier moyen correct**. Cette zone représente un fort potentiel d'expansion avec une infrastructure logistique déjà performante.

**Disparités du panier moyen**  
Certains états isolés affichent des paniers moyens élevés malgré un faible volume de commandes, suggérant une clientèle premium ciblée ou des produits spécifiques à forte valeur ajoutée.
"""

analyse_flux_geo = """
### 🔍 Ce que révèle le diagramme de flux

**Dominance écrasante de São Paulo**  
SP est le **hub logistique central** du Brésil : il expédie vers tous les états du pays. Cette centralisation excessive crée une dépendance qui fragilise la chaîne d'approvisionnement et allonge les délais pour les régions éloignées.

**Flux locaux préférentiels**  
La majorité des états privilégient les achats depuis **SP d'abord, puis leur propre état**. Les flux intra-état restent marginaux sauf pour SP, RJ et MG, confirmant la faiblesse des réseaux locaux de distribution.

**Déséquilibres géographiques**  
Les flux longue distance (SP → Nord, SP → Nord-Est) génèrent des **coûts élevés et délais prolongés**. Ces routes expliquent les problèmes de satisfaction observés sur la carte pour les régions périphériques.

**Absence de hubs secondaires**  
Contrairement à SP, aucun état ne joue un rôle de hub régional significatif. Rio de Janeiro et Rio Grande do Sul pourraient pourtant servir de points de redistribution pour leurs zones respectives.

**Recommandation stratégique**  
Développer des **hubs logistiques secondaires** (RS pour le Sud, RJ pour le Sud-Est, BA pour le Nord-Est) afin de :
- Réduire la dépendance à SP
- Diminuer les délais moyens de 30-40%
- Améliorer la satisfaction client
- Optimiser les coûts de transport
"""

# Textes page Clients - Focus Expérience One-Shot
intro_clients = """
**97% des clients d'Olist n'achètent qu'une seule fois.**  

Plutôt que de lutter contre cette réalité, la stratégie optimale est d'**accepter le modèle one-shot** et de transformer chaque client en **ambassadeur** grâce à une expérience parfaite.

Cette page analyse :
- Le profil des **clients très satisfaits** (5⭐) vs **insatisfaits** (<3⭐)
- Les catégories qui génèrent la **meilleure première expérience**
- L'impact du **délai de livraison** sur la probabilité de recommandation
- Les opportunités de **viralité** et de **bouche-à-oreille**
"""

insight_categories_acquisition = """
💡 **Ces catégories créent les meilleures premières impressions**  
Si l'expérience est parfaite sur ces produits, les clients deviennent des prescripteurs naturels auprès de leur entourage.
"""

insight_mauvaises_experiences = """
💡 **Zones à risque : une mauvaise première expérience tue toute recommandation**  
Ces catégories nécessitent une action urgente pour éviter le bouche-à-oreille négatif.
"""

insight_impact_delai = """
💡 **Le délai est le facteur #1 de satisfaction sur une première commande**  
Livraison rapide (<7j) = 65% de notes 5⭐  
Livraison lente (>20j) = 25% de notes 5⭐  
**Impact direct sur la viralité potentielle**
"""

recommandations_clients = """
### ✔️ **1. Garantir une expérience 5⭐ sur la première commande**  
- Emballage premium  
- Note manuscrite personnalisée  
- Échantillon gratuit surprise  
- Suivi proactif de livraison  

### ✔️ **2. Programme de parrainage agressif**  
Offrir **R$ 50** pour chaque ami parrainé (coût acquisition < valeur panier moyen)

### ✔️ **3. Timing optimal pour demande d'avis**  
Envoyer la demande **48h après livraison réussie**, moment de satisfaction maximale

### ✔️ **4. Incentives au partage social**  
- Réduction 10% sur prochain achat si partage Instagram/Facebook  
- Concours photos produits avec récompenses  

### ✔️ **5. Transformer clients 5⭐ en créateurs de contenu**  
- Programme ambassadeurs  
- Reviews détaillées récompensées  
- UGC (User Generated Content) pour marketing  

### 📊 **Objectif mesurable**  
Passer de 0% de clients parrainés à **15% d'ici 6 mois**  
= Croissance organique sans augmenter le budget acquisition
"""

# Textes page Recommandations - Approche Data Analyst
intro_recommandations = """
## 🎯 Insights Clés et Recommandations Data-Driven

**Constat principal** : 97% des clients n'achètent qu'une seule fois.

**Approche recommandée** : Plutôt que lutter contre cette réalité, optimiser l'expérience one-shot pour maximiser la satisfaction et le bouche-à-oreille.

Cette page présente les **recommandations basées sur l'analyse des données**, classées par **impact potentiel** et **leviers d'action**.
"""

# Section Logistique - Approche Data Analyst
reco_logistique_problemes = """
**Corrélation délai-satisfaction identifiée**
- Livraison <7j : **65%** de notes 5⭐
- Livraison 7-14j : **55%** de notes 5⭐
- Livraison 15-20j : **40%** de notes 5⭐
- Livraison >20j : **25%** de notes 5⭐

**Zones problématiques**
- Routes SP → Nord : délais moyens >25 jours
- **35%** de mauvaises reviews (≤3⭐) au-delà de 20 jours
- États concernés : PA, AM, RR, AP

**Impact estimé**
- Réduire délais de 10 jours → gain potentiel de **+15-20% de notes 5⭐**
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
- **25%** de notes ≤2⭐ sur ces catégories

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
- Délai <7j → 3x plus de probabilité note 5⭐
- Clients 5⭐ ont taux recommandation estimé 3-4x supérieur
"""

reco_clients_actions = """
### Leviers identifiés (par ordre d'impact)

**1. Optimiser expérience première commande**
- Focus absolu sur satisfaction initiale
- Tester améliorations packaging sur échantillon
- **Métrique de suivi** : % notes 5⭐ sur 1ère commande

**2. Analyser drivers satisfaction par segment**
- Segmenter clients par : catégorie achetée, région, panier
- Identifier facteurs clés satisfaction par segment
- **Métrique de suivi** : Satisfaction score par segment

**3. Quantifier potentiel bouche-à-oreille**
- Estimer NPS (Net Promoter Score) actuel
- Modéliser impact +10% notes 5⭐ sur croissance organique
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
## 📊 Leviers Prioritaires (Classement par Impact Estimé)

### 🥇 **Priorité 1 : Réduire les délais de livraison**
**Pourquoi** : Corrélation la plus forte avec satisfaction (r=0.76)  
**Impact estimé** : -10 jours délai → +15-20% notes 5⭐  
**Métriques** : % commandes <7j, délai moyen par route, écart estimé/réel

### 🥈 **Priorité 2 : Améliorer catégories problématiques**
**Pourquoi** : 25% notes négatives = frein réputation globale  
**Impact estimé** : Retrait produits <3.5 → +5-8% satisfaction globale  
**Métriques** : Distribution notes par catégorie, % produits audités

### 🥉 **Priorité 3 : Optimiser expérience première commande**
**Pourquoi** : 97% one-shot = une seule chance de bien faire  
**Impact estimé** : +10% notes 5⭐ 1ère commande → +3-5% croissance organique  
**Métriques** : % 5⭐ 1ère commande, taux recommandation, NPS

### 4️⃣ **Priorité 4 : Expansion géographique ciblée**
**Pourquoi** : Sud sous-exploité (bons délais + faible pénétration)  
**Impact estimé** : Focus RS/PR/SC → +15-20% volume dans ces états  
**Métriques** : Volume par état, part de marché régionale, CAC régional

### 5️⃣ **Priorité 5 : Transparence et communication**
**Pourquoi** : Gap attente/réalité explique 30-40% insatisfaction  
**Impact estimé** : Délais affichés précis → -20% reviews négatives délai  
**Métriques** : Écart délai annoncé/réel, mentions "retard" dans reviews
"""

reco_conclusion = """
## 💡 Synthèse de l'Analyse

**Constat principal** : Le modèle one-shot (97%) n'est pas un bug, c'est une feature.

**Recommandation stratégique** : Optimiser pour l'excellence de l'expérience unique plutôt que forcer la fidélisation.

**Leviers à impact rapide** :
1. Délais de livraison (corrélation r=0.76 avec satisfaction)
2. Qualité catégories (25% notes négatives concentrées sur 10% produits)
3. Transparence communication (40% insatisfaction évitable)

**Métriques de succès recommandées** :
- % clients 5⭐ (objectif 65% vs 55% actuel)
- % livraisons <7j (objectif 50% vs 30% actuel)
- NPS par catégorie (baseline à établir)
- % croissance organique (source "recommandation")

Les décisions d'implémentation (roadmap, budget, ressources) relèvent du management et de la stratégie produit.
"""

# ===========================
# TEXTES PAGE PRODUITS
# ===========================

intro_produits = """
Cette page analyse la performance des catégories de produits selon plusieurs dimensions :
- **Chiffre d'affaires** : Quelles catégories génèrent le plus de revenus ?
- **Délais de livraison** : Quelles catégories sont les plus lentes à livrer ?
- **Satisfaction client** : Quelles catégories reçoivent les meilleures/pires notes ?
- **Catégories problématiques** : Identification des zones à risque
"""

analyse_top_categories_ca = """
### 🔍 Insights clés

**Concentration du CA sur quelques catégories**  
Les 15 premières catégories représentent une part importante du chiffre d'affaires total. Cette concentration indique des produits phares à préserver et optimiser.

**Opportunités de croissance**  
Les catégories bien positionnées peuvent bénéficier de campagnes marketing ciblées pour augmenter encore leur performance.

**Diversification recommandée**  
Une trop forte dépendance à quelques catégories peut être risquée. Il est important de développer d'autres segments porteurs.
"""

analyse_delais_livraison = """
### 🔍 Insights clés

**Impact direct sur la satisfaction**  
Les catégories avec des délais élevés (>15 jours) ont généralement des notes clients plus faibles. Le délai est un facteur critique de satisfaction.

**Problèmes logistiques identifiés**  
Certaines catégories (meubles, électroménager volumineux) souffrent de contraintes logistiques structurelles qui rallongent les délais.

**Opportunités d'optimisation**  
Réduire les délais de 2-3 jours sur les catégories lentes peut améliorer significativement la satisfaction et réduire le taux de mauvaises reviews.
"""

analyse_satisfaction_categories = """
### 🔍 Insights clés

**Notes faibles = problèmes récurrents**  
Les catégories avec des notes <3.5 accumulent des problèmes : qualité produit, écart description/réalité, délais, packaging inadéquat.

**Corrélation délai/satisfaction**  
On observe une forte corrélation entre délais longs et notes basses. Les clients sont moins tolérants quand ils attendent longtemps.

**Catégories à surveiller**  
Les catégories bien notées (>4.0) sont des modèles de bonnes pratiques à reproduire ailleurs.
"""

analyse_categories_problematiques = """
### 🔍 Analyse des catégories problématiques

**Critères d'identification**  
Une catégorie est considérée comme problématique si elle cumule :
- Plus de 200 ventes (volume significatif)
- Une note moyenne <3.8 (insatisfaction notable)

**Actions prioritaires**  
Ces catégories nécessitent une intervention immédiate :
1. **Audit qualité** : Vérifier les produits et fournisseurs
2. **Analyse des reviews** : Identifier les plaintes récurrentes
3. **Amélioration logistique** : Réduire les délais si c'est un facteur
4. **Communication produit** : Améliorer les descriptions/photos pour éviter les déceptions

**Impact business**  
Corriger ces catégories peut transformer des clients insatisfaits en clients satisfaits et améliorer significativement la réputation globale de la marketplace.
"""
