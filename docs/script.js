/* ================== CONFIG SUPABASE ================== */
const SUPABASE_URL = "https://TON-PROJECT-REF.supabase.co";  // <-- remplace
const SUPABASE_KEY = "TON_ANON_PUBLIC_KEY";                  // <-- remplace (clé publishable anon)

/* ================== AVIS ================== */
Script 
function envoyerAvis(){

const nom = document.getElementById("avisNom").value;
const texte = document.getElementById("avisTexte").value;

if(nom === "" || texte === ""){
document.getElementById("messageAvis").textContent = "Veuillez remplir tous les champs.";
return;
}

let avis = JSON.parse(localStorage.getItem("avisPortfolio")) || [];

avis.push({
nom: nom,
texte: texte
});

localStorage.setItem("avisPortfolio", JSON.stringify(avis));

document.getElementById("avisNom").value = "";
document.getElementById("avisTexte").value = "";

document.getElementById("messageAvis").textContent = "Avis publié !";

afficherAvis();

}

function afficherAvis(){

const liste = document.getElementById("listeAvis");
liste.innerHTML = "";

let avis = JSON.parse(localStorage.getItem("avisPortfolio")) || [];

avis.forEach(a => {

const div = document.createElement("div");
div.classList.add("avis-item");

div.innerHTML = `
<strong>${a.nom}</strong>
<p>${a.texte}</p>
`;

liste.appendChild(div);

});

}

document.addEventListener("DOMContentLoaded", afficherAvis);