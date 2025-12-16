"""
queries.py
Requêtes SQL pour le dashboard Retail Analytics
"""

# ===================
# KPIs PRINCIPAUX
# ===================

QUERY_CA_TOTAL = """
SELECT ROUND(SUM(Weekly_Sales), 2) AS CA_Total
FROM sales;
"""

QUERY_CA_MOYEN = """
SELECT ROUND(AVG(Weekly_Sales), 2) AS CA_Moyen
FROM sales;
"""

QUERY_NB_MAGASINS = """
SELECT COUNT(DISTINCT Store) AS Nb_Magasins
FROM sales;
"""

QUERY_NB_DEPARTEMENTS = """
SELECT COUNT(DISTINCT Dept) AS Nb_Departements
FROM sales;
"""

# ===================
# ANALYSES MAGASINS
# ===================

QUERY_TYPES_PERFORMANCE = """
SELECT 
    s.Type,
    COUNT(DISTINCT s.Store) AS Nb_Magasins,
    ROUND(AVG(s.Size), 0) AS Taille_Moyenne,
    ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen
FROM sales sa
JOIN stores s ON sa.Store = s.Store
GROUP BY s.Type
ORDER BY Taille_Moyenne DESC;
"""

QUERY_TYPES_DETAILED = """
SELECT 
    s.Type,
    COUNT(DISTINCT s.Store) AS Nb_Magasins,
    ROUND(AVG(s.Size), 0) AS Taille_Moyenne,
    ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen,
    ROUND(SUM(sa.Weekly_Sales), 2) AS CA_Total
FROM sales sa
JOIN stores s ON sa.Store = s.Store
GROUP BY s.Type
ORDER BY Taille_Moyenne DESC;
"""

QUERY_TAILLE_PERFORMANCE = """
SELECT 
    sa.Store,
    s.Size,
    s.Type,
    ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen
FROM sales sa
JOIN stores s ON sa.Store = s.Store
GROUP BY sa.Store, s.Size, s.Type;
"""

# ===================
# ANALYSES DÉPARTEMENTS
# ===================

QUERY_TOP_DEPARTMENTS = """
SELECT 
    Dept,
    ROUND(SUM(Weekly_Sales), 2) AS CA_Total,
    ROUND(AVG(Weekly_Sales), 2) AS CA_Moyen,
    COUNT(DISTINCT Store) AS Nb_Magasins
FROM sales
GROUP BY Dept
ORDER BY CA_Total DESC;
"""

QUERY_SEGMENTATION_DEPARTEMENTS = """
WITH dept_presence AS (
    SELECT 
        Dept,
        COUNT(DISTINCT Store) as Nb_Magasins,
        ROUND(COUNT(DISTINCT Store) * 100.0 / 
              (SELECT COUNT(DISTINCT Store) FROM sales), 1) AS Taux_Presence,
        ROUND(SUM(Weekly_Sales), 2) AS CA_Total,
        CASE 
            WHEN COUNT(DISTINCT Store) * 100.0 / 
                 (SELECT COUNT(DISTINCT Store) FROM sales) >= 90 THEN 'Universel'
            WHEN COUNT(DISTINCT Store) * 100.0 / 
                 (SELECT COUNT(DISTINCT Store) FROM sales) >= 70 THEN 'Courant' 
            WHEN COUNT(DISTINCT Store) * 100.0 / 
                 (SELECT COUNT(DISTINCT Store) FROM sales) >= 40 THEN 'Sélectif'
            ELSE 'Spécialisé'
        END AS Categorie
    FROM sales
    GROUP BY Dept
)
SELECT 
    Categorie,
    COUNT(*) as Nb_Depts,
    ROUND(AVG(Taux_Presence), 1) as Taux_Moyen,
    ROUND(AVG(CA_Total), 0) as CA_Moyen_Dept
FROM dept_presence
GROUP BY Categorie
ORDER BY CA_Moyen_Dept DESC;
"""

def get_query_departements_champions(min_presence):
    return f"""
    WITH dept_stats AS (
        SELECT 
            Dept,
            COUNT(DISTINCT Store) as Nb_Magasins,
            ROUND(COUNT(DISTINCT Store) * 100.0 / 
                  (SELECT COUNT(DISTINCT Store) FROM sales), 1) AS Taux_Presence,
            ROUND(SUM(Weekly_Sales), 2) AS CA_Total,
            ROUND(AVG(Weekly_Sales), 2) AS CA_Moyen
        FROM sales
        GROUP BY Dept
        HAVING Taux_Presence >= {min_presence}
    )
    SELECT * FROM dept_stats
    ORDER BY CA_Total DESC;
    """

def get_query_departements_specialises(max_presence):
    return f"""
    WITH dept_stats AS (
        SELECT 
            Dept,
            COUNT(DISTINCT Store) as Nb_Magasins,
            ROUND(COUNT(DISTINCT Store) * 100.0 / 
                  (SELECT COUNT(DISTINCT Store) FROM sales), 1) AS Taux_Presence,
            ROUND(SUM(Weekly_Sales), 2) AS CA_Total,
            ROUND(SUM(Weekly_Sales) / COUNT(DISTINCT Store), 2) AS CA_Moyen_Magasin
        FROM sales
        GROUP BY Dept
        HAVING Taux_Presence <= {max_presence} AND CA_Total > 10000
    )
    SELECT * FROM dept_stats
    ORDER BY CA_Moyen_Magasin DESC;
    """

QUERY_DEPT_BY_TYPE = """
SELECT 
    s.Type,
    sa.Dept,
    ROUND(SUM(sa.Weekly_Sales), 2) AS CA_Total,
    ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen,
    COUNT(DISTINCT sa.Store) AS Nb_Magasins,
    RANK() OVER (PARTITION BY s.Type ORDER BY SUM(sa.Weekly_Sales) DESC) as Rang
FROM sales sa
JOIN stores s ON sa.Store = s.Store
GROUP BY s.Type, sa.Dept
ORDER BY s.Type, CA_Total DESC;
"""

def get_query_perf_by_type(store_type):
    return f"""
    SELECT 
        sa.Dept,
        ROUND(SUM(sa.Weekly_Sales), 2) AS CA_Total,
        ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen,
        COUNT(DISTINCT sa.Store) AS Nb_Magasins
    FROM sales sa
    JOIN stores s ON sa.Store = s.Store
    WHERE s.Type = '{store_type}'
    GROUP BY sa.Dept
    ORDER BY CA_Moyen DESC;
    """

# ===================
# ANALYSES TEMPORELLES
# ===================

QUERY_EVOLUTION_MENSUELLE = """
SELECT 
    CAST(strftime('%m', Date) as INTEGER) as Mois,
    ROUND(SUM(Weekly_Sales), 2) as CA_Total_Mensuel,
    ROUND(SUM(Weekly_Sales) / COUNT(*), 2) as CA_Moyen_Hebdo
FROM sales
GROUP BY strftime('%m', Date)
ORDER BY Mois;
"""

QUERY_EVOLUTION_BY_TYPE = """
WITH type_monthly AS (
    SELECT 
        s.Type,
        CAST(strftime('%m', sa.Date) as INTEGER) as Mois,
        ROUND(SUM(sa.Weekly_Sales) / COUNT(*), 2) as CA_Moyen_Hebdo,
        CASE CAST(strftime('%m', sa.Date) as INTEGER)
            WHEN 1 THEN 'Jan' WHEN 2 THEN 'Fév' WHEN 3 THEN 'Mar'
            WHEN 4 THEN 'Avr' WHEN 5 THEN 'Mai' WHEN 6 THEN 'Jun'
            WHEN 7 THEN 'Jul' WHEN 8 THEN 'Aoû' WHEN 9 THEN 'Sep'
            WHEN 10 THEN 'Oct' WHEN 11 THEN 'Nov' WHEN 12 THEN 'Déc'
        END as Nom_Mois
    FROM sales sa
    JOIN stores s ON sa.Store = s.Store
    GROUP BY s.Type, strftime('%m', sa.Date)
)
SELECT 
    Mois,
    Nom_Mois,
    SUM(CASE WHEN Type = 'A' THEN CA_Moyen_Hebdo END) as Type_A,
    SUM(CASE WHEN Type = 'B' THEN CA_Moyen_Hebdo END) as Type_B,
    SUM(CASE WHEN Type = 'C' THEN CA_Moyen_Hebdo END) as Type_C
FROM type_monthly
GROUP BY Mois, Nom_Mois
ORDER BY Mois;
"""

def get_query_departements_saisonniers(seuil_variation):
    return f"""
    WITH dept_monthly AS (
        SELECT 
            Dept,
            CAST(strftime('%m', Date) as INTEGER) as Mois,
            SUM(Weekly_Sales) / COUNT(*) as CA_Moyen_Hebdo,
            COUNT(*) as Nb_Semaines
        FROM sales
        GROUP BY Dept, strftime('%m', Date)
    ),
    dept_stats AS (
        SELECT 
            Dept,
            AVG(CA_Moyen_Hebdo) as CA_Moyen_Global,
            MAX(CA_Moyen_Hebdo) as CA_Max,
            MIN(CA_Moyen_Hebdo) as CA_Min,
            SUM(Nb_Semaines) as Total_Semaines,
            COUNT(DISTINCT Mois) as Mois_Actifs
        FROM dept_monthly
        GROUP BY Dept
        HAVING Total_Semaines >= 40 AND ABS(CA_Moyen_Global) > 2000
    )
    SELECT 
        ds.Dept,
        ROUND(ds.CA_Moyen_Global, 0) as CA_Moyen_Global,
        ROUND(ds.CA_Max, 0) as Pic_CA,
        ROUND(ds.CA_Min, 0) as Creux_CA,
        ROUND(ABS(ds.CA_Max - ds.CA_Min) / ABS(ds.CA_Moyen_Global) * 100, 1) as Coefficient_Variation
    FROM dept_stats ds
    WHERE ABS(ds.CA_Max - ds.CA_Min) / ABS(ds.CA_Moyen_Global) * 100 >= {seuil_variation}
    ORDER BY Coefficient_Variation DESC;
    """

def get_query_evolution_top_depts(dept_list):
    dept_str = ','.join(map(str, dept_list))
    dept_cases = '\n'.join([f"    SUM(CASE WHEN Dept = {dept} THEN CA_Moyen_Hebdo END) as Dept_{dept}," for dept in dept_list])
    
    return f"""
    WITH dept_monthly AS (
        SELECT 
            Dept,
            CAST(strftime('%m', Date) as INTEGER) as Mois,
            ROUND(SUM(Weekly_Sales) / COUNT(*), 2) as CA_Moyen_Hebdo,
            CASE CAST(strftime('%m', Date) as INTEGER)
                WHEN 1 THEN 'Jan' WHEN 2 THEN 'Fév' WHEN 3 THEN 'Mar'
                WHEN 4 THEN 'Avr' WHEN 5 THEN 'Mai' WHEN 6 THEN 'Jun'
                WHEN 7 THEN 'Jul' WHEN 8 THEN 'Aoû' WHEN 9 THEN 'Sep'
                WHEN 10 THEN 'Oct' WHEN 11 THEN 'Nov' WHEN 12 THEN 'Déc'
            END as Nom_Mois
        FROM sales
        WHERE Dept IN ({dept_str})
        GROUP BY Dept, strftime('%m', Date)
    )
    SELECT 
        Mois,
        Nom_Mois,
{dept_cases.rstrip(',')}
    FROM dept_monthly
    GROUP BY Mois, Nom_Mois
    ORDER BY Mois;
    """

# ===================
# PROMOTIONS
# ===================

QUERY_IMPACT_PROMOTIONS = """
SELECT 
    CASE 
        WHEN (COALESCE(f.MarkDown1, 0) + COALESCE(f.MarkDown2, 0) + 
              COALESCE(f.MarkDown3, 0) + COALESCE(f.MarkDown4, 0) + 
              COALESCE(f.MarkDown5, 0)) > 0 THEN 'Avec Promo'
        ELSE 'Sans Promo'
    END AS Statut_Promo,
    COUNT(*) as Nb_Observations,
    ROUND(AVG(sa.Weekly_Sales), 2) AS CA_Moyen
FROM features f
JOIN sales sa ON f.Store = sa.Store AND f.Date = sa.Date
GROUP BY Statut_Promo;
"""