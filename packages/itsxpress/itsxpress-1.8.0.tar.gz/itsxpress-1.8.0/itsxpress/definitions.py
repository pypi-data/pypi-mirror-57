"""Definitions.py: variables shared across the package.

"""
import os

# This is the project Root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define Taxa that Hmms were created for
# A = Alveolata
# B = Bryophyta
# C = Bacillariophyta
# D = Amoebozoa
# E = Euglenozoa
# F = Fungi
# G = Chlorophyta (green algae)
# H = Rhodophyta (red algae)
# I = Phaeophyceae (brown algae)
# L = Marchantiophyta (liverworts)
# M = Metazoa
# N = Microsporidia (No longer present in ITSx files)
# O = Oomycota
# P = Haptophyceae (prymnesiophytes)
# Q = Raphidophyceae
# R = Rhizaria
# S = Synurophyceae
# T = Tracheophyta (higher plants)
# U = Eustigmatophyceae
# X = Apusozoa (No longer present in ITSx files)
# Y = Parabasalia (No longer present in ITSx files)

taxa_choices = ["Alveolata", "Bryophyta", "Bacillariophyta","Amoebozoa", "Euglenozoa", "Fungi",
 "Chlorophyta","Rhodophyta","Phaeophyceae","Marchantiophyta","Metazoa",
 "Oomycota","Haptophyceae", "Raphidophyceae"," Rhizaria","Synurophyceae",
 "Tracheophyta","Eustigmatophyceae", "All"]

taxa_dict = {"Alveolata":"A.hmm","Bryophyta":"B.hmm", "Bacillariophyta":"C.hmm",
 "Amoebozoa":"D.hmm", "Euglenozoa":"E.hmm", "Fungi":"F.hmm","Chlorophyta":"G.hmm",
 "Rhodophyta":"H.hmm","Phaeophyceae":"I.hmm","Marchantiophyta":"L.hmm","Metazoa":"M.hmm",
 "Oomycota":"O.hmm","Haptophyceae":"P.hmm",
 "Raphidophyceae":"Q.hmm"," Rhizaria":"R.hmm","Synurophyceae":"S.hmm",
 "Tracheophyta":"T.hmm","Eustigmatophyceae":"U.hmm","All":"all.hmm"}


maxmismatches = 40
maxratio=0.3
