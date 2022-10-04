const radio1 = document.getElementById("flexRadioDefault1");
const radio2 = document.getElementById("flexRadioDefault2");
const radio3 = document.getElementById("flexRadioDefault3");
const input = document.getElementById("formFileLg");

radio1.addEventListener("click", () => {
  if (radio1.checked) {
    input.name = "unit";
    input.removeAttribute("disabled");
  }
});

radio2.addEventListener("click", () => {
  if (radio2.checked) {
    input.name = "spesifikasi";
    input.removeAttribute("disabled");
  }
});

radio3.addEventListener("click", () => {
  if (radio3.checked) {
    input.name = "pengusahaan";
    input.removeAttribute("disabled");
  }
});
