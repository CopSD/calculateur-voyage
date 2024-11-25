import streamlit as st

# Function to calculate the cost
def calcul_tarif(nb_pax, nb_jours, villes_nuits, choix_guide, nb_jours_guide, nb_repas, prix_repas):
    # Hotel rates per city (per night)
    tarifs_hotels = {
        "Amman": 100,
        "Madaba": 80,
        "Petra": 120,
        "Wadi Rum": 90,
        "Dana": 70,
        "Aqaba": 150,
        "Dead Sea": 200,
        "Autre": 60
    }

    # Accommodation cost
    cout_hebergement = sum(tarifs_hotels[ville] * nuits for ville, nuits in villes_nuits.items())

    # Guide cost
    if nb_pax < 7:
        cout_guide = 50 * nb_jours_guide if choix_guide else 0
    else:
        cout_guide = (nb_jours - 3) * 50  # Example automatic calculation

    # Transport costs based on number of pax
    if 1 <= nb_pax <= 2:
        transport_cout = 115 * nb_jours
    elif 3 <= nb_pax <= 5:
        transport_cout = 200 * nb_jours
    elif 6 <= nb_pax <= 9:
        transport_cout = 280 * nb_jours
    elif 10 <= nb_pax <= 14:
        transport_cout = 340 * nb_jours
    elif 15 <= nb_pax <= 25:
        transport_cout = 500 * nb_jours
    else:
        transport_cout = 600 * nb_jours

    # Meal cost
    cout_repas = nb_repas * prix_repas

    # Total cost calculation
    cout_total = cout_hebergement + cout_guide + transport_cout + cout_repas
    tarif_par_personne = cout_total / nb_pax

    return cout_total, tarif_par_personne

# Title of the application
st.title("Calculateur de Tarifs de Voyage")

# User inputs
nb_pax = st.number_input("Nombre de pax :", min_value=1, value=1)
nb_jours = st.number_input("Nombre de jours :", min_value=1, value=1)

# Adding cities and nights
st.subheader("Ajouter des villes et le nombre de nuits")
villes_nuits = {}
while True:
    ville = st.text_input("Ville (ex: Amman) :", "")
    nuits = st.number_input("Nombre de nuits :", min_value=0, value=1)
    
    if st.button("Ajouter Ville"):
        if ville:
            villes_nuits[ville] = nuits
            st.success(f"Ville {ville} avec {nuits} nuits ajoutée.")
        else:
            st.error("Veuillez entrer une ville.")
    
    if st.button("Terminer l'ajout de villes"):
        break

# Guide option
choix_guide = st.radio("Souhaitez-vous un guide ?", ("Oui", "Non")) == "Oui"
nb_jours_guide = st.number_input("Nombre de jours de guide :", min_value=0, value=0)

# Meal inputs
nb_repas = st.number_input("Nombre de repas :", min_value=0, value=1)
prix_repas = st.number_input("Prix par repas :", min_value=0.0, value=10.0)

# Button to calculate the cost
if st.button("Calculer Tarif"):
    cout_total, tarif_par_personne = calcul_tarif(nb_pax, nb_jours, villes_nuits, choix_guide, nb_jours_guide, nb_repas, prix_repas)
    st.success(f"Tarif total : {cout_total:.2f} €")
    st.success(f"Tarif par personne : {tarif_par_personne:.2f} €")
