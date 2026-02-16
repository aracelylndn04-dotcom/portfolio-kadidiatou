function envoyerMessage() {
  const nom = document.getElementById("nom").value.trim();
  const msg = document.getElementById("msg").value.trim();
  const resultat = document.getElementById("resultat");

  if (nom === "" || msg === "") {
    resultat.textContent = " Merci de remplir ton nom et ton message avant d’envoyer.";
    return;
  }

  resultat.textContent =
    " Merci " + nom + " ! Ton message a bien été noté. Je te répondrai dès que possible ";
}
function ajouterAvis() {
  const nom = document.getElementById("avisNom").value;
  const texte = document.getElementById("avisTexte").value;
  const message = document.getElementById("messageAvis");
  const liste = document.getElementById("listeAvis");

  if (nom === "" || texte === "") {
    message.innerText = "Veuillez remplir les champs.";
    message.style.color = "red";
    return;
  }

  const avis = document.createElement("div");
  avis.className = "avis-item";
  avis.innerHTML = `<strong>${nom}</strong><p>${texte}</p>`;

  liste.prepend(avis);

  message.innerText = "Merci d’avoir laissé un avis sur mon portfolio et d’avoir pris le temps de visiter."<br>
  "Au plaisir d'être parmis vous et d’échanger avec vous."
  message.style.color = "green";

  document.getElementById("avisNom").value = "";
  document.getElementById("avisTexte").value = "";
}