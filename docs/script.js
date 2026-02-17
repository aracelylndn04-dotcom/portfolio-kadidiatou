const SUPABASE_URL = "https://snftxnsaxjjobxkzlq.supabase.co";   
const SUPABASE_KEY = "sb_publishable_nZQHebJywm7-e_OLXoJEng_FEbvtuf0"; 

function envoyerAvis() {
  const nom = document.getElementById("avisNom").value.trim();
  const texte = document.getElementById("avisTexte").value.trim();
  const message = document.getElementById("messageAvis");

  if (!nom || !texte) {
    message.innerText = "Remplis tous les champs.";
    return;
  }

  fetch(`${SUPABASE_URL}/rest/v1/avis`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "apikey": SUPABASE_KEY,
      "Authorization": `Bearer ${SUPABASE_KEY}`
    },
    body: JSON.stringify({ nom, texte })
  })
  .then(res => {
    if (!res.ok) throw new Error("Erreur Supabase");
    message.innerText = "Avis publié ✅";
    document.getElementById("avisNom").value = "";
    document.getElementById("avisTexte").value = "";
    chargerAvis();
  })
  .catch(() => {
    message.innerText = "Erreur : impossible de publier l'avis.";
  });
}

function chargerAvis() {
  fetch(`${SUPABASE_URL}/rest/v1/avis?select=*&order=created_at.desc`, {
    headers: {
      "apikey": SUPABASE_KEY,
      "Authorization": `Bearer ${SUPABASE_KEY}`
    }
  })
  .then(res => res.json())
  .then(data => {
    const liste = document.getElementById("listeAvis");
    if (!liste) return;

    liste.innerHTML = "";
    data.forEach(a => {
      const div = document.createElement("div");
      div.className = "avis-item";
      div.innerHTML = `<strong>${a.nom}</strong><br>${a.texte}`;
      liste.appendChild(div);
    });
  });
}

window.addEventListener("load", chargerAvis);