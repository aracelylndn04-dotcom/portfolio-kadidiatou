const SUPABASE_URL = "https://snftxnsaxjjobxkzlq.supabase.co";
const SUPABASE_KEY = "sb_publishable_nZQHebJywm7-e_OLXoJEng_FEbvtuf0";

async function postAvis(payload) {
  return fetch(`${SUPABASE_URL}/rest/v1/avis`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "apikey": SUPABASE_KEY,
      "Authorization": `Bearer ${SUPABASE_KEY}`,
      "Prefer": "return=minimal"
    },
    body: JSON.stringify(payload)
  });
}

async function envoyerAvis() {
  const pseudo = document.getElementById("avisNom").value.trim();
  const avis = document.getElementById("avisTexte").value.trim();
  const message = document.getElementById("messageAvis");

  if (!pseudo || !avis) {
    message.innerText = "Remplis tous les champs.";
    return;
  }

  message.innerText = "Envoi en cours...";

  try {
    // 1) essai avec colonnes minuscules
    let res = await postAvis({ nom: pseudo, texte: avis });

    // 2) si échec, essai avec colonnes majuscules (Nom / Texte)
    if (!res.ok) {
      res = await postAvis({ Nom: pseudo, Texte: avis });
    }

    if (!res.ok) {
      const errText = await res.text();
      console.log("Supabase error:", res.status, errText);
      message.innerText = `Erreur (${res.status}) : ${errText}`;
      return;
    }

    message.innerText = "Avis publié ✅";
    document.getElementById("avisNom").value = "";
    document.getElementById("avisTexte").value = "";
    await chargerAvis();
  } catch (e) {
    console.error(e);
    message.innerText = "Erreur : impossible de publier l'avis (réseau/JS).";
  }
}

async function chargerAvis() {
  const liste = document.getElementById("listeAvis");
  if (!liste) return;

  const res = await fetch(`${SUPABASE_URL}/rest/v1/avis?select=*&order=created_at.desc`, {
    headers: {
      "apikey": SUPABASE_KEY,
      "Authorization": `Bearer ${SUPABASE_KEY}`
    }
  });

  if (!res.ok) {
    const t = await res.text();
    console.log("Load error:", res.status, t);
    return;
  }

  const data = await res.json();
  liste.innerHTML = "";

  data.forEach(a => {
    const div = document.createElement("div");
    div.className = "avis-item";
    div.innerHTML = `<strong>${a.nom ?? a.Nom}</strong><br>${a.texte ?? a.Texte}`;
    liste.appendChild(div);
  });
}

window.addEventListener("load", chargerAvis);