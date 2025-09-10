def probability_of_disease(accuracy, prevalence):
    # Write your code here.
    disease_inaccuracy = 1 - accuracy
    not_prevalence = 1 - prevalence

    # Using Bayes' Theorem
    accurate_disease = (prevalence * accuracy) / ((prevalence * accuracy) + (not_prevalence * disease_inaccuracy))
    accurate_no_disease = not_prevalence * accuracy / ((not_prevalence * accuracy) + (prevalence * disease_inaccuracy))
    
    return [accurate_disease*100, accurate_no_disease*100]
