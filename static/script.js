const $ = (id) => document.getElementById(id);
const zone = $("email");

// Exemples cliquables
EXEMPLES.forEach((texte) => {
  const b = document.createElement("button");
  b.type = "button";
  b.textContent = texte.length > 38 ? texte.slice(0, 38) + "…" : texte;
  b.onclick = () => { zone.value = texte; majCompteur(); analyser(); };
  $("exemples").appendChild(b);
});

function majCompteur() { $("compteur").textContent = zone.value.length + " / 5000"; }
zone.addEventListener("input", majCompteur);
$("effacer").onclick = () => { zone.value = ""; majCompteur(); $("resultat").hidden = true; $("vide").hidden = false; $("erreur").hidden = true; };

async function analyser() {
  $("erreur").hidden = true;
  $("analyser").disabled = true;
  try {
    const rep = await fetch("/api/classer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: zone.value }),
    });
    const data = await rep.json();
    if (!rep.ok) throw new Error(data.erreur || "Erreur du serveur");
    afficher(data);
  } catch (e) {
    $("erreur").textContent = e.message;
    $("erreur").hidden = false;
  } finally {
    $("analyser").disabled = false;
  }
}
$("analyser").onclick = analyser;

function afficher(d) {
  const cat = CATEGORIES[d.categorie] || { emoji: "✉️", couleur: "#FFB347" };
  $("vide").hidden = true;
  $("resultat").hidden = false;

  $("badge").textContent = cat.emoji + " " + d.categorie;
  $("badge").style.setProperty("--c", cat.couleur);
  $("confiance").textContent = d.confiance + " %";
  $("jauge-barre").style.width = "0%";
  requestAnimationFrame(() => { $("jauge-barre").style.width = d.confiance + "%"; });
  $("alerte").hidden = !d.incertain;

  const box = $("barres");
  box.innerHTML = "";
  Object.entries(d.probabilites).sort((a, b) => b[1] - a[1]).forEach(([nom, p]) => {
    const c = (CATEGORIES[nom] || {}).couleur || "#FFB347";
    const ligne = document.createElement("div");
    ligne.className = "barre-ligne";
    ligne.style.setProperty("--c", c);
    const n = document.createElement("span"); n.textContent = nom;
    const j = document.createElement("div"); j.className = "jauge";
    const f = document.createElement("div"); f.style.width = "0%"; j.appendChild(f);
    const v = document.createElement("b"); v.textContent = p + " %";
    ligne.append(n, j, v);
    box.appendChild(ligne);
    requestAnimationFrame(() => { f.style.width = p + "%"; });
  });
}
