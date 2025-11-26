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

# Textes page Clients
intro_clients = """
Olist est un marketplace dominé par les **one-time buyers** (≈ 97%).  
L'objectif business n'est donc **pas la fidélisation**, mais la qualité de la **première expérience**.

Cette page analyse :
- les catégories qui **attirent** des nouveaux clients,
- celles qui **génèrent des mauvaises premières expériences**,
- l'impact du **délai de livraison** sur la satisfaction.
"""

insight_categories_acquisition = """
💡 *Ces catégories jouent un rôle clé dans l'acquisition : ce sont les produits les plus visibles, les plus attractifs ou les moins risqués.*
"""

insight_mauvaises_experiences = """
💡 *Une mauvaise première expérience = client perdu.  
Ces catégories nécessitent une action immédiate (qualité, logistique, description produit…)*  
"""

insight_impact_delai = """
💡 *Les nouveaux clients sont extrêmement sensibles au délai.  
Allonger la livraison augmente fortement le risque de non-retour.*  
"""

recommandations_clients = """
### ✔️ *1. Optimiser les catégories à fort taux de mauvaises reviews*  
Ce sont les produits qui font perdre le plus de clients dès le premier achat.

### ✔️ *2. Mettre en avant les catégories d'acquisition*  
Elles sont idéales pour publicité, SEO, campagnes d'accueil.

### ✔️ *3. Réduire les délais sur les premières commandes*  
Impact direct sur la satisfaction → augmente les chances de retour.

### ✔️ *4. Améliorer la transparence produit (photo, taille, description)*  
Souvent la vraie cause des bad reviews sur un premier achat.

### ✔️ *5. Ajouter un "suivi proactif" sur la première commande*  
Email, notifications → réduit l'anxiété → augmente la satisfaction.
"""

# Textes page Recommandations
intro_recommandations = """
Cette page regroupe les recommandations concrètes issues des analyses :
- Ventes & performance globale  
- Logistique & délais  
- Produits  
- Géographie  
- Comportement clients  
"""

# Section Logistique
reco_logistique_problemes = """
- Les délais > 10 jours font chuter significativement les notes (jusqu'à 3.2/5).  
- Le taux de **mauvaises reviews** dépasse **35%** au-delà de 20 jours.  
- Certaines routes logistiques, notamment **SP → Nord**, sont clairement plus lentes.
"""

reco_logistique_actions = """
- **Optimiser les routes critiques** : prioriser les flux SP → (PA, AM, RR, AP).  
- **Alerte automatique** sur commandes dépassant l'estimation initiale.  
- **Partenariats logistiques régionaux** dans le Nord/Nord-Est pour réduire 2–4 jours.  
- **Proposer un suivi plus transparent** pour réduire l'insatisfaction liée à l'attente.
"""

# Section Produits
reco_produits_problemes = """
- Quelques catégories génèrent des **notes très faibles** (ex : office furniture 3.49/5).  
- D'autres sont **à fort potentiel** : health_beauty, gifts, sports…  
- Le pricing + shipping impacte fortement la satisfaction dans certaines catégories.
"""

reco_produits_actions = """
- **Auditer les mauvaises catégories** (packaging, qualité, fournisseurs).  
- **Mettre en avant les catégories héro** dans campagnes marketing.  
- **Optimiser le pricing + shipping** pour les articles volumineux (mobilier).  
- **Créer des bundles** pour augmenter le panier moyen dans les catégories populaires.
"""

# Section Géographie
reco_geo_constat = """
- Le CA est très concentré : SP > RJ > MG.  
- Certaines régions ont un **panier moyen élevé** mais une faible base client (ex: Norte).  
- Les délais y sont souvent plus longs → impact direct sur les notes.
"""

reco_geo_actions = """
- **Campagnes ciblées** dans RS, PR, SC : bonnes notes et bons délais → potentiel d'expansion.  
- **Développer des hubs logistiques** dans NO/NE pour accélérer la livraison.  
- **Publicité géographique** : push sur les régions où la concurrence est faible.
"""

# Section Clients
reco_clients_observations = """
- **97% des clients sont "one-time buyers"** → problème majeur.  
- La récence n'est pas exploitable (données incomplètes).  
- Les clients qui dépensent le plus ne laissent pas forcément de meilleures notes.  
- Une hausse du montant (monetary) augmente la probabilité de mauvaise note.
"""

reco_clients_actions = """
- **Améliorer l'expérience du premier achat (critical !)**  
  - Page produit plus claire  
  - Photos + descriptions enrichies  
  - Garantie / retours simplifiés  

- **Réduire le nombre de mauvaises premières expériences** :  
  - Alertes logistiques  
  - Vérification fournisseur avant expédition  

- **Campagnes de retargeting uniquement pour les clients satisfaits**.

- **STRATÉGIE D'ACQUISITION plutôt que fidélisation** :  
  - Puisque presque tous les clients achètent une fois.  
  - Focus sur SEO, réseaux sociaux, ads produit.
"""

# Section Priorités
reco_priorites = """
### 1. Accélérer la livraison (levier n°1 pour améliorer la note client)
### 2. Améliorer la qualité des catégories problématiques (mobilier, audio…)
### 3. Investir dans l'acquisition : les clients reviennent très peu
### 4. Développer la logistique dans le Nord & Nord-Est
### 5. Mettre en avant les produits les plus performants en marketing
"""

reco_conclusion = "Cette page regroupe les recommandations les plus importantes pour orienter la stratégie business."
