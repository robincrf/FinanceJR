from helpers import filtre_csv
import numpy as np

class RendementAnalyzer:
    """
    Classe pour analyser les rendements financiers
    """
    
    def __init__(self):
        """Initialise l'analyseur de rendements"""
        pass
    
    def calculate_rt(self, p1, p2):
        """
        Calcule le rendement journalier entre deux prix
        
        Args:
            p1: Prix au temps t+1 (plus récent)
            p2: Prix au temps t (plus ancien)
            
        Returns:
            Le rendement journalier
        """
        return (p1 - p2) / p1

    def create_rt_list(self, price_list):
        """
        Crée une liste des rendements journaliers à partir d'une liste de prix
        
        Args:
            price_list: Liste des prix chronologiques
            
        Returns:
            Liste des rendements journaliers
        """
        if len(price_list) < 2:
            return []
            
        returns_list = []
        for i in range(len(price_list) - 1):
            return_rate = self.calculate_rt(price_list[i], price_list[i+1])
            returns_list.append(return_rate)
        return returns_list

    def mean_rt(self, returns_list):
        """
        Calcule la moyenne des rendements journaliers
        
        Args:
            returns_list: Liste des rendements
            
        Returns:
            La moyenne des rendements
        """
        if not returns_list:
            return 0
            
        return sum(returns_list) / len(returns_list)

    def variance(self, returns_list):
        """
        Calcule la variance des rendements journaliers
        
        Args:
            returns_list: Liste des rendements
            
        Returns:
            La variance des rendements
        """
        if len(returns_list) < 2:
            return 0
            
        mean = self.mean_rt(returns_list)
        variance_sum = sum((r - mean) ** 2 for r in returns_list)
        return variance_sum / (len(returns_list) - 1)

    def standard_deviation(self, returns_list):
        """
        Calcule l'écart-type des rendements journaliers
        
        Args:
            returns_list: Liste des rendements
            
        Returns:
            L'écart-type des rendements
        """
        return np.sqrt(self.variance(returns_list))
    
    def analyze_price_series(self, price_list):
        """
        Analyse complète d'une série de prix
        
        Args:
            price_list: Liste des prix chronologiques
            
        Returns:
            Dictionnaire contenant les statistiques des rendements
        """
        returns = self.create_rt_list(price_list)
        
        return {
            'returns': returns,
            'mean_return': self.mean_rt(returns),
            'variance': self.variance(returns),
            'standard_deviation': self.standard_deviation(returns),
            'count': len(returns)
        }


    
    
    
    """    

from helpers import filtre_csv
import numpy as np

class rt:
    #rendement journalier
    def rt(self, p1,p2):
        return (p1-p2) / p2

    def create_rt_list(self, price_list):
        n = price_list
        rt_list =[]
        for i in range(0,n-1):
            p = (price_list[i+1] - price_list[i]) / price_list[i]
            rt_list.append(p)
        return rt_list

    # moyenne des rendement journaliers
    def mean_rt(self, rt_list):
        sum = 0
        n = len(rt_list)
        for p in rt_list:
            sum += p
        return sum / n


    # variance des rendements journaliers 
    def standard_deviation(self, rt_list):
        sum = 0
        n = len(rt_list)
        m = np(rt_list)
        for p in rt_list:
            sum += np.pow(p-m, 2)
        
        
        sd = np.sqrt(sum/ (n-1))
        return sd

 """ 