
from modeles import moy_var as mv
import matplotlib.pyplot as plt
import numpy as np

# On retrouve les graphes de la moyenne, la volatilité (moyenne +- ecart type),  le nombre d'observations etc... 

def display_mean(price_list):
    rt = mv.RendementAnalyzer()
    rt_list = rt.create_rt_list(price_list)
    mean = rt.mean_rt(rt_list)
    sd = rt.standard_deviation(rt_list)
    time = len(rt_list) # correspond au nombre de jours - 1

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Graphique 1: Prix dans le temps
    ax1.plot(price_list, 'b-', linewidth=2, label='Prix')
    ax1.axhline(y=np.mean(price_list), color='r', linestyle='--', label=f'Prix moyen: {np.mean(price_list):.2f}')
    ax1.set_title(f'Évolution des prix ({time})')
    ax1.set_ylabel('Prix')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Graphique 2: Rendements
    ax2.plot(rt_list, 'g-', linewidth=1, label='Rendements journaliers')
    ax2.axhline(y=mean, color='r', linestyle='--', label=f'Rendement moyen: {mean:.4f}')
    ax2.axhline(y=mean + sd, color='orange', linestyle=':', alpha=0.7, label=f'+1 σ: {mean + sd:.4f}')
    ax2.axhline(y=mean - sd, color='orange', linestyle=':', alpha=0.7, label=f'-1 σ: {mean - sd:.4f}')
    ax2.set_title(f'Rendements et volatilité ({time})')
    ax2.set_ylabel('Rendement')
    ax2.set_xlabel('Période')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Afficher les statistiques
    print(f"\n=== ANALYSE {time.upper()} ===")
    print(f"Nombre d'observations: {len(rt_list)}")
    print(f"Rendement moyen: {mean:.6f}")
    print(f"Écart-type (volatilité): {sd:.6f}")
    print(f"Variance: {rt.standard_deviation:.8f}")









    


