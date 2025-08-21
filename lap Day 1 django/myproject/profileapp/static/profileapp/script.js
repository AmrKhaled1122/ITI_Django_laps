
document.addEventListener('DOMContentLoaded', function() {
  const btn = document.getElementById('say-hello');
  if (!btn) return;

  btn.addEventListener('click', function() {
    // read the name text from the DOM (safe, no template in JS)
    const nameEl = document.getElementById('profile-name');
    const name = nameEl ? nameEl.textContent.trim() : 'there';
    alert('Hello, ' + name + '!');
  });
});
