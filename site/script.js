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