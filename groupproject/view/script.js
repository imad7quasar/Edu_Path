// script.js
let currentFieldset = 0;
const fieldsets = document.querySelectorAll('fieldset');

function showFieldset(index) {
  fieldsets.forEach((fieldset, idx) => {
    if (idx === index) {
      fieldset.style.display = 'block';
    } else {
      fieldset.style.display = 'none';
    }
  });
}
 
         
function nextPage() {
  if (currentFieldset < fieldsets.length - 1) {
    currentFieldset++;
    showFieldset(currentFieldset);
  }
}

function prevPage() {
  if (currentFieldset > 0) {
    currentFieldset--;
    showFieldset(currentFieldset);
  }
}

// Show the first fieldset initially
showFieldset(currentFieldset);
