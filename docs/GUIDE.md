# 📘 Guide d'installation et d'utilisation
## SISE Ultimate Games — Controller Profiler

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.10 ou supérieur** — [télécharger](https://www.python.org/downloads/)
- **Une manette Xbox ou PlayStation** branchée en USB ou via Bluetooth
  *(un fallback clavier est disponible, mais les analyses comportementales seront moins précises)*
- Le fichier **`.env`** fourni avec le rendu (contient les clés Supabase et Mistral AI)

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/YassineCHN/SISE_ULTIMATE_GAMES.git
cd SISE_ULTIMATE_GAMES
```

### 2. Créer un environnement virtuel

Choisissez l'une des trois méthodes :

**pip + venv** (standard)
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**conda**
```bash
conda create -n sise-games python=3.10
conda activate sise-games
```

**uv** (ultra-rapide)
```bash
uv venv --python 3.10

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
# pip
pip install -r requirements.txt

# conda
pip install -r requirements.txt

# uv
uv pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Placer le fichier `.env` fourni à la **racine du projet** (au même niveau que `main.py`).

Il doit contenir :

```env
SUPABASE_URL=https://votre-projet.supabase.co
SUPABASE_KEY=votre_clé_anon_publique
MISTRAL_API_KEY=votre_clé_api_mistral
```

> **Sans ce fichier**, l'application fonctionne en mode dégradé : les sessions sont sauvegardées localement en CSV et les résumés IA sont générés en local (mock).

### 5. Vérifier la manette (optionnel)

Pour s'assurer que la manette est bien détectée :

```bash
python test_controller.py
```

Une fenêtre Pygame s'ouvre et affiche en temps réel l'état de tous les axes et boutons de la manette.

---

## 🎮 Utilisation

### Workflow recommandé — tout depuis le dashboard

L'application est conçue pour être pilotée depuis le **dashboard Dash**. C'est lui qui orchestre le lancement des jeux et centralise toutes les visualisations en temps réel.

**Étape 1 — Démarrer le dashboard**

```bash
cd app
python app.py
```

Ouvrir ensuite [http://localhost:8050](http://localhost:8050) dans votre navigateur.

**Étape 2 — Lancer une session de jeu**

1. Aller sur la page **Live Session** dans le menu de gauche
2. Saisir votre **nom de joueur**
3. Choisir un **jeu** parmi : Reflex, Labyrinthe, Shooter, Racing
4. Cliquer sur **Lancer** — la fenêtre Pygame s'ouvre
5. Jouer avec la manette — le dashboard affiche les inputs en direct
6. À la fin de la session, la fenêtre Pygame se ferme automatiquement et le résumé IA apparaît dans l'onglet **Résumés**

**Étape 3 — Explorer vos données**

| Page | Contenu |
|---|---|
| 🎮 **Live Session** | Lancement des jeux + flux d'inputs temps réel |
| 👤 **Profils** | Carte UMAP des joueurs, profil attribué, radar de features |
| 🏆 **Leaderboard** | Classements par jeu et global |
| 📋 **Résumés IA** | Analyses Mistral post-session : points forts, axes d'amélioration, objectif |
| 💬 **Chat IA** | Coach conversationnel avec accès à l'historique des sessions |
| 🤖 **Agent IA** | Lancer un agent qui imite le style d'un joueur enregistré |

---

### Contrôles en jeu

| Action | Manette | Clavier (fallback) |
|---|---|---|
| Déplacement | Joystick gauche | `Z Q S D` |
| Viser / Regarder | Joystick droit | Souris |
| Tirer / Action | Gâchette droite `RT` | `Espace` |
| Bouton action | `A / B / X / Y` | `J K L I` |
| Nitro (Racing) | `LB` / `RB` | `Shift` |
| Quitter | `Start` | `Échap` |

---

### Lancement direct en ligne de commande (optionnel)

Il est possible de lancer un jeu sans passer par le dashboard :

```bash
# Syntaxe
python main.py <game_id> <nom_joueur>

# Exemples
python main.py reflex Modou
python main.py shooter Yassine
python main.py racing Nico
python main.py labyrinth Modou
```

> ⚠️ Dans ce cas, les stats ne sont **pas visualisées en temps réel**. La session est sauvegardée dans Supabase et consultable ensuite dans le dashboard.

---

### Lancer l'agent imitateur en ligne de commande

```bash
# Imiter le style d'un joueur réel (données Supabase)
python main.py shooter Agent_IA --agent Modou --mode player

# Avec niveau de fidélité configurable (0.0 = clone parfait, 2.0 = très bruité)
python main.py racing Agent_IA --agent Yassine --mode player --noise 0.5

# Lister les profils disponibles pour un jeu
python main.py reflex _ --list-profiles
```

---

## 🛠️ Résolution de problèmes fréquents

**La manette n'est pas détectée**
- Débrancher et rebrancher la manette avant de lancer l'application
- Vérifier avec `python test_controller.py`
- Sur Windows, s'assurer que le driver Xbox est installé

**`ModuleNotFoundError` au lancement**
- Vérifier que l'environnement virtuel est bien activé
- Relancer `pip install -r requirements.txt`

**Le dashboard ne se connecte pas à Supabase**
- Vérifier que le fichier `.env` est bien à la racine du projet
- Contrôler que les clés `SUPABASE_URL` et `SUPABASE_KEY` sont correctes
- L'application fonctionne en mode dégradé (mock) si Supabase est indisponible

**Le résumé IA ne s'affiche pas**
- Vérifier la clé `MISTRAL_API_KEY` dans le `.env`
- Le résumé est généré en arrière-plan (~10-30s après la fin de la session)
- Rafraîchir la page **Résumés** après quelques secondes

**Erreur Pygame au lancement d'un jeu**
- S'assurer que `pygame` est bien installé : `pip install pygame==2.6.1`
- Sur Linux, installer les dépendances système : `sudo apt-get install python3-pygame`

---

## 📁 Structure des fichiers importants

```
SISE_ULTIMATE_GAMES/
├── main.py              ← Point d'entrée ligne de commande
├── requirements.txt     ← Dépendances Python
├── .env                 ← Clés API (à placer ici)
├── app/
│   └── app.py           ← Démarrage du dashboard (python app/app.py)
├── data/
│   └── sessions.csv     ← Sauvegarde locale des sessions (mode dégradé)
└── test_controller.py   ← Diagnostic manette
```
