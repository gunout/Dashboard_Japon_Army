# dashboard_defense_japon_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Japon",
    page_icon="🗾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé avec couleurs japonaises
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #BC002D, #FFFFFF, #BC002D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #BC002D, #FF6B6B);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #BC002D;
        border-bottom: 3px solid #FFFFFF;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-force-card {
        background: linear-gradient(135deg, #0055B7, #0077CC);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #8B0000, #B22222);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .strategic-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .alliance-card {
        background: linear-gradient(135deg, #0d47a1, #1976d2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .defense-card {
        background: linear-gradient(135deg, #2e7d32, #4caf50);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseJaponDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.missile_systems = self.define_missile_systems()
        self.naval_assets = self.define_naval_assets()
        
    def define_branches_options(self):
        return [
            "Forces d'Auto-Défense Japonaises", "Forces Terrestres d'Auto-Défense", 
            "Forces Maritimes d'Auto-Défense", "Forces Aériennes d'Auto-Défense",
            "Commandement de la Défense Spatiale", "Commandement Cyber",
            "Garde Côtière Japonaise", "Unité des Opérations Spéciales"
        ]
    
    def define_programmes_options(self):
        return [
            "Défense Anti-Missile Intégrée", "Capacités de Contre-Attaque",
            "Défense des Îles Éloignées", "Modernisation des Forces Maritimes",
            "Supériorité Aérospatiale", "Coopération Alliance USA-Japon",
            "Cyber Défense Avancée", "Défense Spatiale"
        ]
    
    def define_missile_systems(self):
        return {
            "SM-3 Block IIA": {"type": "Interceptor ABM", "portee": 2500, "altitude": 1000, "statut": "Opérationnel"},
            "PAC-3 MSE": {"type": "Défense AA/BM", "portee": 35, "altitude": 20, "statut": "Opérationnel"},
            "Type 03 Chu-SAM": {"type": "Défense AA", "portee": 50, "altitude": 10, "statut": "Opérationnel"},
            "12-Type SSM": {"type": "Missile Anti-Navire", "portee": 200, "vitesse": "Mach 0.9", "statut": "Opérationnel"},
            "ASM-3": {"type": "Missile Air-Sol", "portee": 400, "vitesse": "Mach 3", "statut": "Déploiement"}
        }
    
    def define_naval_assets(self):
        return {
            "Classe Izumo": {"type": "Porte-hélicoptères", "deplacement": 27000, "aeronav": "28 hélicoptères", "statut": "Opérationnel"},
            "Classe Maya": {"type": "Destroyer AEGIS", "deplacement": 10800, "armement": "SM-3, SM-6", "statut": "Opérationnel"},
            "Classe Soryu": {"type": "Sous-marin", "deplacement": 4200, "propulsion": "AIP", "statut": "Opérationnel"},
            "Classe Mogami": {"type": "Frégate", "deplacement": 5500, "armement": "Missiles mer-mer", "statut": "Opérationnel"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour le Japon"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Defense': self.simulate_advanced_defense(annees),
            'Temps_Reponse_Jours': self.simulate_advanced_response(annees),
            'Tests_Intercepteurs': self.simulate_interceptor_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Anti_Access': self.simulate_a2ad_capacity(annees),
            'Couverture_BMD': self.simulate_bmd_coverage(annees),
            'Resilience_Cyber': self.simulate_cyber_resilience(annees),
            'Capacites_ISR': self.simulate_isr_capabilities(annees),
            'Cooperation_USA': self.simulate_us_cooperation(annees)
        }
        
        # Données spécifiques aux programmes
        if 'defense_missile' in config.get('priorites', []):
            data.update({
                'Intercepteurs_BMD': self.simulate_bmd_interceptors(annees),
                'Couverture_Radar': self.simulate_radar_coverage(annees),
                'Taux_Interception': self.simulate_interception_rate(annees)
            })
        
        if 'maritime' in config.get('priorites', []):
            data.update({
                'Navires_Combat': self.simulate_naval_vessels(annees),
                'Destroyers_AEGIS': self.simulate_aegis_destroyers(annees),
                'Sous_Marins': self.simulate_submarines(annees)
            })
        
        if 'aerospatial' in config.get('priorites', []):
            data.update({
                'Satellites_Militaires': self.simulate_military_satellites(annees),
                'Capacite_Antisatellite': self.simulate_antisatellite_capability(annees),
                'Avions_Combat': self.simulate_fighter_aircraft(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Incidents_Cyber_Controles': self.simulate_cyber_incidents(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour le Japon"""
        configs = {
            "Forces d'Auto-Défense Japonaises": {
                "type": "armee_totale",
                "budget_base": 50.0,
                "personnel_base": 240,
                "exercices_base": 80,
                "priorites": ["defense_missile", "maritime", "aerospatial", "cyber", "alliance"],
                "doctrines": ["Défense Collective", "Réponse Dynamique", "Dissuasion Intégrée"],
                "capacites_speciales": ["Défense BMD", "Opérations Amphibies", "Guerre ASW"]
            },
            "Forces Maritimes d'Auto-Défense": {
                "type": "branche_navale",
                "personnel_base": 45,
                "exercices_base": 25,
                "priorites": ["bmd", "asw", "amphibie", "mines"],
                "flottes_principales": ["Flotte d'Escorte", "Flotte Sous-marine", "Aviation Navale"],
                "navires_cles": ["Destroyers AEGIS", "Sous-marins Soryu", "Porte-hélicoptères Izumo"]
            },
            "Forces Aériennes d'Auto-Défense": {
                "type": "branche_aerienne",
                "personnel_base": 50,
                "exercices_base": 30,
                "priorites": ["interception", "bmd", "isr", "transport"],
                "squadrons_cles": ["F-15J", "F-2", "F-35A", "E-767 AWACS"],
                "bases_principales": ["Kadena", "Misawa", "Hyakuri"]
            },
            "Défense Anti-Missile Intégrée": {
                "type": "programme_strategique",
                "budget_base": 8.0,
                "priorites": ["intercepteurs", "radars", "commandement", "integration_usa"],
                "composantes": ["AEGIS Ashore", "PAC-3", "SM-3", "Radars J/FPS-5"],
                "couverture": "Archipel japonais et bases US"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 30,
            "exercices_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec augmentations récentes"""
        budget_base = config.get('budget_base', 45.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.02 * (annee - 2000))  # Croissance modérée
            # Augmentations selon périodes
            if 2006 <= annee <= 2010:  # Post-9/11 et menaces nord-coréennes
                base *= 1.05
            elif 2012 <= annee <= 2015:  # Tensions Senkaku/Diaoyu
                base *= 1.08
            elif annee >= 2018:  # Modernisation face à la Chine
                base *= 1.12
            elif annee >= 2022:  # Sécurité nationale renforcée
                base *= 1.25
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs professionnels"""
        personnel_base = config.get('personnel_base', 250)
        # Légère augmentation avec professionnalisation
        return [personnel_base * (1 + 0.003 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [0.9 + 0.05 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec coopération US"""
        base = config.get('exercices_base', 60)
        return [base + 3 * (annee - 2000) + 8 * np.sin(2 * np.pi * (annee - 2000)/2) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 85 + 0.5 * (annee - 2000)  # Départ élevé, amélioration continue
            if annee >= 2006:  # Réformes post-9/11
                base += 5
            if annee >= 2014:  # Modernisation
                base += 4
            if annee >= 2020:  # Préparation accrue
                base += 3
            readiness.append(min(base, 96))
        return readiness
    
    def simulate_advanced_defense(self, annees):
        """Capacité de défense avancée"""
        defense = []
        for annee in annees:
            base = 80  # Défense solide
            if annee >= 2007:
                base += 3  # Systèmes BMD
            if annee >= 2015:
                base += 6  # Modernisation
            if annee >= 2021:
                base += 5  # Contre-mesures avancées
            defense.append(min(base, 94))
        return defense
    
    def simulate_advanced_response(self, annees):
        """Temps de réponse avancé"""
        return [max(10 - 0.3 * (annee - 2000), 3) for annee in annees]
    
    def simulate_interceptor_tests(self, annees):
        """Tests d'intercepteurs"""
        tests = []
        for annee in annees:
            if annee < 2006:
                tests.append(2)
            elif annee < 2012:
                tests.append(4 + (annee - 2006))
            elif annee < 2018:
                tests.append(8 + 2 * (annee - 2012))
            else:
                tests.append(15 + 3 * (annee - 2018))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(80 + 1.2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_a2ad_capacity(self, annees):
        """Capacités Anti-Access/Area Denial"""
        return [min(70 + 2.0 * (annee - 2000), 92) for annee in annees]
    
    def simulate_bmd_coverage(self, annees):
        """Couverture de défense anti-missile balistique"""
        return [min(60 + 3.0 * (annee - 2000), 95) for annee in annees]
    
    def simulate_cyber_resilience(self, annees):
        """Résilience cybernétique"""
        return [min(75 + 2.2 * (annee - 2000), 94) for annee in annees]
    
    def simulate_isr_capabilities(self, annees):
        """Capacités ISR (Intelligence, Surveillance, Reconnaissance)"""
        return [min(80 + 1.8 * (annee - 2000), 96) for annee in annees]
    
    def simulate_us_cooperation(self, annees):
        """Niveau de coopération avec les USA"""
        cooperation = []
        for annee in annees:
            base = 85  # Alliance solide
            if annee >= 2001:
                base += 5  # Post-9/11
            if annee >= 2012:
                base += 3  # Pivot vers l'Asie
            if annee >= 2017:
                base += 4  # Coopération renforcée
            cooperation.append(min(base, 98))
        return cooperation
    
    def simulate_bmd_interceptors(self, annees):
        """Intercepteurs BMD déployés"""
        return [min(10 + 2 * (annee - 2000), 50) for annee in annees]
    
    def simulate_radar_coverage(self, annees):
        """Couverture radar"""
        return [min(70 + 2.5 * (annee - 2000), 95) for annee in annees]
    
    def simulate_interception_rate(self, annees):
        """Taux d'interception estimé"""
        return [min(75 + 1.5 * (annee - 2000), 92) for annee in annees]
    
    def simulate_naval_vessels(self, annees):
        """Nombre de navires de combat"""
        return [min(120 + 3 * (annee - 2000), 160) for annee in annees]
    
    def simulate_aegis_destroyers(self, annees):
        """Destroyers AEGIS"""
        aegis = []
        for annee in annees:
            if annee < 2007:
                aegis.append(4)
            elif annee < 2012:
                aegis.append(6)
            elif annee < 2018:
                aegis.append(8)
            else:
                aegis.append(10 + (annee - 2018))
        return [min(a, 15) for a in aegis]
    
    def simulate_submarines(self, annees):
        """Sous-marins en service"""
        return [min(16 + 0.5 * (annee - 2000), 24) for annee in annees]
    
    def simulate_military_satellites(self, annees):
        """Satellites militaires en orbite"""
        return [min(5 + 1.5 * (annee - 2000), 20) for annee in annees]
    
    def simulate_antisatellite_capability(self, annees):
        """Capacité antisatellite"""
        return [min(40 + 2.5 * (annee - 2000), 85) for annee in annees]
    
    def simulate_fighter_aircraft(self, annees):
        """Avions de combat"""
        return [min(250 + 5 * (annee - 2000), 350) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(80 + 1.8 * (annee - 2000), 95) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(75 + 2.0 * (annee - 2000), 93) for annee in annees]
    
    def simulate_cyber_incidents(self, annees):
        """Incidents cyber contrôlés (%)"""
        return [min(85 + 1.0 * (annee - 2000), 97) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🗾 ANALYSE STRATÉGIQUE AVANCÉE - JAPON</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #BC002D, #FFFFFF); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ FORCES D'AUTO-DÉFENSE JAPONAISES - SYSTÈME DE DÉFENSE INTÉGRÉ</h3>
            <p><strong>Analyse multidimensionnelle des capacités défensives et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Forces d'Auto-Défense Japonaises"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Crise Taïwan", "Attaque Nord-Coréenne", "Conflit Territorial"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS PROFESSIONNELS</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ Forces hautement entraînées</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers']), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="defense-card">
                <h4>🛡️ DÉFENSE ANTI-MISSILE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} intercepteurs BMD</p>
            </div>
            """.format(data_actuelle['Couverture_BMD'], 
                     int(data_actuelle.get('Intercepteurs_BMD', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="alliance-card">
                <h4>🤝 COOPÉRATION USA</h4>
                <h2>{:.0f}%</h2>
                <p>⚡ Alliance stratégique</p>
            </div>
            """.format(data_actuelle['Cooperation_USA']), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Reponse_Jours'] - data_actuelle['Temps_Reponse_Jours']) / 
                             data_2000['Temps_Reponse_Jours']) * 100
            st.metric(
                "⏱️ Temps Réponse",
                f"{data_actuelle['Temps_Reponse_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            if 'Destroyers_AEGIS' in df.columns:
                croissance_aegis = ((data_actuelle['Destroyers_AEGIS'] - data_2000.get('Destroyers_AEGIS', 4)) / 
                                  data_2000.get('Destroyers_AEGIS', 4)) * 100
                st.metric(
                    "🚢 Destroyers AEGIS",
                    f"{data_actuelle['Destroyers_AEGIS']:.0f}",
                    f"{croissance_aegis:+.1f}%"
                )
        
        with col7:
            croissance_bmd = ((data_actuelle['Couverture_BMD'] - data_2000['Couverture_BMD']) / 
                            data_2000['Couverture_BMD']) * 100
            st.metric(
                "🎯 Couverture BMD",
                f"{data_actuelle['Couverture_BMD']:.1f}%",
                f"{croissance_bmd:+.1f}%"
            )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Defense', 'Resilience_Cyber', 'Couverture_BMD']
            noms = ['Préparation Opér.', 'Capacité Défense', 'Résilience Cyber', 'Couverture BMD']
            couleurs = ['#BC002D', '#FFFFFF', '#2d3436', '#0d47a1']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS DÉFENSIVES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Intercepteurs_BMD' in df.columns:
                strategic_data.append(df['Intercepteurs_BMD'])
                strategic_names.append('Intercepteurs BMD')
            
            if 'Tests_Intercepteurs' in df.columns:
                strategic_data.append(df['Tests_Intercepteurs'])
                strategic_names.append('Tests Intercepteurs')
            
            if 'Destroyers_AEGIS' in df.columns:
                strategic_data.append(df['Destroyers_AEGIS'])
                strategic_names.append('Destroyers AEGIS')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des enjeux stratégiques
            st.markdown("""
            <div class="defense-card">
                <h4>🎯 ENJEUX STRATÉGIQUES RÉGIONAUX</h4>
                <p><strong>Mer de Chine Orientale:</strong> Îles Senkaku/Diaoyu</p>
                <p><strong>Détroit de Taïwan:</strong> Stabilité régionale</p>
                <p><strong>Mer du Japon:</strong> Menaces nord-coréennes</p>
                <p><strong>Pacifique Nord:</strong> Routes maritimes vitales</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des alliances
            st.markdown("""
            <div class="alliance-card">
                <h4>🌐 ARCHITECTURE DE SÉCURITÉ</h4>
                <p><strong>USA:</strong> Alliance fondamentale</p>
                <p><strong>Corée du Sud:</strong> Coopération trilatérale</p>
                <p><strong>Australie:</strong> Partenaire Quad</p>
                <p><strong>ASEAN:</strong> Partenariats sécuritaires</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des menaces
            menaces_data = {
                'Année': [2006, 2009, 2012, 2016, 2017, 2022, 2023],
                'Événement': ['Essai TN-1', 'Essai TN-2', 'Tensions Senkaku', 'Essais multiples', 'Missile Hwasong', 'Essais records', 'Menaces accrues'],
                'Niveau Menace': [6, 7, 5, 8, 8, 9, 9]  # sur 10
            }
            menaces_df = pd.DataFrame(menaces_data)
            
            fig = px.bar(menaces_df, x='Année', y='Niveau Menace', 
                        title="📉 ÉVOLUTION DES MENACES RÉGIONALES",
                        labels={'Niveau Menace': 'Niveau de Menace'},
                        color='Niveau Menace',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Évolution de la posture défensive
            posture = [min(70 + 2 * (annee - 2000), 90) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=posture,
                         title="🛡️ ÉVOLUTION DE LA POSTURE DÉFENSIVE",
                         labels={'x': 'Année', 'y': 'Niveau de Posture (%)'})
            fig.update_traces(fillcolor='rgba(188, 0, 45, 0.3)', line_color='#BC002D')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['SM-3 Block IIA', 'F-35A', 'Destroyer Maya', 'Sous-marin Taigei', 
                           'PAC-3 MSE', 'Avion E-767'],
                'Portée (km)': [2500, 2200, 0, 0, 35, 0],
                'Année Service': [2018, 2018, 2020, 2022, 2020, 2000],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Modernisation']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des capacités navales
            naval_data = {
                'Type Navire': ['Destroyers AEGIS', 'Frégates', 'Sous-marins', 'Navires ASW', 'Bâtiments débarquement'],
                '2000': [4, 20, 16, 40, 10],
                '2027': [12, 25, 22, 55, 15]
            }
            naval_df = pd.DataFrame(naval_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=naval_df['Type Navire'], y=naval_df['2000'],
                                marker_color='#1e3c72'))
            fig.add_trace(go.Bar(name='2027', x=naval_df['Type Navire'], y=naval_df['2027'],
                                marker_color='#BC002D'))
            
            fig.update_layout(title="🚢 MODERNISATION DE LA FLOTTE NAVALE",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="strategic-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Yokosuka:</strong> Base principale US Navy</p>
                <p><strong>Sasebo:</strong> Base Maritime JMSDF</p>
                <p><strong>Misawa:</strong> Base aérienne majeure</p>
                <p><strong>Okinawa:</strong> Position avancée stratégique</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="defense-card">
                <h4>🎯 DOCTRINE D'AUTO-DÉFENSE</h4>
                <p><strong>Défense collective:</strong> Sécurité mutuelle</p>
                <p><strong>Réponse dynamique:</strong> Flexibilité opérationnelle</p>
                <p><strong>Dissuasion intégrée:</strong> Multi-couches</p>
                <p><strong>Coopération étroite:</strong> Alliance USA-Japon</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="alliance-card">
                <h4>⚡ STRATÉGIE DE DÉFENSE ANTI-MISSILE</h4>
                <p><strong>Défense en couches:</strong> SM-3 + PAC-3</p>
                <p><strong>Intégration US:</strong> Commandement unifié</p>
                <p><strong>Surveillance avancée:</strong> Radars J/FPS</p>
                <p><strong>Réponse immédiate:</strong> Alerte permanente</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="navy-card">
                <h4>🛡️ DOCTRINE NAVALE AVANCÉE</h4>
                <p><strong>Guerre ASW:</strong> Supériorité sous-marine</p>
                <p><strong>Défense aérienne:</strong> Couverture AEGIS</p>
                <p><strong>Opérations amphibies:</strong> Défense îles</p>
                <p><strong>Protection SLOC:</strong> Routes commerciales</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="strategic-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES JAPONAISES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Défense proactive:</strong> Anticipation des menaces</div>
                <div><strong>• Interopérabilité:</strong> Intégration avec alliés</div>
                <div><strong>• Rapidité de réponse:</strong> Temps de réaction minimal</div>
                <div><strong>• Flexibilité opérationnelle:</strong> Adaptation multi-scénarios</div>
                <div><strong>• Supériorité technologique:</strong> Avantage qualitatif</div>
                <div><strong>• Résilience:</strong> Capacité de récupération</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Missiles NK', 'Incursion Chinoise', 'Cyber Attaque', 
                                 'Blocus Maritime', 'Crise Taïwan', 'Actions Russes'],
                'Probabilité': [0.9, 0.7, 0.8, 0.5, 0.6, 0.4],
                'Impact': [0.8, 0.7, 0.6, 0.9, 0.9, 0.5],
                'Niveau Préparation': [0.9, 0.8, 0.85, 0.7, 0.75, 0.6]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Attaque Missile', 'Incursion Maritime', 'Guerre Cyber', 
                           'Crise Régionale', 'Opérations Spéciales'],
                'Interception': [0.9, 0.3, 0.1, 0.6, 0.4],
                'Défense': [0.8, 0.8, 0.7, 0.8, 0.7],
                'Contre-Attaque': [0.4, 0.7, 0.6, 0.5, 0.8]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Interception', x=response_df['Scénario'], y=response_df['Interception']),
                go.Bar(name='Défense', x=response_df['Scénario'], y=response_df['Défense']),
                go.Bar(name='Contre-Attaque', x=response_df['Scénario'], y=response_df['Contre-Attaque'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="defense-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement BMD:</strong> Intercepteurs avancés</div>
                <div><strong>• Capacités de contre-attaque:</strong> Missiles de longue portée</div>
                <div><strong>• Défense cyber:</strong> Résilience numérique</div>
                <div><strong>• Coopération renforcée:</strong> Exercices conjoints</div>
                <div><strong>• Modernisation navale:</strong> Sous-marins et frégates</div>
                <div><strong>• Préparation îles:</strong> Déploiement avancé</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_defense_database(self):
        """Base de données des systèmes de défense"""
        st.markdown('<h3 class="section-header">🛡️ BASE DE DONNÉES DES SYSTÈMES DE DÉFENSE</h3>', 
                   unsafe_allow_html=True)
        
        defense_data = []
        for nom, specs in self.missile_systems.items():
            defense_data.append({
                'Système': nom,
                'Type': specs['type'],
                'Portée (km)': specs['portee'],
                'Altitude (km)': specs.get('altitude', 'N/A'),
                'Statut': specs['statut'],
                'Classification': 'Défensif'
            })
        
        defense_df = pd.DataFrame(defense_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(defense_df, x='Portée (km)', y='Altitude (km)',
                           size='Portée (km)', color='Type',
                           hover_name='Système', log_x=True,
                           title="🛡️ CARACTÉRISTIQUES DES SYSTÈMES DE DÉFENSE",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="defense-card">
                <h4>📋 INVENTAIRE DÉFENSIF</h4>
            """, unsafe_allow_html=True)
            
            for systeme in defense_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{systeme['Système']}</strong><br>
                    🎯 {systeme['Type']} • 🚀 {systeme['Portée (km)']} km<br>
                    📍 Alt: {systeme['Altitude (km)']} km • {systeme['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "🛡️ Systèmes Défensifs",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_defense_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - JAPON</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="defense-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Alliance USA Solide</strong>
                        <p>Coopération militaire et technologique approfondie</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🚢 Marine Technologiquement Avancée</strong>
                        <p>Flotte moderne avec capacités ASW et BMD de premier ordre</p>
                    </div>
                    <div class="air-force-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Défense Anti-Missile Intégrée</strong>
                        <p>Systèmes BMD parmi les plus avancés au monde</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Position Géostratégique</strong>
                        <p>Position clé pour le contrôle du Pacifique Nord</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>💥 Menaces Missilistiques</strong>
                        <p>Exposition aux missiles nord-coréens et chinois</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🏝️ Défense Territoire Étendu</strong>
                        <p>Difficulté à protéger les nombreuses îles éloignées</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>👥 Contraintes Démographiques</strong>
                        <p>Population vieillissante affectant le recrutement</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>⚖️ Limitations Constitutionnelles</strong>
                        <p>Contraintes légales sur les capacités offensives</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DÉFENSE ANTI-MISSILE</h5>
                    <p>• SM-3 Block IIA déployé<br>• AEGIS Ashore opérationnel<br>• Laser défensif<br>• Satellites d'alerte</p>
                </div>
                <div>
                    <h5>🚢 MODERNISATION NAVALE</h5>
                    <p>• Porte-avions légers<br>• Sous-marins Taigei<br>• Frégates nouvelles génération<br>• Drones maritimes</p>
                </div>
                <div>
                    <h5>💻 DOMAINE CYBER/ESPACE</h5>
                    <p>• Commandement cyber unifié<br>• Satellites de reconnaissance<br>• Guerre électronique avancée<br>• IA défensive</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="defense-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Renforcement capacités BMD<br>
                    • Modernisation forces navales<br>
                    • Développement contre-mesures<br>
                    • Protection infrastructures critiques</p>
                </div>
                <div>
                    <h5>⚡ COOPÉRATION RENFORCÉE</h5>
                    <p>• Intégration alliance USA-Japon<br>
                    • Partenariats régionaux élargis<br>
                    • Exercices multilatéraux<br>
                    • Partage intelligence</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseJaponDashboardAvance()
    dashboard.run_advanced_dashboard()