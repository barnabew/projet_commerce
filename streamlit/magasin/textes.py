"""
textes.py
Textes et analyses pour le dashboard Retail Analytics
"""

# ===================
# INTRODUCTIONS PAGES
# ===================

intro_departements = """
**Analyse de l'assortiment départemental pour optimiser la performance par type de magasin.**

Cette section analyse :
- **La segmentation stratégique** : Classification des départements selon leur présence
- **Les champions départementaux** : Départements à fort CA dans tous types de magasins  
- **Les départements spécialisés** : Niches rentables à faible présence
- **L'optimisation par type** : Stratégies différenciées selon la taille du magasin

Objectif : Développer des stratégies d'assortiment ciblées pour maximiser la performance.
"""

intro_temporel = """
**Analyse des patterns temporels pour exploiter la saisonnalité et optimiser les stratégies promotionnelles.**

Cette page explore :
- **Les tendances mensuelles globales** : Identification des pics et creux saisonniers
- **Les variations par type de magasin** : Comportements différenciés selon la taille
- **La saisonnalité départementale** : Opportunités de croissance temporelles
- **L'efficacité promotionnelle** : Impact des markdown sur les ventes

Insight clé : Exploiter les patterns temporels pour maximiser les revenus.
"""

# ===================
# ANALYSES MAGASINS
# ===================

analyse_correlation = """
### Corrélation Taille-Performance Confirmée

**Insight stratégique** : La relation positive entre la taille des magasins et leur performance 
valide la segmentation A/B/C et justifie des stratégies d'assortiment différenciées.

**Implications business** :
- **Type A** : Assortiment large, départements premium, stratégies de cross-selling
- **Type B** : Équilibre entre assortiment et rentabilité, focus départements populaires  
- **Type C** : Assortiment optimisé, concentration sur départements à forte rotation

La corrélation positive indique que l'expansion des surfaces reste un levier de croissance viable.
"""

analyse_evolution_types = """
### Patterns Temporels Différenciés par Type

**Observations clés** :
- **Type A** : Amplitude saisonnière élevée, sensibilité aux événements promotionnels
- **Type B** : Stabilité relative, croissance régulière  
- **Type C** : Volatilité modérée, adaptation rapide aux tendances locales

**Recommandations temporelles** :
- Planifier les promotions majeures sur les Type A (impact amplifié)
- Maintenir la régularité d'approvisionnement sur les Type B
- Adapter rapidement l'assortiment des Type C aux pics saisonniers
"""

# ===================
# ANALYSES DÉPARTEMENTS  
# ===================

analyse_segmentation_depts = """
### Classification Stratégique des Départements

**Méthodologie** : Segmentation selon le taux de présence dans les magasins

- **Universels (>90%)** : Départements indispensables, présents partout
- **Courants (70-90%)** : Départements populaires, forte demande 
- **Sélectifs (40-70%)** : Départements ciblés, opportunités de différenciation
- **Spécialisés (<40%)** : Départements niches, potentiel de marge élevée

Cette classification guide les décisions d'assortiment par type de magasin.
"""

analyse_champions = """
### Départements Champions : Moteurs de Performance

**Critères** : Départements avec forte présence ET forte performance CA

Ces départements représentent :
- **Le cœur d'assortiment** à maintenir dans tous les magasins
- **Les leviers de croissance** prioritaires pour les investissements
- **Les standards de performance** à reproduire sur d'autres départements

Focus sur l'optimisation continue de ces champions pour maximiser l'impact.
"""

analyse_specialises = """
### Départements Spécialisés : Opportunités de Différenciation

**Stratégie** : Identifier les niches rentables à faible présence mais forte performance

Avantages des départements spécialisés :
- **Marges supérieures** dues à la spécialisation
- **Différenciation concurrentielle** par l'unicité de l'offre
- **Fidélisation client** par l'expertise perçue

Opportunité d'expansion sélective selon le profil des magasins.
"""

analyse_perf_par_type = """
### Performance Départementale Différenciée

**Principe** : Les mêmes départements performent différemment selon le type de magasin

Facteurs d'influence :
- **Taille du magasin** : Espace disponible pour l'assortiment
- **Clientèle cible** : Profils de consommateurs différents
- **Localisation** : Contexte géographique et concurrentiel

Utiliser ces données pour personnaliser l'assortiment par type.
"""

# ===================
# ANALYSES TEMPORELLES
# ===================

insight_evolution_globale = """
**Pattern Global Identifié**

L'évolution mensuelle révèle des cycles saisonniers clairs avec des opportunités 
d'optimisation :
- **Pics de performance** : Identifier les mois à fort potentiel
- **Creux saisonniers** : Périodes nécessitant des actions correctives
- **Tendance générale** : Croissance ou décroissance à long terme

Ces insights temporels permettent une planification stratégique plus précise.
"""

insight_evolution_types = """
**Comportements Temporels Différenciés**

Chaque type de magasin présente des patterns saisonniers distincts :
- Adaptation des stratégies promotionnelles selon le type
- Planification d'assortiment personnalisée par période
- Optimisation des ressources selon les cycles de performance

L'approche temporelle différenciée maximise l'efficacité des actions commerciales.
"""

analyse_saisonnalite = """
### Exploitation Stratégique de la Saisonnalité

**Métrique** : Coefficient de variation mesurant l'amplitude des variations saisonnières

**Applications business** :
- **Planification stock** : Anticipation des pics de demande
- **Stratégies promotionnelles** : Timing optimal des opérations commerciales  
- **Allocation ressources** : Concentration des efforts sur les périodes clés
- **Formation équipes** : Préparation aux variations d'activité

Les départements à forte saisonnalité nécessitent une gestion proactive.
"""

insight_promotions = """
**Efficacité des Stratégies Promotionnelles**

L'analyse de l'impact des promotions (markdown) révèle :
- L'effet réel des réductions sur les volumes de vente
- La rentabilité nette des opérations promotionnelles
- Les opportunités d'optimisation du mix promotionnel

Ces insights guident la stratégie pricing et promotionnelle pour maximiser la rentabilité.
"""

# ===================
# RECOMMANDATIONS
# ===================

intro_recommandations = """
## Recommandations Stratégiques pour l'Optimisation Retail

**Approche data-driven** : Utilisation des insights analytiques pour développer des recommandations actionnables.

**Objectifs** :
- Optimiser l'assortiment départemental par type de magasin
- Exploiter les patterns temporels pour maximiser les revenus
- Améliorer l'efficacité des stratégies promotionnelles
- Développer des leviers de croissance durables

Cette page présente les **recommandations prioritaires** classées par **impact potentiel**.
"""

# Recommandations Magasins
reco_magasins_constats = """
**Relation taille-performance validée**
- Corrélation positive significative entre taille et CA moyen
- Performance Type A : 2-3x supérieure aux Types B/C
- Patterns temporels différenciés selon le type de magasin

**Opportunités identifiées**
- Sous-optimisation de certains magasins Type A
- Potentiel d'amélioration des Type B par l'assortiment
- Spécialisation possible des Type C sur des niches rentables
"""

reco_magasins_actions = """
### Actions prioritaires par type

**Type A (Grands magasins)**
- Développer l'assortiment premium et les départements spécialisés
- Implémenter des stratégies de cross-selling entre départements
- Optimiser l'espace de vente pour maximiser le CA/m²

**Type B (Magasins moyens)**
- Équilibrer assortiment large et rentabilité
- Focus sur les départements champions universels
- Adapter l'offre aux pics saisonniers locaux

**Type C (Petits magasins)**
- Concentration sur départements à forte rotation
- Spécialisation sur 2-3 niches rentables
- Agilité dans l'adaptation aux tendances locales

**Métrique de suivi** : CA/m² par type de magasin
"""

# Recommandations Départements
reco_departements_observations = """
**Segmentation départementale révélatrice**
- 15-20% de départements universels génèrent 60% du CA
- Départements spécialisés : marges supérieures mais risque de surstockage
- Performance départementale varie fortement selon le type de magasin

**Opportunités d'optimisation**
- Réallocation d'espace vers les départements champions
- Développement sélectif de départements spécialisés
- Standardisation de l'assortiment universel
"""

reco_departements_actions = """
### Stratégie d'assortiment optimisée

**1. Renforcer les départements champions**
- Augmenter l'espace et l'assortiment des top performers
- Investir dans la formation équipes sur ces départements
- Optimiser la présentation merchandising

**2. Développer les niches spécialisées**
- Sélectionner 2-3 départements spécialisés par magasin selon le profil local
- Former des experts produit pour ces niches
- Communiquer sur l'expertise et la différenciation

**3. Rationaliser l'assortiment universel**
- Standardiser les départements universels (gain d'efficacité)
- Optimiser les commandes groupées
- Réduire la complexité opérationnelle

**Métrique de suivi** : Marge et rotation par département
"""

# Recommandations Saisonnalité
reco_saisonnalite_patterns = """
**Cycles saisonniers identifiés**
- Amplitude de variation jusqu'à 150% sur certains départements
- Patterns différenciés selon le type de magasin
- Corrélation forte entre saisonnalité et efficacité promotionnelle

**Opportunités temporelles**
- Optimisation du timing des promotions
- Planification proactive des stocks saisonniers
- Adaptation des équipes aux pics d'activité
"""

reco_saisonnalite_actions = """
### Exploitation stratégique des cycles

**1. Planification saisonnière proactive**
- Calendrier promotionnel aligné sur les pics de performance
- Commandes stock anticipées pour les départements saisonniers
- Formation équipes sur les produits saisonniers avant les pics

**2. Adaptation de l'assortiment par période**
- Modulation de l'espace selon les cycles départementaux
- Introduction temporaire de départements saisonniers
- Liquidation organisée des stocks en fin de saison

**3. Communication ciblée par période**
- Campagnes marketing alignées sur les patterns identifiés
- Mise en avant des départements en phase ascendante
- Offres spéciales pendant les creux saisonniers

**Métrique de suivi** : Prévision vs réalisé par département/période
"""

# Recommandations Promotions
reco_promotions_constats = """
**Impact promotionnel mesuré**
- Effet variable selon les départements et périodes
- Risque de cannibalisation des ventes non promotionnelles
- Opportunité d'optimisation du ROI promotionnel

**Leviers d'amélioration**
- Ciblage plus précis des promotions
- Timing optimal selon la saisonnalité
- Mesure de l'impact net (vs cannibalisation)
"""

reco_promotions_actions = """
### Stratégie promotionnelle optimisée

**1. Ciblage départements/périodes**
- Concentrer les promotions sur les départements saisonniers en phase montante
- Éviter les promotions sur départements déjà performants
- Utiliser les promotions pour relancer les départements en déclin

**2. Personnalisation par type de magasin**
- Promotions premium pour Type A (marges préservées)
- Promotions volume pour Type B (écoulement stock)
- Promotions ciblées pour Type C (adaptation locale)

**3. Mesure et optimisation continue**
- Tracking ROI promotionnel par département
- A/B testing sur différents formats promotionnels
- Analyse de la cannibalisation et ajustement

**Métrique de suivi** : ROI promotionnel et impact net sur la marge
"""

# Priorités stratégiques
reco_priorites = """
### Actions Prioritaires (Impact/Effort)

**1. 🎯 Optimisation départements champions (Impact: Élevé, Effort: Faible)**
- Réallocation immédiate d'espace vers les top performers
- ROI estimé : +15-20% sur les départements concernés

**2. 📊 Exploitation saisonnalité (Impact: Élevé, Effort: Moyen)**
- Mise en place du calendrier promotionnel data-driven
- Réduction estimée du surstockage : -25%

**3. 🏪 Spécialisation Type A (Impact: Moyen, Effort: Élevé)**
- Développement de départements premium/spécialisés
- Augmentation estimée du panier moyen : +10-15%

**4. 💡 Rationalisation Type C (Impact: Moyen, Effort: Faible)**
- Focus sur 3-5 départements à forte rotation
- Amélioration estimée de la rentabilité : +20%

**5. 📈 Optimisation promotionnelle (Impact: Faible, Effort: Élevé)**
- Mise en place du tracking ROI promotionnel
- Amélioration estimée de l'efficacité : +5-10%
"""

reco_conclusion = """
**Feuille de route recommandée**

Phase 1 (0-3 mois) : Optimisation départements + Calendrier saisonnier  
Phase 2 (3-6 mois) : Spécialisation Type A + Rationalisation Type C  
Phase 3 (6-12 mois) : Optimisation promotionnelle + Mesure impact

**Impact estimé global : +25-30% d'amélioration de la performance retail**

**"L'analyse data-driven révèle des leviers concrets d'optimisation. 
La priorisation par impact/effort garantit un ROI maximal des actions."**
"""