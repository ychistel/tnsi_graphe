document.addEventListener("DOMContentLoaded", function() {
    const regions = document.querySelectorAll("#map path");
    const colorPicker = document.getElementById("colorPicker");

    regions.forEach(region => {
        // Initialisation de la couleur de remplissage
        region.style.fill = "#ffffff";
        
        // Gestion du clic sur une région
        region.addEventListener("click", function() {
            // Récupérer la couleur choisie
            const selectedColor = colorPicker.value;
            // Appliquer la couleur à la région cliquée
            region.style.fill = selectedColor;
        });
    });
});
