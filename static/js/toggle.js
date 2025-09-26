document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("togglePassword");
  const passwordInput = document.getElementById("password");
  const eyeIcon = document.getElementById("eyeIcon");

  let visible = false;

  toggleBtn.addEventListener("click", function () {
    visible = !visible;
    passwordInput.type = visible ? "text" : "password";

    // Cambiar icono (opcional: requiere tener eye.svg y eye-off.svg en static/img)
    eyeIcon.src = visible
      ? "/static/img/eye-off.svg"
      : "/static/img/eye.svg";
    eyeIcon.alt = visible ? "Ocultar contraseña" : "Mostrar contraseña";
  });
});
