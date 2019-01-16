# MH

Title: 
IPF in Python 

Summary: 
The package performs the two-dimensional iterative proportional fitting [1] method (IPF) for trip distribution as applicable in trip modelling. The program is written in Python and uses numpy arrays for handling zone to zone trip matrices. The inputs are three csv files containing origin target trips (rows), destination target trips (columns), and a seed matrix which contains the initial number of trips between each origin and destination zone pair. The result is a converged matrix in txt format showing the future number of trips between each origin and destination pair as distributed according to the trip weights found in the original seed matrix [2].

Statement of Need: 
The application of the IPF method is in the area of travel demand modelling.

Author Name: 
Mina Hassanvand

Affiliation: 
Stantec Consulting Ltd

References: 
[1] L. Rüschendorf. Convergence of the iterative proportional fitting procedure. Annals of Statistics, pages 1160--1174, 1995.
[2] M. Ben-Akiva and S. Lerman. Discrete Choice Analysis: Theory and Application to Travel Demand. MIT Press, 1985.

