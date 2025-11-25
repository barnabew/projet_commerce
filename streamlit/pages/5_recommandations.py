import streamlit as st
import styles

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="recommandations")

st.markdown("<div class='section-header'>🧭 Recommandations Stratégiques</div>", unsafe_allow_html=True)
st.markdown("""
Cette page regroupe les recommandations concrètes issues des analyses :
- Ventes & performance globale  
- Logistique & délais  
- Produits  
- Géographie  
- Comportement clients  
""")

st.divider()
# --------------------------------------------------------------------------
# 1. LOGISTIQUE & DÉLAIS DE LIVRAISON
# --------------------------------------------------------------------------
st.header("1️⃣ Logistique & Délais de Livraison")

st.subheader("🚨 Problèmes identifiés")
st.markdown("""
- Les délais > 10 jours font chuter significativement les notes (jusqu’à 3.2/5).  
- Le taux de **mauvaises reviews** dépasse **35%** au-delà de 20 jours.  
- Certaines routes logistiques, notamment **SP → Nord**, sont clairement plus lentes.
""")

st.subheader("🎯 Recommandations")
st.markdown("""
- **Optimiser les routes critiques** : prioriser les flux SP → (PA, AM, RR, AP).  
- **Alerte automatique** sur commandes dépassant l’estimation initiale.  
- **Partenariats logistiques régionaux** dans le Nord/Nord-Est pour réduire 2–4 jours.  
- **Proposer un suivi plus transparent** pour réduire l’insatisfaction liée à l’attente.
""")

st.divider()
# --------------------------------------------------------------------------
# 2. PRODUITS & ASSORTIMENT
# --------------------------------------------------------------------------
st.header("2️⃣ Produits & Assortiment")

st.subheader("🚨 Problèmes identifiés")
st.markdown("""
- Quelques catégories génèrent des **notes très faibles** (ex : office furniture 3.49/5).  
- D'autres sont **à fort potentiel** : health_beauty, gifts, sports…  
- Le pricing + shipping impacte fortement la satisfaction dans certaines catégories.
""")

st.subheader("🎯 Recommandations")
st.markdown("""
- **Auditer les mauvaises catégories** (packaging, qualité, fournisseurs).  
- **Mettre en avant les catégories héro** dans campagnes marketing.  
- **Optimiser le pricing + shipping** pour les articles volumineux (mobilier).  
- **Créer des bundles** pour augmenter le panier moyen dans les catégories populaires.
""")

st.divider()
# --------------------------------------------------------------------------
# 3. GÉOGRAPHIE & EXPANSION
# --------------------------------------------------------------------------
st.header("3️⃣ Géographie & Expansion")

st.subheader("🚨 Constat")
st.markdown("""
- Le CA est très concentré : SP > RJ > MG.  
- Certaines régions ont un **panier moyen élevé** mais une faible base client (ex: Norte).  
- Les délais y sont souvent plus longs → impact direct sur les notes.
""")

st.subheader("🎯 Recommandations")
st.markdown("""
- **Campagnes ciblées** dans RS, PR, SC : bonnes notes et bons délais → potentiel d’expansion.  
- **Développer des hubs logistiques** dans NO/NE pour accélérer la livraison.  
- **Publicité géographique** : push sur les régions où la concurrence est faible.
""")

st.divider()
# --------------------------------------------------------------------------
# 4. CLIENTS & COMPORTEMENT D'ACHAT
# --------------------------------------------------------------------------
st.header("4️⃣ Clients & Comportement d’Achat")

st.subheader("🚨 Observations clés")
st.markdown("""
- **97% des clients sont “one-time buyers”** → problème majeur.  
- La récence n’est pas exploitable (données incomplètes).  
- Les clients qui dépensent le plus ne laissent pas forcément de meilleures notes.  
- Une hausse du montant (monetary) augmente la probabilité de mauvaise note.
""")

st.subheader("🎯 Recommandations")
st.markdown("""
- **Améliorer l’expérience du premier achat (critical !)**  
  - Page produit plus claire  
  - Photos + descriptions enrichies  
  - Garantie / retours simplifiés  

- **Réduire le nombre de mauvaises premières expériences** :  
  - Alertes logistiques  
  - Vérification fournisseur avant expédition  

- **Campagnes de retargeting uniquement pour les clients satisfaits**.

- **STRATÉGIE D’ACQUISITION plutôt que fidélisation** :  
  - Puisque presque tous les clients achètent une fois.  
  - Focus sur SEO, réseaux sociaux, ads produit.
""")

st.divider()
# --------------------------------------------------------------------------
# 5. PRIORITÉS STRATÉGIQUES (SYNTHÈSE)
# --------------------------------------------------------------------------
st.header("5️⃣ Priorités Stratégiques (Top 5)")

st.markdown("""
### 🥇 1. Accélérer la livraison (levier n°1 pour améliorer la note client)
### 🥈 2. Améliorer la qualité des catégories problématiques (mobilier, audio…)
### 🥉 3. Investir dans l’acquisition : les clients reviennent très peu
### 🏅 4. Développer la logistique dans le Nord & Nord-Est
### 🎖 5. Mettre en avant les produits les plus performants en marketing
""")

st.success("📌 Cette page regroupe les recommandations les plus importantes pour orienter la stratégie business.")
