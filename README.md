# IPL-Genie

A Web-App Created Using Basic HTML, CSS on the front-end and Flask on the back-end which Predicts the Outcome of an IPL
match Using Machine Learning (Logistic regression).

Live on http://ipl-genie.herokuapp.com/


# Machine Learning Model:
Used Logistic Regression Algorithm to Train the Model using IPL Dataset Sourced from Kaggle.

Test accuracy of 65-70%



# Team Rating Calculation:

Team A rating = (1-(0.1*position of team A on points table))+(No. of matches Team A has won Against Team B in the past / Total no. of Matches Played Between Team A and Team B)

Team B rating = (1-(0.1*position of team B on points table))+(No. of matches Team B has won Against Team A in the past / Total no. of Matches Played Between Team A and Team B)
