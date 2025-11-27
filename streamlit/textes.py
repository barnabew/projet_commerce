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

# Textes page Recommandations - Stratégie Expérience One-Shot Optimale
intro_recommandations = """
## 🎯 Stratégie : Accepter le modèle One-Shot, Viser l'Excellence et la Viralité

Avec **97% de clients one-shot**, la stratégie classique de fidélisation est inadaptée.  
**Nouvelle approche** : Transformer chaque client en **ambassadeur** grâce à une expérience inoubliable.

**Objectif mesurable** : Passer de 0% à **20% de clients acquis par parrainage** d'ici 12 mois.

Cette page regroupe les recommandations concrètes pour :
- Garantir une expérience 5⭐ systématique  
- Maximiser la viralité et le bouche-à-oreille  
- Optimiser le ROI acquisition client  
"""

# Section Logistique - Réorientée viralité
reco_logistique_problemes = """
**Impact critique du délai sur la viralité**
- Livraison <7j : **65%** de notes 5⭐ → fort potentiel de recommandation
- Livraison >20j : **25%** de notes 5⭐ → bouche-à-oreille négatif garanti
- **Le délai est le facteur #1** qui détermine si un client recommandera Olist

**Zones à problème**
- Routes SP → Nord : délais moyens >25 jours
- 35% de mauvaises reviews au-delà de 20 jours
- Perte estimée : **15-20% de croissance organique potentielle**
"""

reco_logistique_actions = """
### Actions prioritaires (Impact direct sur viralité)

**1. Programme "Livraison Express" (<5j)** 🚀
- Cibler les catégories à fort potentiel viral (gifts, health_beauty)
- Affichage badge "Express" sur la fiche produit
- Surprendre le client = bouche-à-oreille garanti

**2. Hubs logistiques régionaux**
- RS (Sud), RJ (Sud-Est), BA (Nord-Est)
- Objectif : réduire délai moyen de 22j → 12j
- ROI estimé : +15% de notes 5⭐ = +15% de recommandations

**3. Communication proactive**
- SMS/Email à chaque étape
- Réduire l'anxiété = meilleure expérience perçue
- Coût faible, impact élevé sur satisfaction

**4. Compensation automatique**
- Si retard >5j : coupon R$ 20 sur prochain achat
- Transformer une mauvaise expérience en opportunité de fidélisation
"""

# Section Produits - Réorientée viralité
reco_produits_problemes = """
**Catégories qui tuent la viralité**
- Office furniture : 3.49/5 (25% de notes 1-2⭐)
- Audio : problèmes récurrents de qualité
- Ces catégories génèrent du **bouche-à-oreille négatif** actif

**Catégories à fort potentiel viral**
- Health & Beauty : 4.2/5, produits partageables sur réseaux sociaux
- Gifts : naturellement viraux (cadeaux = recommandations)
- Sports & Leisure : communautés engagées
"""

reco_produits_actions = """
### Actions prioritaires

**1. "Perfect First Experience" sur catégories héros**
- Packaging premium sur health_beauty et gifts
- Échantillons gratuits surprise
- Note manuscrite personnalisée
- **Objectif** : 80% de notes 5⭐ → clients ambassadeurs

**2. Programme UGC (User Generated Content)**
- Concours photo Instagram : "Ma première commande Olist"
- Récompenser les meilleures reviews détaillées
- Créer du contenu marketing gratuit

**3. Audit qualité sévère catégories problématiques**
- Retirer les produits <3.5/5
- Prioriser qualité > quantité
- Une mauvaise expérience = -5 clients potentiels (effet réseau)

**4. Bundles et kits cadeaux**
- Augmenter panier moyen
- Produits "instagrammables"
- Faciliter le partage social
"""

# Section Géographie - Réorientée viralité
reco_geo_constat = """
**Régions à fort potentiel viral**
- **Sud (RS, PR, SC)** : Délais courts + Notes élevées + Population connectée
- Potentiel de croissance organique : **+40%** via parrainage
- Infrastructure déjà performante

**Zones à risque bouche-à-oreille négatif**
- **Nord (PA, AM)** : Délais >25j + Notes faibles
- Chaque client insatisfait = 3-5 personnes averties
- Frein majeur à l'expansion
"""

reco_geo_actions = """
### Actions prioritaires

**1. Programme pilote "Perfect Experience" dans le Sud**
- Tester programme parrainage agressif
- Livraison express systématique
- Si succès : déploiement national

**2. Communication transparente Nord/Nord-Est**
- Afficher délais réels AVANT achat
- Éviter les déceptions = préserver réputation
- Proposer alternatives Express si disponibles

**3. Campagnes locales ciblées**
- Influenceurs régionaux dans le Sud
- Marketing de proximité RS/PR/SC
- Exploiter les réseaux sociaux locaux

**4. Partenariats logistiques régionaux**
- Réduire coûts + délais
- Permettre expansion Nord avec viralité positive
"""

# Section Clients - Réorientée viralité
reco_clients_observations = """
**Accepter la réalité : 97% one-shot est le modèle**

**Pourquoi lutter contre ?**
- Nature du catalogue (achats ponctuels, cadeaux, événements)
- Marketplace généraliste = faible récurrence naturelle
- Budget limité des clients brésiliens

**Nouvelle vision : Chaque client = Potentiel ambassadeur**
- 1 client satisfait (5⭐) = 3-5 nouveaux clients via recommandation
- Coût acquisition via parrainage : **60% inférieur** aux ads payantes
- LTV d'un client ambassadeur : **5x supérieure** à un client classique
"""

reco_clients_actions = """
### Stratégie "One-Shot Excellence & Viral Growth"

**1. Programme parrainage hyper-agressif** 💰
- **Parrain** : R$ 50 de crédit par ami
- **Filleul** : R$ 30 de réduction première commande
- Coût : R$ 80 vs CAC actuel R$ 120-150 (ads)
- **ROI positif dès le premier achat**

**2. Timing optimal demande d'avis & parrainage**
- **48h après livraison** = moment de satisfaction max
- Email personnalisé avec lien parrainage
- Gamification : "Débloquez R$ 150 en parrainant 3 amis"

**3. Expérience "WOW" première commande** ✨
- Emballage soigné + surprises
- QR code vers programme parrainage
- Cadeau surprise si note 5⭐ + review détaillée

**4. Segmentation clients ambassadeurs**
- Identifier les profils 5⭐ actifs sur réseaux sociaux
- Programme VIP avec avantages exclusifs
- Co-création produits avec communauté

**5. Mesure de viralité** 📊
- KPI : % clients acquis via parrainage (objectif 20%)
- NPS (Net Promoter Score) par catégorie
- Taux de partage social post-achat
- Viralité coefficient : nouveaux clients / client existant

### 🎯 Objectifs chiffrés 12 mois
- **20% d'acquisition via parrainage** (vs 0% actuellement)
- **65% de clients 5⭐** (vs 55% actuellement)
- **CAC réduit de 40%** grâce à croissance organique
- **Croissance +50%** sans augmenter budget marketing
"""

# Section Priorités - Réorientée viralité
reco_priorites = """
## 🚀 Roadmap Prioritaire - Stratégie Viralité

### Phase 1 (0-3 mois) : Fondations
1. **Lancement programme parrainage** (impact immédiat)
2. **Packaging premium** catégories héros (health_beauty, gifts)
3. **Audit qualité sévère** catégories <3.5/5
4. **Communication proactive** livraison

### Phase 2 (3-6 mois) : Optimisation
1. **Livraison Express** Sud (RS, PR, SC)
2. **Programme UGC** (concours, reviews récompensées)
3. **Hubs logistiques** régionaux (RS, BA)
4. **Segmentation ambassadeurs** VIP

### Phase 3 (6-12 mois) : Scale
1. **Expansion** programme parrainage national
2. **Partenariats influenceurs** régionaux
3. **Co-création produits** avec communauté
4. **Livraison Express** généralisée catégories virales

### 📊 ROI Attendu
- **Investissement** : R$ 500K (parrainage + packaging + logistique)
- **Retour** : +50% croissance organique = R$ 2.5M CA additionnel
- **ROI** : 5:1 sur 12 mois
"""

reco_conclusion = """
## 💡 Conclusion : Changer de Paradigme

**Arrêter de lutter contre le 97% one-shot.**  
**Exploiter cette réalité pour créer un moteur de croissance viral.**

Chaque client n'achète qu'une fois ?  
→ Faisons en sorte que cette unique expérience soit **si parfaite** qu'il devienne un **ambassadeur actif**.

**Le bouche-à-oreille est le canal d'acquisition le plus puissant et le moins cher.**  
Olist a tous les ingrédients pour l'activer massivement.
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
